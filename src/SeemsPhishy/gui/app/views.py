from flask import render_template, request, session
from src.SeemsPhishy.gui.app import app


app.secret_key = 'dljsawadslqk24e21cjn!Ew@@dsa5'


@app.route('/')  # Home
def index():
    return render_template("/index.html")


@app.route('/datasets')
def datasets():
    return render_template("/datasets_overview.html")


@app.route('/datasets/companies')
def datasets_companies():
    import pandas as pd
    data = [['Alex', 10, 1], ['Bob', 12, 0], ['Clarke', 13, 2], ['Clarke', 13, 3], ['Clarke', 13, 2], ['Clarke', 13, 3]]
    df = pd.DataFrame(data, columns=['Name', 'Age', "Status"], dtype=float)
    print(df.head())
    return render_template("/datasets_companies.html", row_data=df.values.tolist(), column_names=df.columns, zip=zip, status_col="Status")


@app.route('/datasets/pdfs')
def datasets_pdfs():
    return render_template("/datasets_pdfs.html")


@app.route('/text-generation/letter')
def text_generation_letter():
    return render_template("/text_generation_letter.html")


@app.route('/text-generation/email')
def text_generation_email():
    return render_template("/text_generation_email.html")


@app.route('/text-generation/newsletter')
def text_generation_newsletter():
    return render_template("/text_generation_newsletter.html")


@app.route('/information-gain')
def information_gain():
    return render_template("/information_gain_overview.html")


@app.route('/information-gain/companies')
def information_gain_companies():
    return render_template("/information_gain_companies.html")


@app.route('/information-gain/leakage')
def information_gain_leakage():
    return render_template("/information_gain_leakage.html")

#################################################################

@app.route('/faq')
def faq():
    return render_template("/faq.html")


@app.route('/settings')
def settings():
    return render_template("/settings.html")


@app.route('/profile')
def profile():
    return render_template("/profile.html")

#################################################################


@app.route('/search', methods=['POST', 'GET'])
def search():
    return render_template("/datasets_companies.html")

