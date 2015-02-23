#!/usr/bin/env python
from flask import Flask
app = Flask(__name__, template_folder='views')

# Configurations
app.config.from_object('config')

# Load views
import views

# run server
def run():
    # Change template_folder to minified versions
    if app.config['PRODUCTION']:
        print " * starting in PRODUCTION mode"
        import jinja2
        my_loader = jinja2.ChoiceLoader([
	    jinja2.FileSystemLoader([app.config['MIN_DIR'],]),
            app.jinja_loader,
        ])
        app.jinja_loader = my_loader
    else:
        print " * starting in DEVELOPMENT mode"
        app.static_folder='views'
    host = app.config['HOST']
    port = app.config['PORT']
    debug = app.config['DEBUG']
    app.run(host=host, port=port, debug=debug)