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

        s_connect_string = f'postgresql://{self.s_db_user}:{self.s_db_pwd}@{self.s_db_host}:{self.s_db_port}/{self.s_db_database}'

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
        df = pd.read_sql_query('SELECT * FROM SearchedEntities', self.alchemy_connection)
        print(df)


if __name__ == "__main__":
    backend = Backend()
    backend.connect()
    backend.test()
