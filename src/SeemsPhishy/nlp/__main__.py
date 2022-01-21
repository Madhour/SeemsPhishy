from SeemsPhishy.nlp.preprocessing import pipe_preprocessing
from SeemsPhishy.nlp.information_gain import sklearn_tf_idf
from SeemsPhishy.nlp.information_gain import named_entity_recoc
from SeemsPhishy.nlp.information_gain import keywords_yake
from SeemsPhishy.utils import set_logger
import sqlalchemy
import spacy

log = set_logger("NLP", mode="debug")


def main(conn, texts, stop_word_removal=True, stemming_lemma='l', keyword=True, ner=True, tf_idf=True):

    pre_texts = []
    tf_idf_words = []
    entities = []
    keywords = []

    if ner is True:
        for key, text1 in texts.items():
            current_entities = named_entity_recoc(text1)
            entities.append(current_entities)
            for element in current_entities:
                query_entity = f"INSERT INTO Keywords (n_file_id, s_keyword, s_tag) VALUES ({key}, '{element[0]}', 'NER');"
                sql_query_df = sqlalchemy.text(query_entity)
                conn.execute(sql_query_df)

    for key2, text2 in texts.items():
        nlp_model = spacy.load("en_core_web_lg")
        pre_text = str(pipe_preprocessing(text2, stop_word_removal, stemming_lemma, nlp_model))
        pre_texts.append(pre_text)

    if tf_idf is True:
        key_new = list(texts.keys())
        print(key_new)
        sklearn_tf_idf(conn, key_new[0], pre_texts)

    if keyword is True:
        key_new = list(texts.keys())
        for text3 in pre_texts:
            current_keywords = keywords_yake(text3)
            keywords.append(current_keywords)
            for element in current_keywords:
                query_entity = f"INSERT INTO Keywords (n_file_id, s_keyword, s_tag) VALUES ({key_new[0]}, '{element[0]}', 'KEYWORDS');"
                sql_query_df = sqlalchemy.text(query_entity)
                conn.execute(sql_query_df)
                print(element[0])

    log.debug(entities)
    log.debug(keywords)

    return keywords, pre_texts, entities






