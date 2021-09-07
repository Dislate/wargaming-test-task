from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "8RkUb32S1FsMZzyuVE7lwVG7gd-bIiPXFBaMH78UHRvzIVsD8lsl1q_CYixM8ezeSPPeLjlbZSaZcOF1tCZydg"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
redis_cli = FlaskRedis(app)


from test_task import routes