from flask import render_template, request, session
from src.SeemsPhishy.gui.app import app
from src.SeemsPhishy.gui.app.backend import Backend

backend = Backend("debug")
backend.connect()
app.secret_key = 'dljsawadslqk24e21cjn!Ew@@dsa5'


@app.route('/')  # Home
def index():
    df_companies = backend.list_companies()
    no_file, no_keywords, no_texts = backend.get_dashboard_infos()
    donut_label, donut_data = backend.get_dashboard_donut_data()
    return render_template("/index.html",
                           row_data=df_companies.values.tolist(),
                           column_names=df_companies.columns,
                           zip=zip,
                           status_col="status",
                           no_file=no_file[0],
                           no_keywords=no_keywords[0],
                           no_texts=no_texts[0],
                           no_file_sub=no_file[1],
                           no_keywords_sub=no_keywords[1],
                           no_texts_sub=no_texts[1],
                           donut_label=donut_label,         # ["Keyword1", "Keyword2", "other"],
                           donut_data=donut_data)           # [100, 222, 400])


@app.route('/datasets/new')
def datasets():
    return render_template("/datasets_overview.html")


@app.route('/datasets/companies')
def datasets_companies():
    df = backend.list_companies()
    return render_template("/datasets_companies.html", row_data=df.values.tolist(), column_names=df.columns, zip=zip, status_col="status")


@app.route('/datasets/files')
def datasets_files():
    df = backend.list_files()
    return render_template("/datasets.html", row_data=df.values.tolist(), column_names=df.columns, zip=zip, status_col="status")


@app.route('/text-generation/letter')
def text_generation_letter():
    return render_template("/text_generation_letter.html")


@app.route('/text-generation/email')
def text_generation_email():
    return render_template("/text_generation_email.html")


@app.route('/text-generation/newsletter')
def text_generation_newsletter():
    return render_template("/text_generation_newsletter.html")


@app.route('/information-gain/execute')
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


#################################################################

@app.errorhandler(404)
def not_found(e):
    # defining function
    return render_template("404.html")
