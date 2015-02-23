# Use minified htmls rather then the source htmls
PRODUCTION = True
# alias for the opposite of PRODUCTION state
DEVELOPMENT = not PRODUCTION

# Statement for enabling the development environment in flask
DEBUG = not PRODUCTION

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
APP_DIR = BASE_DIR + '/app'
VIEWS_DIR = APP_DIR + '/views'
MIN_DIR = APP_DIR + '/build'

PORT = 1555

HOST = '0.0.0.0'