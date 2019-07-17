

from flask import Flask
from api import bp
from view import view_bp

app = Flask('搬山道人')
app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/api')
app.register_blueprint(view_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(port=5000)