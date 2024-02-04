from flask import Flask
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DATABASE_URL = "mysql+pymysql://root:shaman@localhost:3306/Contash"
engine = create_engine(DATABASE_URL)
app = Flask(__name__)
CORS(app)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
