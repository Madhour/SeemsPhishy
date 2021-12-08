from src.SeemsPhishy.utils import set_logger
import sqlalchemy
import pandas as pd


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
        s_query = """
        SELECT s.s_name AS entity, s.n_status AS status, 
        b_ner as NER, b_tfidf as tfidf, b_word2vec as word2vec,
        count(d.n_file_id) as files, count(distinct k.s_keyword) as keywords
        FROM SearchedEntities s 
            INNER JOIN datafiles d on S.n_entity_id = d.n_entity_id
            INNER JOIN keywords k on d.n_file_id = k.n_file_id
        GROUP BY s.s_name, S.n_status, b_ner, b_tfidf, b_word2vec
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

    def get_dashboard_donut_data(self, split=2):
        s_query = "SELECT * FROM keywords"
        df = pd.read_sql_query(s_query, self.alchemy_connection)

        df = df.groupby("s_keyword").sum(["n_no_occurcances"]).sort_values(["n_no_occurcances"], ascending=False)
        df_top = df[:split]
        rest = df[split:]["n_no_occurcances"].sum()
        if rest is None:
            rest = 0

        labels = df_top.index.to_list()
        labels.append("others")
        data = df_top.n_no_occurcances.to_list()
        data.append(rest)
        return labels, data

    def get_entity_names(self):
        s_query = """
                SELECT s_name as entity, n_entity_id as id
                FROM searchedentities
                """
        df = pd.read_sql_query(s_query, self.alchemy_connection)
        return df

    ################################################################################

    def new_entity(self, form_infos):
        self.log.info(f"Add new entity")
        self.log.debug(f"Form: {form_infos}")

        # async call_data_retrival(form_infos, db_conncection)       # no return, # db status change define in funct
        return True

    def exec_information_gain(self, form_infos):
        self.log.info(f"Execute Information Gain Process")
        self.log.debug(f"Form: {form_infos}")

        # async call_data_keywords(form_infos, db_conncection)       # no return, # db status change define in funct
        return True


if __name__ == "__main__":
    backend = Backend()
    backend.connect()
    # backend.test()
    # backend.list_companies()
    # backend.get_dashboard_donut_data()
    backend.get_entity_names()
