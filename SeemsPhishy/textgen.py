from transformers import pipeline
from jinja2 import *
import time
import random

random_names = (
"Oskar Al-Ghazzawi",
"Adzo Snider",
"Georgios Yun",
"Askr Ogtrop",
"Winfrith McNeal",
"Sven Bieber")


def generate(input_text, num_text = 1):
    generator = pipeline('text-generation', model='gpt2') 

    output_text = generator(input_text, min_length=100, num_return_sequences=num_text)
    
    return output_text



def buildMail(text, organization):
    report_number = int(time.time())
    names = random.sample(random_names, (len(text)))

    template = Template(open('SeemsPhishy/templates/phishing_tpl.html').read()) # HTML Template stored inside /lib/
    tpl = template.render(newsletter = text, report_number = report_number, author_names = names)
    #html = open(f'./SeemsPhishy/newsletters/Newsletter-{organization}-{report_number}.html', 'w') #stores rendered report as HTML file
    html = open(f'./SeemsPhishy/newsletters/Newsletter-{organization}.html', 'w') #stores rendered report as HTML file
    html.write(tpl)
    html.close()