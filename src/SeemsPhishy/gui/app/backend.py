#from src.SeemsPhishy.utils import set_logger
from SeemsPhishy.utils import set_logger
import sqlalchemy
from sqlalchemy import text
import pandas as pd
#from src.SeemsPhishy.dataretrieval.enumeration import Enumeration
from SeemsPhishy.dataretrieval.enumeration import Enumeration
#from src.SeemsPhishy.dataretrieval.ocr import TextParser
from SeemsPhishy.dataretrieval.ocr import TextParser
<<<<<<< HEAD
import SeemsPhishy.nlp.__main__ as nlp
import time, datetime
=======
import SeemsPhishy.nlp.__main__ as __main__
>>>>>>> ea8345e6ab4ffd8f1461f76bdacc92f308c38f96


class Backend:
    def __init__(self, mode="debug"):
        self.s_db_pwd = 1234
        self.s_db_port = 5433
        self.s_db_user = "postgres"
        self.s_db_database = "postgres"
        self.s_db_host = "localhost"
        self.debug_level = mode

        self.log = set_logger("Seems-Phishy", mode=mode)

        self.alchemy_engine = None
        self.alchemy_connection = None

    def connect(self):
        self.log.info("Connect to database")

        s_connect_string = f"postgresql://{self.s_db_user}:{self.s_db_pwd}@{self.s_db_host}:{self.s_db_port}/{self.s_db_database}"

        self.log.debug(f"connect string:{s_connect_string}")

        self.alchemy_engine = sqlalchemy.create_engine(s_connect_string)
        self.alchemy_connection = self.alchemy_engine.connect()
        return True

    def test(self):
        """
        tests the connection to the db.

        :return:
        """
        # checks if data / tables are present if it fails it initialises the database
        df = pd.read_sql_query("SELECT * FROM SearchedEntities", self.alchemy_connection)
        print(df)

    def get_dashboard_infos(self):
        no_file = pd.read_sql_query("SELECT count(n_file_id), count(distinct n_entity_id) FROM datafiles",
                                    self.alchemy_connection).values[0]
        no_keywords = pd.read_sql_query("SELECT count(n_keyword_id), count(distinct n_file_id) FROM keywords",
                                        self.alchemy_connection).values[0]
        no_texts = pd.read_sql_query("SELECT count(n_entity_id), count(distinct n_entity_id) FROM textsgen",
                                     self.alchemy_connection).values[0]
        return no_file, no_keywords, no_texts

    def list_entities(self):
        # s_query = """
        # SELECT s.s_name AS entity, s.n_status AS status, 
        # b_ner as NER, b_tfidf as tfidf, b_word2vec as yake_keywords,
        # count(distinct d.n_file_id) as files, count(distinct k.s_keyword) as keywords
        # FROM SearchedEntities s 
        #     INNER JOIN datafiles d on S.n_entity_id = d.n_entity_id
        #     INNER JOIN keywords k on d.n_file_id = k.n_file_id
        # GROUP BY s.s_name, S.n_status, b_ner, b_tfidf, b_word2vec
        # """

        s_query = """
        SELECT s.s_name AS entity, s.n_status AS status, 
        b_ner as NER, b_tfidf as tfidf, b_word2vec as yake_keywords, count(distinct d.n_file_id) as files
        FROM SearchedEntities s 
            INNER JOIN datafiles d on S.n_entity_id = d.n_entity_id
        GROUP BY s.s_name, s.n_status, b_ner, b_tfidf, b_word2vec
        """
        df = pd.read_sql_query(s_query, self.alchemy_connection)
        return df

    def list_files(self):
        s_query = """
        SELECT searchedentities.s_name as entity, datafiles.s_title as title, datafiles.n_status as status, datafiles.s_path as url
        FROM datafiles INNER JOIN searchedentities ON  datafiles.n_entity_id = searchedentities.n_entity_id
        
        """
        df = pd.read_sql_query(s_query, self.alchemy_connection)
        return df

    def list_leakage_files(self):
        s_query = """
        SELECT searchedentities.s_name as entity, datafiles.s_title as title, datafiles.n_status as status, datafiles.s_path as url
        FROM datafiles INNER JOIN searchedentities ON  datafiles.n_entity_id = searchedentities.n_entity_id
        WHERE datafiles.b_leakage_warn = true
        """
        df = pd.read_sql_query(s_query, self.alchemy_connection)
        return df

    def get_dashboard_donut_data(self, split=2):
        s_query = "SELECT * FROM keywords"
        df = pd.read_sql_query(s_query, self.alchemy_connection)
        print(df)
        df = df.groupby("s_keyword").sum(["n_no_occurancies"]).sort_values(["n_no_occurancies"], ascending=False)
        df_top = df[:split]
        rest = df[split:]["n_no_occurancies"].sum()
        if rest is None:
            rest = 0

        labels = df_top.index.to_list()
        labels.append("others")
        data = df_top.n_no_occurancies.to_list()
        data.append(rest)
        return labels, data

    def get_entity_names(self):
        s_query = """
                SELECT s_name as entity, n_entity_id as id
                FROM searchedentities
                """
        df = pd.read_sql_query(s_query, self.alchemy_connection)
        return df

    def get_keywords(self, entity_id):
        s_query = f"""
        SELECT d.s_title, k.s_keyword, k.s_tag, k.n_no_occurancies
        FROM keywords k
        INNER JOIN datafiles d on k.n_file_id = d.n_file_id
        INNER JOIN searchedentities s on s.n_entity_id = d.n_entity_id
        WHERE s.n_entity_id = {int(entity_id)}
                        """
        df = pd.read_sql_query(s_query, self.alchemy_connection)
        return df

    def get_keywords_textgen(self, entity_id, ner, tf_idf, keywords):
        tag_list = []
        if ner:
            tag_list.append("NER")
        else:
            tag_list.append("None")
        if tf_idf:
            tag_list.append("TFIDF")
        else:
            tag_list.append("None")
        if keywords:
            tag_list.append("KEYWORDS")
        else:
            tag_list.append("None")

        s_query = f"""
        SELECT k.s_keyword, k.n_keyword_id
        FROM keywords k
        INNER JOIN datafiles d on k.n_file_id = d.n_file_id
        INNER JOIN searchedentities s on s.n_entity_id = d.n_entity_id
        WHERE s.n_entity_id = {int(entity_id)} AND k.s_tag IN ('{tag_list[0]}','{tag_list[1]}','{tag_list[2]}')
                        """
        df = pd.read_sql_query(s_query, self.alchemy_connection)
        return df

    ################################################################################

    def delete_db_entry(self, table, attribute, id):
        query = f"DELETE FROM {table} WHERE {attribute} = {id};"
        sql_query = text(query)
        self.alchemy_connection.execute(sql_query)
        return True

    def get_table(self, table_name):
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, self.alchemy_connection)
        return df
    
    def new_entity(self, form_infos):
        self.log.info(f"Add new entity")
        self.log.debug(f"Form: {form_infos}")

        self.delete_db_entry("SearchedEntities", "n_entity_id", 52)
        self.delete_db_entry("SearchedEntities", "n_entity_id", 53)


        n_status = 1
        s_name = form_infos["custom_name"]
        s_query = form_infos["search_term"]
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        b_tfidf = form_infos["tf_idf"]
        b_wordvec = form_infos["keywords"]  # diese Params rausnehmen --> bei new immer nur retrieval + ocr und dann separat bei IG die Verfahren wählen
        b_ner = form_infos["ner"]

        query = f"INSERT INTO SearchedEntities (n_status, s_name, s_query, ts_searched, b_tfidf, b_word2vec, b_ner) VALUES ({n_status}, '{s_name}', '{s_query}', '{timestamp}', {b_tfidf}, {b_wordvec}, {b_ner});"
        sql_query = text(query)
        self.alchemy_connection.execute(sql_query)
        
        
        company_enum = Enumeration(form_infos["search_term"]) 
        results = company_enum.getFiles() #if files found = 0: Auf GUI anzeigen, dass nochmal Start gedrückt werden muss

        if results:
            print("Dictionary is not empty!")
        else:
            print("Dictionary is empty!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("TRY AGAIN WITH ANOTHER ENTITY NAME")

        corpus = TextParser(results).convertFiles(form_infos["number_of_results"])
        
        query_2 = f"SELECT n_entity_id FROM SearchedEntities WHERE s_name = '{s_name}';"
        entity_id = pd.read_sql_query(query_2, self.alchemy_connection)
        n_entity_id = entity_id.loc([0][0])
        print(n_entity_id)
        
        for key in corpus:
            new_key = str(key).replace("'","")
            print(key)
            print(new_key)
            current_timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            query_df = f"INSERT INTO DataFiles (n_entity_id, n_status, s_path, s_title, s_text, ts_created) VALUES ({n_entity_id[0][0]}, {n_status}, '{results[str(key)]}', '{new_key}', '{corpus[str(key)]}', '{current_timestamp}');"
            sql_query_df = text(query_df)
            self.alchemy_connection.execute(sql_query_df)

        a = self.get_table("SearchedEntities")
        print(a)
        b = self.get_table("DataFiles")
        print(b)

        if form_infos["ner"] is True or form_infos["tf_idf"] is True or form_infos["keywords"] is True:
            self.exec_information_gain(form_infos)
            
        return True

    #async def exec_information_gain(self, form_infos):
    def exec_information_gain(self, form_infos):
        self.log.info(f"Execute Information Gain Process")
        self.log.debug(f"Form: {form_infos}")

        if "entity_id" in form_infos:
            n_entity_id = form_infos["entity_id"]
        else:
            s_name = form_infos["custom_name"]
            query_2 = f"SELECT n_entity_id FROM SearchedEntities WHERE s_name = '{s_name}';"
            entity_id = pd.read_sql_query(query_2, self.alchemy_connection)
            n_entity_id = entity_id.loc([0][0])
            print(n_entity_id)
            print(n_entity_id[0][0])
        

        query_texts = f"SELECT s_text,n_file_id FROM DataFiles WHERE n_entity_id = '{n_entity_id[0][0]}';"
        texts = pd.read_sql_query(query_texts, self.alchemy_connection)

        texts_dict = {}

        for index, row in texts.iterrows():
            texts_dict[row["n_file_id"]] = row["s_text"]
        
<<<<<<< HEAD
        nlp.main(self.alchemy_connection, texts_dict, stop_word_remov=form_infos["stop_words"], stemming_lemma=form_infos["lemma_stemm"], keyword=form_infos["keywords"], ner=form_infos["ner"], tf_idf=form_infos["tf_idf"]) # keyword Parameter noch mit GUI anpassen

        print(self.get_table("Keywords"))

=======
        __main__.main(texte, stop_word_remov=True, stemming_lemma='l', keyword=form_infos["keywords"], ner=form_infos["ner"], tf_idf_tf=form_infos["tf_idf"])
        
        # Function(model_choice, text)
        # async call_data_keywords(form_infos, db_conncection)       # no return, # db status change define in funct
>>>>>>> ea8345e6ab4ffd8f1461f76bdacc92f308c38f96
        return True

    def generate_text(self, form_infos, keyword_infos):
        # User chooses keywords
        self.log.info(f"Execute Textgeneration")
        self.log.debug(f"Form: {form_infos}")
        self.log.debug(f"Form: {keyword_infos}")

        print("TEXT GEN FORM:")
        n_entity_id = form_infos["entity_id"]

        query_keywords = f"SELECT s_keyword FROM Keywords JOIN DataFiles ON Keywords.n_file_id = DataFiles.n_file_id JOIN SearchedEntities ON DataFiles.n_entity_id = SearchedEntities.n_entity_id WHERE SearchedEntities.s_name = '{n_entity_id}';"
        keywords_df = pd.read_sql_query(query_keywords, self.alchemy_connection)

        print(keywords_df)

        # if type == "mail":
        # async generate_mail(form_infos, db_conncection)       # no return, # db status change define in funct
        return "Lukas stinkt" # return rendered newsletter template

    ################################################################################

if __name__ == "__main__":
    backend = Backend()
    backend.connect()
    # backend.call_data_retrieval({"organization":"Protiviti GmbH"})
    # backend.test()
    # backend.list_companies()
    # backend.get_dashboard_donut_data()
    backend.get_entity_names()
