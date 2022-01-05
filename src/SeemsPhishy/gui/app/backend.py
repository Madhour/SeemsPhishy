#from src.SeemsPhishy.utils import set_logger
from SeemsPhishy.utils import set_logger
import sqlalchemy
import pandas as pd
#from src.SeemsPhishy.dataretrieval.enumeration import Enumeration
from SeemsPhishy.dataretrieval.enumeration import Enumeration
#from src.SeemsPhishy.dataretrieval.ocr import TextParser
from SeemsPhishy.dataretrieval.ocr import TextParser
import SeemsPhishy.nlp as nlp


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

    def get_keywords(self, entity_id):
        s_query = f"""
        SELECT d.s_title, k.s_keyword, k.s_tag, k.n_no_occurcances
        FROM keywords k
        INNER JOIN datafiles d on k.n_file_id = d.n_file_id
        INNER JOIN searchedentities s on s.n_entity_id = d.n_entity_id
        WHERE s.n_entity_id = {int(entity_id)}
                        """
        df = pd.read_sql_query(s_query, self.alchemy_connection)
        return df

    ################################################################################

    def new_entity(self, form_infos):
        self.log.info(f"Add new entity")
        self.log.debug(f"Form: {form_infos}")
        
        # async call_data_retrieval(form_infos, db_connection)       # no return, # db status change define in funct
        company_enum = Enumeration(form_infos.organization) # Input: organization name, amount of pages to query (to be implemented)
        results = company_enum.getFiles()
        corpus = TextParser(results).convertFiles() # extracts text from PDFs
        print(corpus)
        
                
        # store data in db
            # DB-query
            
        return True

    async def exec_information_gain(self, form_infos):
        self.log.info(f"Execute Information Gain Process")
        self.log.debug(f"Form: {form_infos}")

        texte = ("Just for future viewers: apparently the function get_feature_namest() for the vectorizer is now deprecated; when version 1.2 of sklearn is released the function will be completely removed (thus breaking the code in this video). The new standard function to use is to change the line to: vectorizer.get_feature_names_out(). In my (albeit limited) set of tests, I received no different results using either function.", "Thanks for a really nice tutorial! I was wondering if this Tf Idf technique would be useful for a corpus of tweets? I can see in the video that a single document in your corpus is fairly long and it makes sense when you extract key terms from it. How would it work with a tweet as a single document which is 280 characters max? Thank you!", "For example, if I am looking at medical journals and come across something like non small cell lung cancer, this whole phrase has a very specific meaning/importance. Is there a way to look for and classify phrases like this? rather than breaking it up into ['non', 'small', 'cell', 'lung', 'cancer']  which could result in each word ending up in a different cluster which won't return much logical value?", "Hi, thanks for this, such a great video. I do have a question though. When trying to make the tf-idf vectorizer using my own cleaned corpus I'm getting the error 'AttributeError: 'list' object has no attribute 'lower''. I know this is because i am feeding it a list of lists. I thought it was important that I fed the model a list of lists (where each sub-list is a document) given that tf-idf takes into account individual documents in a whole corpus. of course I could solve this by changing the input, but as I said I thought that it was important that the corpus has within it individual documents (i.e., lists within the list). any idea on how to go about this? Thanks!", "Any chance that you show an application that pulls data from a csv? I'm trying to follow your tutorial with my own data, but I rarely have data in JSON and I'm failing to get my data in a form that allow me to follow your work. (I'm too indoctrinated in pandas and tidyverse)", "I guess my question wont be any relevant (because the video is 10 months old) but i'd be very happy if anyone could explanin why there are string values in our feature_names list that contain multiple strings. For example: anc supporter shot, political conflict area etc. ... I always thought TFIDF only works with singular words...", "Krass wie Niklas sich auskennt in der Wildnis, da kann man einiges lernen. Auch seine schönen Worte darüber dass man die schönen Momente im Leben geniessen soll. Wie Familie & Freunde wichtiger sind als jede Minute am Handy. Wahre Worte von einem wahren Überlebenskünstler. Hut ab! Sehr spannende Folge :))", "Was sich hier deutlich zeigt: Das Wichtigste in so einer outdoor survival Situation ist nicht Jagen oder Angeln, sondern einfach Wissen darüber, welche Pflanzen und Pilze essbar sind und welche nicht. Niklas hatte einfach an Tag 1 schon eine bessere Mahlzeit als irgendein anderer Teilnehmer in der gesamten Woche.", "TOP - so schön Niklas Variante gesehen zu haben. Irgendwie hat er es recht gelassen gemacht! Er hat mehr gegessen als alle anderen gemeinsam. Und die Schwitzhütte - TOP!", "Schön, dass ihr Niklas nicht einfach abgeschrieben habt nach dem Motto Tolle Folge, er passt wirklich gut dazu. Jetzt ne Folge 7 Days of Dave. Fertignahrung und exzessiver Social Media Konsum!", "Die Serie begann langsam etwas langweilig zu werden, die Sonderfolge war wichtig! Richtig stark, geiler typ, gutes Schnitttempo und endlich mal paar survival skills außer rumliegen und Beeren essen", "Have a good end of 2021 y’all! This year was actually going pretty good for me up until the later part of it, and these videos were a little bright part of my day. Thanks :3", "Thanks for putting a large amount of your time just to make us smile, and that’s definitely what these videos do! Keep up your great work and Merry Christmas!", "I'm 44 years old guy and I simply love Daily Dose Of Internet. It makes me happier everytime I watch the new video and helps me to forget everyday miseries of life :-) Keep up in a good work. I wish you all the best!", "As someone who was chased by this particular rooster so much as a kid we ended up having to shoot it, they are actually terrifying and vicious beasts", "Some days this channel is the only reason i smile. Thank you for your dedication and continued uploading during these times. Merry chrismas and happy new year!")


        
        nlp.main(texte, stop_word_remov=True, stemming_lemma='l', keyword=form_infos["keywords"], ner=form_infos["ner"], tf_idf=form_infos["tf_idf"])
        
        # Function(model_choice, text)
        # async call_data_keywords(form_infos, db_conncection)       # no return, # db status change define in funct
        return True

    def generate_text(self, form_infos):
        # User chooses keywords
        self.log.info(f"Execute Textgeneration")
        self.log.debug(f"Form: {form_infos}")

        # if type == "mail":
        # async generate_mail(form_infos, db_conncection)       # no return, # db status change define in funct
        return True # return rendered newsletter template

    ################################################################################

if __name__ == "__main__":
    backend = Backend()
    backend.connect()
    backend.call_data_retrieval({"organization":"Protiviti GmbH"})
    # backend.test()
    # backend.list_companies()
    # backend.get_dashboard_donut_data()
    backend.get_entity_names()
