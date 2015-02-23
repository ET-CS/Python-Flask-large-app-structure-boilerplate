# Flask Large Application Structure Template/Boilerplate/Example

Don't be mistaken - this is only "Hello, world!" app. but in big.

Beside of aim being template for new applications in Flask, This project also demonstrates several key concepts:

* Structure for large Flask application as module (inspired by https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications).
* Building app that supporting two modes: DEVELOPMENT, PRODUCTION. where in PRODUCTION mode all assets (html, less, js) are minified, and the practice of using the `dry` automation tool to minify all assets for production.
* The usage of two templates engine (Mako, Jinja2) in the same application so the PRODUCTION minified htmls would have no inheritance built in them (for performance). This method also could be used to embed js or css from other files into the html itself (if needed).
* My app structure philsosophy, where each view should be inside views/[view] folder with all files related to that view (include the controller!).

## Concept 1: Structure for large Flask application

This concept is must. Do you know the feeling when you start you Flask project and the main.py just gets too long..? You want to split the content into other files and `import` them but now, how can they reach your `app` variable?
Create the entire app as python package can help you sort those porblems up.
Also this project demonstrate how you should create config.py file at base directory to maintaine settings for your app.
Go and look at the source.. and see how I created a structure for large flask application.

## Concept 2: DEVELOPMENT versus PRODUCTION

Many developers don't seperate between DEVELOPMENT flow to PRODUCTION flow.
This is how I see the key differences in the development versus production flow:

DEVELOPMENT:

* Changes in code should be reflected immediatly using Flask code reload
* Enable Flask 'Debug=True' so error messages will sent to browser
* HTML should be served from the original (non minified) templates in real time without no caching
* LESS should be compiled on Client-Side.

PRODUCTION:

* No debug messages sent into browser for security reasons.
* All HTML files, JavaScript files should be minified.
* LESS files should be compiled in server side into CSS.
* All inheritence should be removed from templates to generate static one file templates
* Server should serve the minified templates and not the original htmls.
* Templates should be cached into memory.

Also, caching before the web-server (using tools such as nginx or varnish), or internal caching of rendered strings of the templates (for pages that could be cached) is an important practice and great feature that should be implemented for production.. but it's far from the scope of this example.

## Concept 3: Two templates engine

This concept used to seperate the inheritence in templates from production.
One template engine used to generate the inheritence (I love mako for this for his simple inheritence) and other template engine for the logic from controllers.
Look at `index.html` files inside `/app/views/index/` folder and see how from the first line to the last line is `mako` template engine inherit syntax, while the last line uses the `{{ }}` jinja2 syntax.
Also, look at the rendered `index.min.html` inside /app/build directory, and look how the Jinja2 syntax is still there, but mako is gone and inheritence is rendered.

## Concept 4: Dry

This project assets are all minified using `dry build` command.
I've supplied the minified files into this repository, so you could change into DEVELOPMENT mode and see how it's work.

Important to notice, that in DEVELOPMENT mode, the entire /views directory is served as static folder (so .css and .js files could be loaded without need to compile them into the static folder like in production). It's BAD in terms of security, as users can see and download the python files as well as the templates inside that directory. but HEY! it's DEVELOPMENT MODE!, don't forget to change to PRODUCTION when app is visible to the whole world.

## Concept 5: My app structure philsosophy

I've structed my projects in so many ways over the years, until lately It evolved into something new.
I found myself troubled by the why most modern apps are structed where controllers are in one folder, views in other, templates in other and so on..
I found myself wander between folder when working on one page in the app.
Lets say you work on the index route `/`, you are editing something in the controller which is either in /controllers folder, or in some main.py or urls.py in the base folder of your app.
Now, you go into /templates folder to edit the html file to show the new argument you've just passed into your template.
then, you go into /css folder to edit something in the css troubles you.
Now, it's time to edit the Javascript files located in another directory `/js`, to alert the user when you click on this new html item.

So much trouble...

As of today, I am trying a new structure design where I arrange my application files by routes and not by extension.
All index files should be in one folder
. /views/index/
              . __init__.py - controller for the `/` (index) route.
              . index.html
              . index.css (or index.less, index.sass, index.scss)
              . index.js
              . other files related only for that route (index in this example).

While other `site` oriented files should be at /views/ root:

. /views/
        . site.html
        . site.css
        . site.js
        . other files related to whole website.

that way, I can work on any page without (almost) change directory. all the related files for that page are in front of me. from the controller to the template and assets.

# Benefit

While in development mode, any change to the app files, either if it's .py files, html file or javascript file, will be reflected in your browser immediately without need to compile, reload, restart, build or any other action.

Just by changing the `PRODUCTION` setting in config.py file you can speed your website and be PRODUCTION ready!

[ TODO some benchmark ]

# Bottle

The same concept could be trasfered easily to Bottle (or any other micro-framework), as flask and bottle has very similar syntaxs. Jinja2 would have to be implemented manually though, as other things like static file serving and config loading which bottle framework doesn't implement for you in default.

# Last words

This very "simple" app has nothing really but "Hello, world!" message, but it should demonstrate an easy and smarter way of development in Python/Flask and thinking with production as well as development in mind.

I've added an empty model directory inside the app directory. It's only as concept as I didn't implemented any database or model in this simple example.


Push new ideas, fixes and I'll be happy to hear how you'd struct your project or if you'll do things differently.