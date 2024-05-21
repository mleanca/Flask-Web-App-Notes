# This will store all the main views, routes, and url endpoints for the functional front-end aspect of the website
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return '<h1>Test</h1>'