from flask import Blueprint
from db.context import Context

bp = Blueprint('ping', __name__, url_prefix='/')
dbContext = Context('oracle', 'jdbc:oracle:thin:@127.0.0.1:1521:JGDBM', 'GWSTD', 'xxxxx')
