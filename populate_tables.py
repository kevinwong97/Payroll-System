# populate_tables.py


# ########
# Packages
# ########
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import date
# ###########################################
# Import your classes defined in other files
# ###########################################
# From file xxx.py import class Xxxx
from schema import Employer
from schema import Employee
from schema import Payslip
from schema import Paydetails




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

def populate():

    # Get a session
    session = get_db_session()


    # Insert a list [] of Employees to employee table 
    # using the Employee constructor
    session.add_all([
        Employer(
                 firstname = 'Jeff',
                 lastname = 'Reynold',
                 title = 'Mr', 
                 email = 'jeffrey@gmail.com',
                 work_phone = '(03) 98743214',
                 date_employed = '2019-01-25'),
                        
        Employer(firstname = 'Jam', 
                 lastname = 'Booster', 
                 title = 'Mrs', 
                 email = 'jam@booster.com',
                 work_phone = '(03) 98145457',
                 date_employed = '2019-01-30'
                 ),

        Employer(firstname = 'Julie', 
                 lastname = 'Rome', 
                 title = 'Ms', 
                 email = 'julie@rome.com', 
                 work_phone='(03) 98157691',
                 date_employed = '2019-01-12'
                 ),    
        ])

    session.add_all([
        Employee(
                 firstname = 'George', 
                 lastname = 'Tanner', 
                 title = 'Mr', 
                 email = 'g.tanner@theorg.com', 
                 work_phone = '(03) 98120001',
                 date_employed = '2019-05-20',
                 employer_id = 1,
                 ),
                        
        Employee(firstname = 'Samantha', 
                 lastname = 'Riley', 
                 title = 'Mrs', 
                 email = 's.riley@theorg.com',
                 work_phone = '(03) 98120002',
                 date_employed = '2019-04-30',
                 employer_id = 2 ),

        Employee(firstname = 'Rebecca', 
                 lastname = 'White', 
                 title = 'Ms', 
                 email = 'r.white@theorg.com', 
                 work_phone='(03) 98120003',
                 date_employed = '2019-07-16',
                 employer_id = 3
                 ),    
        ])


    session.add_all([
        
        # PO 1
        Payslip( 
            employee_id = 1, 
            payslip_date = '2019-10-23',
                pay_details = [
                    Paydetails(
                        hourly_rate = 25, 
                        total_hours = 10, 
                        net_pay = 250,
                        total_deductions = 25,
                        total_pay = 225,
                        ), 

                        # More items

                    ] 
            ), 

        Payslip( 
            employee_id = 2, 
            payslip_date = '2019-10-20',
                pay_details = [
                    Paydetails(
                        hourly_rate = 40, 
                        total_hours = 10, 
                        net_pay = 400,
                        total_deductions = 40,
                        total_pay = 360,
                        ), 

                        # More items

                    ] # 
            ), # 
        
        Payslip( 
            employee_id = 3, 
            payslip_date = '2019-10-15',
                pay_details = [
                    Paydetails(
                        hourly_rate = 75, 
                        total_hours = 15, 
                        net_pay = 1125,
                        total_deductions = 112.5,
                        total_pay = 1012.5,
                        ), 

                        # More items

                    ] # 
            ), # 

    # etc
        ])
    # Commit the transactions
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
        populate()
