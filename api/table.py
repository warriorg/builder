
from .base import bp, dbContext

import json


@bp.route('/table', methods=['get'])
def list():
    tables = dbContext.userTables()
    return json.dumps(tuple(tables))


@bp.route('/table/<tableName>/column', methods=['get'])
def columns(tableName):
    columns = dbContext.columns(tableName)
    return json.dumps(tuple(columns))
