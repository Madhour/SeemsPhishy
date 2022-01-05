# app/__init__.py

from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object('config')

#from src.SeemsPhishy.gui.app import views
from SeemsPhishy.gui.app import views

app.run(host="0.0.0.0")
