# employee_dao_test.py


"""
The test is best done on an empty database as the employee_id used is 1
And it can be run more than once
"""

# Import packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse
from datetime import date
# Import the DAO
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from employee_dao import EmployeeDAO

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

def test_create():
    # Get a session
    session = get_db_session()
    
    # Instantiate the employee DAO
    emp = EmployeeDAO()

    # Setup the data as a dictionary
    """
    data = {}
    data['firstname'] = "Kevin"
    data['lastname'] = "Wong"
    data['title'] = "Mr"
    data['email'] = "Kevin@gmail.com"
    data['work_phone'] = "(02) 9999 9999"
    data['data_employed'] = date(2019, 1, 22)
    """

    # Alternatively, the data could be set up in JSON format
    data = {
        'firstname':"Kevin",
        'lastname': "Wong",
        'title': "Mr",
        'email': "Kevin@gmail.com",
        'work_phone': "(02) 9999 9999", # no comma on last item
        'date_employed': "2019-01-22",
        'employer_id': "3"
    }

    # Call the create() method from the DAO
    # and pass the dictionary as parameter
    result = emp.create(session, data)

    # Print the result
    print(result)

    # Close the session
    session.close()

def test_find_by_id():
    # Get a session
    session = get_db_session()
    
    # Instantiate the employee DAO
    emp = EmployeeDAO()

    # Assign an employee_id
    employee_id = 1 # exists
    #employee_id = 2 # does not exist?
    
    # Call the find_by_id() method from the DAO
    # and pass the employee_id as parameter - could pass it directly
    result = emp.find_by_id(session, employee_id)

    # Print the result
    print(result)
    
    # Close the session
    session.close()

def test_find_all():
    # Get a session
    session = get_db_session()
    
    # Instantiate the employee DAO
    emp = EmployeeDAO()

    # Call the find_all() method from the DAO
    result = emp.find_all(session)

    # Print the result
    print(result)

    # Close the session
    session.close()    

def test_find_by_lastname():
    # Get a session
    session = get_db_session()
        
    # Instantiate the employee DAO    
    emp = EmployeeDAO()
      
    # Assign a lastname  
    lastname = "Wong" # exists
    #lastname = "xyz" # does not exist

    # Call the find_by_lastname() method from the DAO
    # and pass the lastname as parameter - could pass it directly
    result = emp.find_by_lastname(session, lastname)

    # Print the result
    print(result)

    # Close the session
    session.close()  

def test_find_ids():
    # Get a session
    session = get_db_session()
    
    # Instantiate the employee DAO
    emp = EmployeeDAO()

    # Call the find_ids() method from the DAO
    result = emp.find_ids(session)

    # Print the result
    print(result)

    # Close the session
    session.close()    

def test_update():
    # Get a session
    session = get_db_session()

    # Instantiate the employee DAO
    emp = EmployeeDAO()

    # Assign an employee_id 
    employee_id = 1 # exists
    #employee_id = 2 # does not exist?

    # Create a dictionary and add items
    # Do not add the employee_id to the dict
    data = {}
    data['firstname'] = "James"
    data['lastname'] = "Wong"
    data['title'] = "Mr"
    data['email'] = "Kevin@gmail.com"
    data['work_phone'] = "(02) 7778 2132"
    data['date_employed'] = "2019-01-25"
    data['employer_id'] = "2"
    # Alternatively, the data could be defined in JSON format
        
    # Call the update() method from the DAO
    # and pass the employee_id and data as parameters    
    result = emp.update(session, employee_id, data)

    # Print the result
    print(result)

    # Close the session
    session.close()    

def test_delete():
    # Get a session
    session = get_db_session()
        
    emp = EmployeeDAO()

    # Assign an employee_id
    employee_id = 1 # exists
    #employee_id = 2 # does not exist?

    # Call the delete() method from the DAO
    # and pass the employee_id as parameter - could pass it directly
    result = emp.delete(session, employee_id)

    # Print the result
    print(result)

    # Close the session
    session.close()          

if __name__ == "__main__":

    # You may wish to comment/uncomment the functions calls below
    # To select which ones to run or not to run

    # If you run test_create() twice in a row
    # You will try to insert the same record twice
    # You Will get an integrity error
    # Phone number has to be unique
    # Either comment out test_create() (to run the other function calls)
    # Or use DB Browser for SQLite to delete the record

    # You may want to run test_delete() last
    # Because if you delete the record as soon as you insert
    # You cannot run the other tests like test_find_by_id(), test_update()

    # Use DB Browser for SQLite to check if data was really inserted/updated/deleted

    # If the database is opened in DB Browser for SQLite, 
    # you might not run the tests as the database will be locked
    # Need to close the database in DB Browser for SQLite

    print("\nTesting ...")

    # Test the create() method
    test_create()
    
    test_find_by_id()

    test_find_all()

    test_find_by_lastname()

    test_find_ids()

    test_update()

    test_delete()

