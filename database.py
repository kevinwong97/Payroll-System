# database.py
# France Cheong
# 29/01/2019

# ########
# Packages
# ########
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database location
# Uniform Resource Identifier (URI) generic version of URL
# URI - a string of characters that unambiguously identifies a particular resource
DATABASE_URI = 'sqlite:///app.db'
# File app.db will be created in the folder where the python script is found

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    # echo=False means do not show generated SQL statements
    # Can be set to echo=True to show SQL
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 