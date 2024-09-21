from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database URL
DATABASE_URL = "sqlite:///concerts.db"

#  database engine
engine = create_engine(DATABASE_URL)

#  configured "Session" class
Session = sessionmaker(bind=engine)

#  session
session = Session()
