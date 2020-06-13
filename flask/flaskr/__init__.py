from flask import Flask
import os
import importlib

# Instantiate flask class
app = Flask(__name__)

def deploy():

    # All api list to load
    api_list = ['hello', 'db']

    # Set SECRET_KEY
    app.config.from_mapping(SECRET_KEY=os.getenv('SECRET_KEY', 'dev'))

    # Load all blueprints inside directory.
    for f in api_list:

        # Import everything inside file
        m = importlib.import_module( 'apis.{}'.format(f) )

        # Register blueprint
        app.register_blueprint(m.bp)

    return app
