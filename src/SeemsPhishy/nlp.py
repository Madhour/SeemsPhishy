import spacy
from spacy.tokens import Doc
import os

#gewünschte spacy Modell wird geladen (Sprache: Englisch)
#python -m spacy download en_core_web_sm (muss vor Ausführung installiert werden)
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
