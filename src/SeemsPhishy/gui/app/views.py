from flask import render_template, request, session
import psycopg2

from src.SeemsPhishy.gui import app


@app.route('/')  # Home
def index():

    return "hello world"
