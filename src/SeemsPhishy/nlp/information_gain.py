import sqlalchemy
import yake
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


def named_entity_recoc(text1, nlp_model):
    print(text1)
    doc = nlp_model(text1)
    print(doc.ents)
    return doc.ents


def sklearn_tf_idf(conn, key, dataset):
    tf_idf_vectorizer = TfidfVectorizer(use_idf=True)
    tf_idf = tf_idf_vectorizer.fit_transform(dataset)
    df = pd.DataFrame(tf_idf[0].T.todense(), index=tf_idf_vectorizer.get_feature_names(), columns=["TF-IDF"])
    df = df.sort_values('TF-IDF', ascending=False)

    output_old = df.head(25)
    output = output_old.index.tolist()

    for keyword in output:
        query_entity = f"INSERT INTO Keywords (n_file_id, s_keyword, s_tag) VALUES ({key}, '{keyword}', 'TFIDF');"
        sql_query_df = sqlalchemy.text(query_entity)
        conn.execute(sql_query_df)

    print(output)
    return output


def keywords_yake(texts, language="en", max_ngram_size=3, deduplication_threshold=0.9, num_of_keywords=1):
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                                top=num_of_keywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(texts)
    return keywords


def ner_bert(texts):
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    ner_results = nlp(texts)
    return ner_results
