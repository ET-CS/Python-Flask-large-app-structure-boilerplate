# dry settings file.
# use `dry build` command to compile.
target_folder = "../build"
target_css_folder = "../static/css"
target_js_folder = "../static/js"

templating = True
template_engine = 'mako'
context = { 'config': { 'PRODUCTION': True } }