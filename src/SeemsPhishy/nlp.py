import spacy
from spacy.tokens import Doc

doc = nlp.make_doc("This is a sentence")
for name, proc in nlp.pipeline:          
    doc = proc(doc)        