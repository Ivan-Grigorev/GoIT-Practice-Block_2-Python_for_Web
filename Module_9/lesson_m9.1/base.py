from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:v320@localhost:5432/compucter_firm')
Session = sessionmaker(bind=engine)

Base = declarative_base()
