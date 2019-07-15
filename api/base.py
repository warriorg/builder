from flask import Blueprint
from db.context import Context

bp = Blueprint('ping', __name__, url_prefix='/')
dbContext = Context('oracle', 'jdbc:oracle:thin:@192.168.10.133:1521:JGDBM', 'GWSTD', 'chinaport2018')
