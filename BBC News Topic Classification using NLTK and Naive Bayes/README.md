# BBC News Topic Classification with TF-IDF & Naive Bayes

## Overview
A machine learning pipeline that classifies BBC News articles into 5 categories (business, entertainment, politics, sport, technology) with **97% accuracy** using traditional NLP techniques.

## Technical Stack
- **Text Processing**: NLTK (lemmatization, stopwords)
- **Feature Extraction**: TF-IDF with bigrams
- **Model**: Multinomial Naive Bayes
- **Evaluation**: Precision/Recall, Confusion Matrix

## Dataset
The [BBC News Dataset](http://mlg.ucd.ie/datasets/bbc.html) from University College Dublin contains:
- 2,225 articles (2004-2005)
- 5 balanced categories
- Raw text format

**Preprocessing Applied**:
- Removed 266 duplicate articles
- Standardized text (lowercase, special chars removal)
- Train-test split (80/20 stratified)

##  Results
| Metric        | Score |
|---------------|-------|
| Accuracy      | 97%   |
| F1-Score      | 0.97  |
