from flask import Blueprint

bp = Blueprint( 'db', __name__, url_prefix='/db' )

"""
GET /db/list

A api that returns rows from table
"""
@bp.route('/list')
def hello_world():

    return 'List rows inside table.'
