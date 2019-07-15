

from flask import Flask
from api import bp
from view import view_bp

app = Flask('搬山道人')
app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/api')
<<<<<<< HEAD
app.register_blueprint(view_bp, url_prefix='/')
=======
# app.register_blueprint(view_bp, url_prefix='/')

dbContext = Context('oracle', 'jdbc:oracle:thin:@127.0.0.1:1521:JGDBM', 'GWSTD', 'xxxxx')

table = dbContext.userTables()[0]

columns = dbContext.columns(table['name'])
>>>>>>> 7a32434e3ece4965f993db1dc73514cfa7e3f3db

if __name__ == '__main__':
    app.run(port=5000)
