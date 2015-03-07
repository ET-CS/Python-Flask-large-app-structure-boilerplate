__all__ = ["render",]

# All views should be imported here. TODO maybe implement some way to auto-import all sub-directories.
import index

from app import app
from flask import request, send_from_directory

@app.route('/favicon.ico')
@app.route('/humans.txt')
@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])