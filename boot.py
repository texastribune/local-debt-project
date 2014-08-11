import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

logging.basicConfig(filename='logs/debt.log',level=logging.WARNING)
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
logger = logging.getLogger()

Base = declarative_base()

engine = create_engine('sqlite:///debt.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
