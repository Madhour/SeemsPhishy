import spacy
import yake
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import string
from nltk.corpus import stopwords
import json
import glob
import re
from sklearn.feature_extraction.text import TfidfTransformer
from sqlalchemy import text

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline



def named_entity_recoc(text1):
    print(text1)
    nlp = spacy.load("en_core_web_lg") 
    doc = nlp(text1)
    print(doc.ents)

    return doc.ents

        #for token in doc.ents:
            #print(token.text, token.label_)



def sklearn_tf_idf(conn, key, dataset):
    tfIdfVectorizer=TfidfVectorizer(use_idf=True)
    tfIdf = tfIdfVectorizer.fit_transform(dataset)
    df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
    df = df.sort_values('TF-IDF', ascending=False)

    output_old = df.head(25)
    output = output_old.index.tolist()

    for keyword in output:
        query_entity = f"INSERT INTO Keywords (n_file_id, s_keyword, s_tag) VALUES ({key}, '{keyword}', 'TFIDF');"
        sql_query_df = text(query_entity)
        conn.execute(sql_query_df)

    print(output)
    return output




def keywords_yake(text, language = "en", max_ngram_size = 3, deduplication_threshold = 0.9, numOfKeywords = 1):
    #kw_extractor = yake.KeywordExtractor()

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(text)
    return keywords
    #for kw in keywords:
    #    print(kw)

def ner_bert(text):
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    ner_results = nlp(text)
    return ner_results
    #print(ner_results)

