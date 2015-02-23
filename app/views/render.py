from app import app
from mako.template import Template
from mako.lookup import TemplateLookup; mylookup = TemplateLookup(directories=[app.config['VIEWS_DIR']])
from flask import render_template

def template(template_to_render, **kwargs):
    if app.config['PRODUCTION']:
    	# use the minified versions of the files
	return render_template(template_to_render + '.min.html', **kwargs)
    else:
	# if in debug mode - don't use the minified versions, so render files using both MAKO and Jinja.
	mytemplate = Template(filename=app.config['VIEWS_DIR'] + '/' + template_to_render  + '/' + template_to_render + '.html', lookup=mylookup).render(config = app.config)
	return app.jinja_env.from_string(mytemplate).render(**kwargs)