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
<<<<<<< HEAD
from sqlalchemy import text
=======
>>>>>>> ea8345e6ab4ffd8f1461f76bdacc92f308c38f96

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline



<<<<<<< HEAD
def named_entity_recoc(text1):
    print(text1)
    nlp = spacy.load("en_core_web_lg") 
    doc = nlp(text1)
    print(doc.ents)
=======


def named_entity_recoc(text, nlp):
        doc = nlp(text)
>>>>>>> ea8345e6ab4ffd8f1461f76bdacc92f308c38f96

    return doc.ents

        #for token in doc.ents:
            #print(token.text, token.label_)



<<<<<<< HEAD
def sklearn_tf_idf(conn, key, dataset):
=======
#def tf_idf(texte):

#    def load_data(file):
#        with open (file, "r", encoding="utf-8") as f:
#            data = json.load(f)
#        return (data)
#
#    def write_data(file, data):
#        with open (file, "w", encoding="utf-8") as f:
#            json.dump(data, f, indent=4)
#
#    def remove_stops(text, stops):
#        text = re.sub(r"AC\/\d{1,4}\/\d{1,4}", "", text)
#        words = text.split()
#        final = []
#        for word in words:
#            if word not in stops:
#                final.append(word)
#        final = " ".join(final)
#        final = final.translate(str.maketrans("", "", string.punctuation))
#        final = "".join([i for i in final if not i.isdigit()])
#        while "  " in final:
#            final = final.replace("  ", " ")
#        return (final)
#
#    def clean_docs(docs):
#        stops = stopwords.words("english")
#        months = load_data("data/months.json")
#        stops = stops+months
#        final = []
#        for doc in docs:
#            clean_doc = remove_stops(doc, stops)
#            final.append(clean_doc)
#        return (final)
#
#    descriptions = load_data("data/trc_dn.json")["descriptions"]
#    names = load_data("data/trc_dn.json")["names"]
#
#    # print (descriptions[0])
#
#    cleaned_docs = clean_docs(texte)
#    # print (cleaned_docs[0])
#
#    vectorizer = TfidfVectorizer(
#                                    lowercase=True,
#                                    max_features=100,
#                                    max_df=0.8,
#                                    min_df=5,
#                                    ngram_range = (1,3),
#                                    stop_words = "english"
#
#                                )
#
#    vectors = vectorizer.fit_transform(texte)
#
#    feature_names = vectorizer.get_feature_names()
#
#    dense = vectors.todense()
#    denselist = dense.tolist()
#
#    all_keywords = []
#
#    for description in denselist:
#        x=0
#        keywords = []
#        for word in description:
#            if word > 0:
#                keywords.append(feature_names[x])
#            x=x+1
#        all_keywords.append(keywords)
##    print (descriptions[0])
#    print (all_keywords[0])
#
#    true_k = 1
#
#    model = KMeans(n_clusters=true_k, init="k-means++", max_iter=100, n_init=1)
#
#    model.fit(vectors)
#
#    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
#    terms = vectorizer.get_feature_names()
#
#    for i in range(true_k):
#                print(f"Cluster {i}")
#                print("\n")
#                for ind in order_centroids[i, :10]:
#                    print(' %s' % terms[ind],)
#                    print("\n")
#                print("\n")
#                print("\n")
#    
#
#    with open ("trc_results.txt", "w", encoding="utf-8") as f:
#        for i in range(true_k):
#            f.write(f"Cluster {i}")
#            f.write("\n")
#            for ind in order_centroids[i, :10]:
#                f.write (' %s' % terms[ind],)
#                f.write("\n")
#            f.write("\n")
#            f.write("\n")


def sklearn_tf_idf(dataset):
>>>>>>> ea8345e6ab4ffd8f1461f76bdacc92f308c38f96
    tfIdfVectorizer=TfidfVectorizer(use_idf=True)
    tfIdf = tfIdfVectorizer.fit_transform(dataset)
    df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
    df = df.sort_values('TF-IDF', ascending=False)
<<<<<<< HEAD
=======
    return df.head(25)

>>>>>>> ea8345e6ab4ffd8f1461f76bdacc92f308c38f96

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

<<<<<<< HEAD
=======

>>>>>>> ea8345e6ab4ffd8f1461f76bdacc92f308c38f96
def ner_bert(text):
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    ner_results = nlp(text)
    return ner_results
    #print(ner_results)

