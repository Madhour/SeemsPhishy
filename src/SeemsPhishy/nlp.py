import spacy
from spacy.tokens import Doc

nlp = spacy.load("en_core_web_lg")

text = """spaCy is an open-source software library for advanced natural language processing, 
written in the programming languages Python and Cython. The library is published under the MIT license
and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""
doc = nlp(text)   

print(doc.ents)   

#python -m spacy download en_core_web_sm (muss vor Ausführung installiert werden)
