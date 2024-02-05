from flask import Flask
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()
DATABASE_URL = os.environ['MYSQL_CONNECTION_STRING']
engine = create_engine(DATABASE_URL)
app = Flask(__name__)
CORS(app)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
