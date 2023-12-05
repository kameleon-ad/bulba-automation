from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from openai import OpenAI

DB_MIGRATE = Migrate()
SQL_DB = SQLAlchemy()
OPENAI_CLIENT = OpenAI()
