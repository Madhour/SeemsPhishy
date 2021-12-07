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
        no_file = pd.read_sql_query("SELECT count(n_file_id), count(distinct n_entity_id) FROM datafiles", self.alchemy_connection).values[0]
        no_keywords = pd.read_sql_query("SELECT count(n_keyword_id), count(distinct n_file_id) FROM keywords", self.alchemy_connection).values[0]
        no_texts = pd.read_sql_query("SELECT count(n_entity_id), count(distinct n_entity_id) FROM textsgen", self.alchemy_connection).values[0]
        return no_file, no_keywords, no_texts

    def list_companies(self):
        df = pd.read_sql_query("SELECT s_name AS Company, n_status AS status FROM SearchedEntities", self.alchemy_connection)
        return df

    def list_files(self):
        s_query = """
        SELECT searchedentities.s_name as company, datafiles.s_title as filename, datafiles.n_status as status
        FROM datafiles INNER JOIN searchedentities ON  datafiles.n_entity_id = searchedentities.n_entity_id
        
        """
        df = pd.read_sql_query(s_query, self.alchemy_connection)
        return df


if __name__ == "__main__":
    backend = Backend()
    backend.connect()
    backend.test()
    backend.list_companies()
