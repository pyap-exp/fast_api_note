from urllib.parse import quote_plus

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(f'postgresql+psycopg://{config("DB_USER")}:{quote_plus(config("DB_PASSWORD"))}@{config("DB_HOST")}/{config("DB_NAME")}')
conn = engine.connect()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
