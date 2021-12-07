# app/__init__.py

from flask import Flask
from jac.contrib.flask import JAC
import jinja2
from jac import CompressorExtension

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object('config')

app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_OUTPUT_DIR'] = './static'
app.config['COMPRESSOR_STATIC_PREFIX'] = '/static'
jac = JAC(app)

env = jinja2.Environment(extensions=[CompressorExtension])
env.compressor_output_dir = './static'
env.compressor_static_prefix = '/static'
env.compressor_source_dirs = './static_files'

from src.SeemsPhishy.gui.app import views
