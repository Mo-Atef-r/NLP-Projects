import streamlit as st
st.set_page_config(layout="wide")

import pandas as pd
import plotly.express as px
from gensim.models import LdaModel
from gensim.corpora.dictionary import Dictionary
from transformers import pipeline

# ==== Constants ====
MODEL_PATH = "D:/Data_and_AI/Projects/NLP/News Topic and Sentiment Explorer/Model"
DATA_PATH = "D:/Data_and_AI/Projects/NLP/News Topic and Sentiment Explorer/post_sentiment_data_7_topics.csv"

topic_names = {
    0: "Family",
    1: "Travel/ Lifestyle",
    2: "Crime / U.S. Local News",
    3: "Politics/ World News",
    4: "General Interests",
    5: "Entertainment",
    6: "Donald Trump"
}

# ==== Load Models and Data ====
@st.cache_resource
def load_lda():
    dictionary = Dictionary.load(f"{MODEL_PATH}/lda_dictionary.dict")
    lda_model = LdaModel.load(f"{MODEL_PATH}/lda_model_gensim")
    return lda_model, dictionary

@st.cache_resource
def load_sentiment_pipeline():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@st.cache_data
def load_dashboard_data():
    df = pd.read_csv(DATA_PATH)
    df['date'] = pd.to_datetime(df['date'])
    df['month_year'] = df['date'].dt.to_period('M').astype(str)
    df['month_year_dt'] = pd.to_datetime(df['month_year'])
    return df

lda_model, dictionary = load_lda()
sentiment_pipeline = load_sentiment_pipeline()
dashboard_df = load_dashboard_data()

# ==== Layout ====

st.title("📰 News Topic and Sentiment Explorer")

tab1, tab2 = st.tabs(["📌 Analyze Article", "📊 Dashboard"])

# ======= TAB 1: Analyze Single Article =======
with tab1:
    st.subheader("Analyze News Article")

    headline = st.text_input("Headline")
    description = st.text_area("Short Description")
    
    if st.button("Analyze"):
        full_text = f"{headline} {description}"
        bow_vector = dictionary.doc2bow(full_text.lower().split())
        topic_probs = lda_model.get_document_topics(bow_vector)

        # Map topics to names and sort
        topic_probs_named = [(topic_names.get(topic_id, f"Topic {topic_id}"), prob)
                             for topic_id, prob in topic_probs]
        top_topics = sorted(topic_probs_named, key=lambda x: x[1], reverse=True)[:3]

        # --- Plot topic distribution ---
        topic_df = pd.DataFrame(top_topics, columns=["Topic", "Probability"])
        fig_topic = px.bar(topic_df, x="Topic", y="Probability", title="Top 3 Topic Probabilities")
        st.plotly_chart(fig_topic, use_container_width=True)

        # --- Sentiment analysis ---
        result = sentiment_pipeline(full_text)[0]
        label = result["label"]
        score = result["score"]

        sentiment_df = pd.DataFrame({
            "Sentiment": ["Positive", "Negative"],
            "Probability": [score if label == "POSITIVE" else 1 - score,
                            1 - score if label == "POSITIVE" else score]
        })
        fig_sentiment = px.bar(sentiment_df, x="Sentiment", y="Probability", title="Sentiment Analysis")
        st.plotly_chart(fig_sentiment, use_container_width=True)

# ======= TAB 2: Dashboard =======
with tab2:
    st.subheader("Dashboard: News Trends Over Time")

    # === Sentiment Trend Over Time ===
    sentiment_over_time = dashboard_df.groupby(['month_year', 'sentiment_label']).size().unstack(fill_value=0)
    sentiment_over_time_prop = sentiment_over_time.div(sentiment_over_time.sum(axis=1), axis=0).reset_index()
    sentiment_over_time_long = sentiment_over_time_prop.melt(id_vars='month_year', var_name='Sentiment', value_name='Proportion')
    sentiment_over_time_long['month_year_dt'] = pd.to_datetime(sentiment_over_time_long['month_year'])

    fig_sentiment_trend = px.line(
        sentiment_over_time_long,
        x='month_year_dt',
        y='Proportion',
        color='Sentiment',
        title="📈 Overall Sentiment Trend Over Time (Monthly)",
        line_shape="spline",
        hover_data={'Proportion': ':.2%'}
    )
    st.plotly_chart(fig_sentiment_trend, use_container_width=True)

    # === Topic Trend Over Time ===
    topic_over_time = dashboard_df.groupby(['month_year', 'dominant_topic_id_lda']).size().unstack(fill_value=0)
    topic_over_time_prop = topic_over_time.div(topic_over_time.sum(axis=1), axis=0).reset_index()
    topic_over_time_long = topic_over_time_prop.melt(id_vars='month_year', var_name='Topic ID', value_name='Proportion')
    topic_over_time_long['month_year_dt'] = pd.to_datetime(topic_over_time_long['month_year'])
    topic_over_time_long['Topic Name'] = topic_over_time_long['Topic ID'].map(topic_names)

    # === Multiselect for topic filter ===
    all_topics = sorted(topic_over_time_long['Topic Name'].dropna().unique())
    selected_topics = st.multiselect("Select topics to display", all_topics, default=all_topics)

    filtered_topic_df = topic_over_time_long[topic_over_time_long['Topic Name'].isin(selected_topics)]

    fig_topic_trend = px.area(
        filtered_topic_df,
        x='month_year_dt',
        y='Proportion',
        color='Topic Name',
        title="📊 Topic Proportions Over Time (Monthly)",
        line_shape="spline",
        hover_data={'Proportion': ':.2%'}
    )
    st.plotly_chart(fig_topic_trend, use_container_width=True)
