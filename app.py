

from flask import Flask
from api import bp
# from view import view_bp
from code.ssm import SSM
from db.context import Context

app = Flask('搬山道人')

app = Flask(__name__)

app.register_blueprint(bp, url_prefix='/api')
# app.register_blueprint(view_bp, url_prefix='/')

dbContext = Context('oracle', 'jdbc:oracle:thin:@192.168.10.133:1521:JGDBM', 'GWSTD', 'chinaport2018')

table = dbContext.userTables()[0]

columns = dbContext.columns(table['name'])

if __name__ == '__main__':
    ssm = SSM(table, columns, "com.warriorg.test")
    ssm.generate()
    # app.run(port=5000, debug=True)
