
text = "This is an example text. It's purpose is to test this programm."

def pipe_preprocessing(s_w_r, pref_operation):

    #notwendigen Module
    import spacy
    from nltk.stem import PorterStemmer
    import pandas as pd
    from nltk.stem import PorterStemmer





    #Textdatei öffnen und einlesen
    #with open(textdatei,encoding="utf8") as f:
    contents = text
    corpus = contents
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(corpus)


    #Textdatei in einen pd Dataframe umwandeln
    p = PorterStemmer()

    text_df = []
    lemma_df = []
    stemm_df = []
    pos_df = []
    tag_df = []
    dep_df = []
    shape_df = []
    stop_df = []



    for token in doc:
        text_df.append(token.text)
        lemma_df.append(token.lemma_)
        pos_df.append(token.pos_)
        tag_df.append(token.tag_)
        dep_df.append(token.dep_)
        shape_df.append(token.shape_)
        stop_df.append(token.is_stop)

        #extrawurst für das Stemming
        corp_stem = []
    for token in doc:
        corp_stem.append(token.text)
        #Liste in der Text gestemmt wurde
        stemm_list = []
        p = PorterStemmer()
    for w in corp_stem:
        stemm_list.append(p.stem(w))


        data = {'Text':text_df, 'Lemma':lemma_df,'Stemm':stemm_list, 'POS':pos_df, 'TAG':tag_df,'DEP':dep_df, 'SHAPE':shape_df, 'STOP':stop_df }
        df = pd.DataFrame(data)


    #______________________________________________________________________________
    #Some General Removements
    #Removal of all \n, points(.) commas(,) etc., so that mostly words are left
    #______________________________________________________________________________
    df = df[df.POS != 'SPACE'] #entfernt alle \ o.ä. aus dem df
    df = df[df.POS != 'PUNCT'] #entfernt alle . und , aus dem df
    df = df[df.DEP != 'punct']#entfernt weitere Punktanreihungen
    df = df[df.Text != '•'] #entfernt alle Bullet points aufzähler aus dem df
    df = df[df.Text != '©'] #entfernt dieses Sonderzeichen aus dem Text
    df = df[df.Text != '®'] #entfernt dieses Sonderzeichen aus dem Text



    #______________________________________________________________________________
    #Stop Word Removal (Default = True)
    #______________________________________________________________________________
    if s_w_r == True:
        df = df[df.STOP == False] #behält alle einträge im df wo Stop != True, also welche keine Stop-Words sind
        print('Es wurde alle Stopwords entfernt. Dies Länge des Datenframes beträgt:', len(df))
        print('_____________________________________________________________________')




    if s_w_r == False:
        print('No stop word removal')
        print('_____________________________________________________________________')




    #______________________________________________________________________________
    #Lemmatisierung oder Stemming
    #______________________________________________________________________________
    if pref_operation == 'l':
        lemm_list = df.Lemma.to_list()
        lemma_txt = ' '.join(lemm_list)
        print(lemma_txt)



    if pref_operation == 's':
        stemm_list = df.Stemm.to_list()
        stemm_txt = ' '.join(stemm_list)
        print(stemm_txt)


