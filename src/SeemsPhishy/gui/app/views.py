from flask import render_template, request, session
#from src.SeemsPhishy.gui.app import app
from SeemsPhishy.gui.app import app
#from src.SeemsPhishy.gui.app.backend import Backend
from SeemsPhishy.gui.app.backend import Backend


backend = Backend("debug")
backend.connect()
app.secret_key = 'dljsawadslqk24e21cjn!Ew@@dsa5'
global text_gen_infos
text_gen_infos = None


@app.route('/')  # Home
def index():
    df_companies = backend.list_entities()
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
def datasets(send=False):
    return render_template("/datasets_overview.html", send=send)


@app.route('/datasets/entities')
def datasets_companies():
    df = backend.list_entities()
    return render_template("/datasets_companies.html", row_data=df.values.tolist(), column_names=df.columns, zip=zip, status_col="status")


@app.route('/datasets/files')
def datasets_files():
    df = backend.list_files()
    return render_template("/datasets.html", row_data=df.values.tolist(), column_names=df.columns, zip=zip, status_col="status")


@app.route('/textgeneration')
def text_generation_1(send=False):
    entities = backend.get_entity_names().entity.values.tolist()
    values = backend.get_entity_names().id.values.tolist()
    return render_template("/text_generation_1.html", entities=entities, values=values, zip=zip, send=send)


@app.route('/information-gain/execute')
def information_gain(send=False):
    entities = backend.get_entity_names().entity.values.tolist()
    values = backend.get_entity_names().id.values.tolist()
    return render_template("/information_gain_overview.html", entities=entities, values=values, zip=zip, send=send)


@app.route('/information-gain/entities')
def information_gain_companies():
    entities = backend.get_entity_names().entity.values.tolist()
    values = backend.get_entity_names().id.values.tolist()
    return render_template("/information_gain_companies.html", entities=entities, values=values, zip=zip)


@app.route('/information-gain/leakage')
def information_gain_leakage():
    df = backend.list_leakage_files()
    return render_template("/information_gain_leakage.html", row_data=df.values.tolist(), column_names=df.columns, zip=zip,
                           status_col="status")


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


#################################################################
@app.route('/add_new_entity', methods=['POST', 'GET'])
def add_new_entity():
    if request.method == 'POST':
        inputs = dict(request.form)
        print(inputs)
        if "ner" not in inputs:
            inputs["ner"] = False
        else:
            inputs["ner"] = True

        if "tf_idf" not in inputs:
            inputs["tf_idf"] = False
        else:
            inputs["tf_idf"] = True

        if "keywords" not in inputs:
            inputs["keywords"] = False
        else:
            inputs["keywords"] = True

        if "stop_words" not in inputs:
            inputs["stop_words"] = False
        else:
            inputs["stop_words"] = True

        print(inputs)

        backend.new_entity(inputs)
    return datasets(send=True)


@app.route('/start_information_gain', methods=['POST', 'GET'])
def start_information_gain():
    if request.method == 'POST':
        inputs = dict(request.form)
        print(inputs)
        if "ner" not in inputs:
            inputs["ner"] = False
        else:
            inputs["ner"] = True

        if "tf_idf" not in inputs:
            inputs["tf_idf"] = False
        else:
            inputs["tf_idf"] = True


        if "keywords" not in inputs:
            inputs["keywords"] = False
        else:
            inputs["keywords"] = True

        if "stop_words" not in inputs:
            inputs["stop_words"] = False
        else:
            inputs["stop_words"] = True
        
        print(inputs)
        backend.exec_information_gain(inputs)

    return text_generation_1(send=True)


@app.route('/display_information', methods=['POST', 'GET'])
def display_keyword_information():
    if request.method == 'POST':
        entity_id = request.form.get("entity_id")

        df = backend.get_keywords(entity_id)
        return render_template("/information_gain_companies_detail.html", row_data=df.values.tolist(), column_names=df.columns, zip=zip, status_col="status")

    return index()


@app.route('/text_gen2', methods=['POST', 'GET'])
def text_gen_choose_keywords():
    if request.method == 'POST':
        inputs = dict(request.form)
        if "ner" not in inputs:
            inputs["ner"] = False
        else:
            inputs["ner"] = True
        
        if "tf_idf" not in inputs:
            inputs["tf_idf"] = False
        else:
            inputs["tf_idf"] = True
            
        if "keywords" not in inputs:
            inputs["keywords"] = False
        else:
            inputs["keywords"] = True

        print(inputs)

        # fill text_gen_infos var
        global text_gen_infos
        text_gen_infos = inputs

    # entities = backend.get_entity_names().entity.values.tolist()
    # values = backend.get_entity_names().id.values.tolist()
    keywords = backend.get_keywords_textgen(inputs["entity_id"], inputs["ner"], inputs["tf_idf"], inputs["keywords"])
    print(keywords)
    return render_template("/text_generation_2.html", keywords=keywords.s_keyword.values.tolist(), ids=keywords.n_keyword_id.values.tolist(), zip=zip, send=False)


@app.route('/text_result', methods=['POST', 'GET'])
def text_result():
    global text_gen_infos
    print(text_gen_infos)
    # inputs = text_gen_infos | dict(request.form)        # needs python 3.9 or higher (joins two dicts together)
    # inputs = {**text_gen_infos, **dict(request.form)}
    keyword_list = request.form.getlist("list_keywords")
    generated_text = backend.generate_text(text_gen_infos, keyword_list)

    # TODO display result
    return render_template("/text_generation_result.html", generated_text=generated_text)
