from flask import Blueprint

bp = Blueprint( 'hello', __name__, url_prefix='/hello' )

"""
GET /hello

A api that returns 'Hello World!' when it is accessed to root directory.
"""
@bp.route('/')
def hello_world():

    return 'Hello World!'
