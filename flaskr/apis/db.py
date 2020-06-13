from flask import Blueprint

bp = Blueprint( 'db', __name__, url_prefix='/db' )

"""
GET /

A api that returns 'Hello World!' when it is accessed to root directory.
"""
@bp.route('/list')
def hello_world():

    return 'List rows inside table.'
