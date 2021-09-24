from flask import Flask
from redis import Redis
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "YourSecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init databases
db = SQLAlchemy(app)
redis_cli = Redis(host='redis-db', port=6379)

# Init redis counter
redis_cli.set('count_docs', 0)

# Import routes after init app
from test_task import routes