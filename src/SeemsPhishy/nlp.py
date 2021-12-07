import spacy
from spacy.tokens import Doc
import os

#gewünschte spacy Modell wird geladen (Sprache: Englisch)
nlp = spacy.load("en_core_web_lg")


#alle files die im gegebenen directory liegen und mit .txt enden werden gelesen
for filename in os.listdir("C:\\Users\\Oliver.Wieder\\Jupyterlab\\NLP"):
    print("drinnen")
    if filename.endswith(".txt"): 
         # print(os.path.join(directory, filename))
        file1 = open(filename, 'r')
        Lines = file1.readlines() 

        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))
            doc = nlp(line)   
            print(doc.ents)
    else:
        print("kein txt")
        continue
'''file1 = open('examplefile.txt', 'r')
Lines = file1.readlines()

nlp = spacy.load("en_core_web_lg")

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
'''

text = """spaCy is an open-source software library for advanced natural language processing, 
written in the programming languages Python and Cython. The library is published under the MIT license
and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""
doc = nlp(text)   

print(doc.ents)   

#python -m spacy download en_core_web_sm (muss vor Ausführung installiert werden)
