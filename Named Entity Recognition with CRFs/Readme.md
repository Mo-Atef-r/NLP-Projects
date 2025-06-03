# Named Entity Recognition with Conditional Random Fields (CRF)

This project implements a Named Entity Recognition (NER) system using Conditional Random Fields (CRF) on the CoNLL-2003 dataset. The model achieves strong performance while demonstrating the challenges of NER and some inherent limitations in the dataset itself.

## Features

- CRF model with carefully tuned hyperparameters
- Comprehensive feature engineering including:
  - Word-level features (case, suffixes, etc.)
  - Part-of-Speech (POS) tags
  - Chunk tags
  - Contextual features (previous/next words and tags)
- Detailed error analysis

## Dataset

The project uses the **CoNLL-2003** dataset for Named Entity Recognition:

**Citation:**  
Sang, E. F., & De Meulder, F. (2003). *Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition.* In Proceedings of the Seventh Conference on Natural Language Learning (CoNLL-2003) (pp. 142–147).  

**Dataset Link:** [https://www.clips.uantwerpen.be/conll2003/ner/](https://www.clips.uantwerpen.be/conll2003/ner/)  

The dataset includes four entity types with BIO tagging:
- **PER** (Person)  
- **ORG** (Organization)  
- **LOC** (Location)  
- **MISC** (Miscellaneous)
