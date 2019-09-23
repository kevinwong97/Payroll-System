# create_tables.py
# France Cheong
# 21/01/2019

# Import packages
from sqlalchemy import create_engine

# Import the Base class from which all mapped classes inherited in schema.py
# This class maintains a catalogue of classes and tables
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from schema import Base 

# Database location
# Uniform Resource Identifier (URI) generic version of URL
# URI - a string of characters that unambiguously identifies a particular resource
DATABASE_URI = 'sqlite:///app.db'
# File app.db will be created in the folder where the python script is found

engine = create_engine(DATABASE_URI, echo=False)
# echo=False means do not show generated SQL statements
# Can be set to echo=True to show SQL

# Create the database and the tables
Base.metadata.create_all(engine)
# All the classes/tables specified in schema.py will be created
# If database file app.db does not exist, it will be created as well
# Does not delete a table if it exists and has data in it