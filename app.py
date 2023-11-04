from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

def get_user():
    if 'user' not in session or session['user'] == None:
        return None
    else:
        return Usuario.query.filter_by(user_id=session['user']).first()

from routes.views import *
from routes.cadastrar import *
from routes.todo import *

if __name__ == '__main__':
    app.run(debug=True)