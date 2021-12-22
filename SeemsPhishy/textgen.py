from transformers import pipeline
from jinja2 import *
import time

def generate(input_text):
    #generator1 = pipeline('text-generation', model='gpt2')
    generator2 = pipeline('text-generation', model='distilgpt2') 
    #generator1 = pipeline('text-generation', model='gpt2')

    #output_text_1 = generator1(input_text, min_length=30, num_return_sequences=1)
    output_text_2 = generator2(input_text, min_length=30, num_return_sequences=3)
    
    return output_text_2

def buildMail(text, organization):
    report_number = int(time.time())
    organization = ""
   

    template = Template(open('SeemsPhishy/templates/phishing_tpl.html').read()) # HTML Template stored inside /lib/
    tpl = template.render(newsletter = text, report_number = report_number)
    html = open(f'./SeemsPhishy/newsletters/Newsletter-{organization}-{report_number}.html', 'w') #stores rendered report as HTML file
    html.write(tpl)
    html.close()