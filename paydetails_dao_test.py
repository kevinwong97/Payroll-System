# Import packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the DAO
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from paydetails_dao import PaydetailsDAO

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
    
    # Instantiate the Product DAO
    payd = PaydetailsDAO()

    # Setup the data as a dictionary
    data = {}
    data['hourly_rate'] = 25
    data['total_hours'] = 10
    data['net_pay'] = 250
    data['total_deductions'] = 25
    data['total_pay'] = 225
    data['pay_slip_id'] = 1

    # Call the create() method from the DAO
    # and pass the dictionary as parameter
    result = payd.create(session, data)

    # Print the result
    print(result)

    # Close the session
    session.close()

def test_find_by_id():
    # Get a session
    session = get_db_session()
    
    # Instantiate the Product DAO
    payd = PaydetailsDAO()

    
    pay_details_id = 3 # exists
    #pproduct_id = 5 # does not exist?
    
    # Call the find_by_id() method from the DAO
    # and pass the product_id as parameter - could pass it directly
    result = payd.find_by_id(session, pay_details_id)

    # Print the result
    print(result)

    # Close the session
    session.close()

def test_find_all():
    # Get a session
    session = get_db_session()
    
    # Instantiate the Product DAO
    payd = PaydetailsDAO()

    # Call the find_all() method from the DAO
    result = payd.find_all(session)

    # Print the result
    print(result)

    # Close the session
    session.close()    


def test_find_ids():
    # Get a session
    session = get_db_session()
    
    # Instantiate the Product DAO
    payd = PaydetailsDAO()

    # Call the find_ids() method from the DAO
    result = payd.find_ids(session)

    # Print the result
    print(result)

    # Close the session
    session.close()    

def test_update():
    # Get a session
    session = get_db_session()

    # Instantiate the Product DAO
    payd = PaydetailsDAO()

   
    pay_details_id = 1 # exists
   

    # Create a dictionary and add items
    # Do not add the employee_id to the dict
    data = {}
    #data['product_id'] = "" # No
    data['hourly_rate'] = 20
    data['total_hours'] = 20
    data['net_pay'] = 400
    data['total_deductions'] = 40
    data['total_pay'] = 360
    data['pay_slip_id'] = 1 
        
    # Call the update() method from the DAO
    # and pass the product_id and data as parameters    
    result = payd.update(session, pay_details_id, data)

    # Print the result
    print(result)

    # Close the session
    session.close()    

def test_delete():
    # Get a session
    session = get_db_session()
        
    # Instantiate the Product DAO
    payd = PaydetailsDAO()

    pay_details_id = 1 # exists
   

    # Call the delete() method from the DAO
    # and pass the pproduct_id as parameter - could pass it directly
    result = payd.delete(session, pay_details_id)

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

    test_find_ids()

    test_update()

    test_delete()

