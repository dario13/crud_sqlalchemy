from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root@172.20.0.2/example_sqlalchemy")
Session = sessionmaker(bind=engine)

Base = declarative_base()