from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, AutoConfig, AutoModelForPreTraining
from jinja2 import *
from torch import tensor, device
import time
import random

from SeemsPhishy.gui.app.static.assets.names import random_names

SPECIAL_TOKENS = {"bos_token": "<|BOS|>",
                  "eos_token": "<|EOS|>",
                  "unk_token": "<|UNK|>",
                  "pad_token": "<|PAD|>",
                  "sep_token": "<|SEP|>"}

MAXLEN = 768


def outdated_generate(input_text, num_text=1):
    generator = pipeline('text-generation', model='Madhour/gpt2-eli5')

    output_text = generator(num_return_sequences=num_text)

    return output_text


def generate(input_text, num_text=1):
    tokenizer = AutoTokenizer.from_pretrained("Madhour/gpt2-eli5")
    model = AutoModelForCausalLM.from_pretrained("Madhour/gpt2-eli5")
    prompt = SPECIAL_TOKENS['bos_token'] + "I have a question." + SPECIAL_TOKENS['sep_token'] + input_text + \
             SPECIAL_TOKENS['sep_token']
    prompt = tensor(tokenizer.encode(prompt)).unsqueeze(0)
    text = model.generate(prompt,
                          do_sample=True,
                          min_length=50,
                          max_length=768,
                          top_k=30,
                          top_p=0.7,
                          temperature=0.9,
                          repetition_penalty=2.0,
                          num_return_sequences=3)

    len_input = len("I have a question." + input_text)
    text_dict = {}
    for text in [tokenizer.decode(a, skip_special_tokens=True) for a in text]:
        title = text.split("?:")[0][len_input:]
        body = "".join(text.split("?:")[1:])
        text_dict[title] = body
    return [text_dict]


def build_mail(text, organization):
    report_number = int(time.time())
    names = random.sample(random_names, (len(text[0].items())))

    template = Template(open('./templates/phishing_tpl.html').read())  # HTML Template stored inside /lib/
    tpl = template.render(newsletter=text, report_number=report_number, author_names=names)
    # html = open(f'./SeemsPhishy/newsletters/Newsletter-{organization}-{report_number}.html', 'w') #stores rendered report as HTML file
    html = open(f'./newsletters/Newsletter-{organization}.html', 'w')  # stores rendered report as HTML file
    html.write(tpl)
    html.close()
