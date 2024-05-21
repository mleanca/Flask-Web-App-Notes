# This file makes the "website" folder a python package, so we can import this folder and run it automatically anywhere

# pip installed flask, flask-login module and flask-sqlalchemy (a database, a wrapper for sql to make it easier to create and manage the database)
from flask import Flask

def create_app():
    print('Creating app')
    app = Flask(__name__) # initializing Flask
    app.config['SECRET_KEY'] = 'afagn rwguineo nvjona vnamacaocacma' # to encrypt and secure keys
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    
    return app # an app is now created
    