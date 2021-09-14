from flask import Flask
from redis import Redis
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "8RkUb32S1FsMZzyuVE7lwVG7gd-bIiPXFBaMH78UHRvzIVsD8lsl1q_CYixM8ezeSPPeLjlbZSaZcOF1tCZydg"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
redis_cli = Redis(host='redis-db', port=6379)

# Init redis counter
redis_cli.set('count_docs', 0)

# noinspection PyPackageRequirements
from test_task import routes