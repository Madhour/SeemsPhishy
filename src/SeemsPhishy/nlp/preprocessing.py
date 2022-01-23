from nltk.stem import PorterStemmer
import pandas as pd

# function for pre-processing with spacy
def pipe_preprocessing(text, s_w_r, pref_operation, nlp_model):
    contents = text
    corpus = contents
    doc = nlp_model(corpus)

    p = PorterStemmer()

    # creating lists for the dataframe
    text_df = []
    lemma_df = []
    pos_df = []
    tag_df = []
    dep_df = []
    shape_df = []
    stop_df = []
    corp_stem = []
    stemm_list = []

    for token in doc:
        text_df.append(token.text)
        lemma_df.append(token.lemma_)
        pos_df.append(token.pos_)
        tag_df.append(token.tag_)
        dep_df.append(token.dep_)
        shape_df.append(token.shape_)
        stop_df.append(token.is_stop)

    for token in doc:
        corp_stem.append(token.text)
        p = PorterStemmer()
    for w in corp_stem:
        stemm_list.append(p.stem(w))

    #creating the dataframe
    data = {'Text': text_df, 'Lemma': lemma_df, 'Stemm': stemm_list, 'POS': pos_df, 'TAG': tag_df, 'DEP': dep_df,
            'SHAPE': shape_df, 'STOP': stop_df}
    df = pd.DataFrame(data)

    # ______________________________________________________________________________
    # Some General Removal of all \n, points(.) commas(,) etc., so that mostly words are left
    # ______________________________________________________________________________
    df = df[df.POS != 'SPACE']
    df = df[df.POS != 'PUNCT']
    df = df[df.DEP != 'punct']
    df = df[df.Text != '•']
    df = df[df.Text != '©']
    df = df[df.Text != '®']

    # ______________________________________________________________________________
    # Stop Word Removal (Default = True)
    # ______________________________________________________________________________
    if s_w_r is True:
        df = df[df.STOP == False]

    # ______________________________________________________________________________
    # Lemma or Stemming
    # ______________________________________________________________________________
    if pref_operation == 'l':
        lemm_list = df.Lemma.to_list()
        lemma_txt = ' '.join(lemm_list)
        return lemma_txt

    if pref_operation == 's':
        stemm_list = df.Stemm.to_list()
        stemm_txt = ' '.join(stemm_list)
        return stemm_txt
