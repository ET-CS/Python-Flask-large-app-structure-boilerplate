from app import app; from app.views import *

@app.route("/")
def index():
    return render.template('index', name='world')