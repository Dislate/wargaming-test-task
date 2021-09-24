from flask.cli import AppGroup
from test_task import db

start_cli = AppGroup('start', short_help="First settings cli for first start")


@start_cli.command('create_db')
def create_db():
    """Function create database and all tables"""
    db.create_all()
    db.session.commit()
