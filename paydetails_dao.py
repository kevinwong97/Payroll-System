
# Import packages
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from schema import Payslip
from schema import Paydetails

class PaydetailsDAO():

    def create(self, session, data):

        # Print info for debugging
        print("\nCreating paydetails ...") #\n means print("\n") a blank line
        print(data)

        # Instantiate an object of the mapped Product class - defined in schema.py
        # SKip the product_id when inserting as it will be generated by the database
        paydetails = Paydetails(
                     hourly_rate = data['hourly_rate'],
                     total_hours = data['total_hours'],
                     net_pay = data['net_pay'],
                     total_deductions = data['total_deductions'],
                     total_pay = data['total_pay'],
                     pay_slip_id = data['pay_slip_id']
        )
        # Get the session to add the employee object            
        session.add(paydetails)
        session.commit() # Must commit to save the record permanently

        # Create a blank dictionary to return the result
        result = {}  
        result['message'] = 'Paydetails added successfully!'
        inserted_pay_details_id = paydetails.pay_details_id
        result['pay_details_id'] = inserted_pay_details_id
        return result # return the result as a dictionary 

    def find_by_id(self, session, pay_details_id):

        # Print info for debugging
        print("\nFinding paydetails ...")
        print(pay_details_id)
       

        # Get the session to query the Product class
        # And get by the primary key i.e. product_id
        payd = session.query(Paydetails).get(pay_details_id)
        
        # Create a blank dictionary to return the result
        result = {}

        # prod is a single Alchemy object - no need for a loop to process
        if not payd:
            # If no product found i.e. prod is none
            result['message'] = "Paydetails NOT found"
        else:
            # Else grab the values in the returned SQLalchemy object
            # And build another python dictionary
            d = {} # Create an empty dict and add items to it
            d['pay_details_id'] = payd.pay_details_id
            d['hourly_rate'] = payd.hourly_rate
            d['total_hours'] = payd.total_hours
            d['net_pay'] = payd.net_pay
            d['total_deductions'] = payd.total_deductions
            d['total_pay'] = payd.total_pay
            d['pay_slip_id'] = payd.pay_slip_id
            

            # Store the prod dict in the result dict under key "product"
            result['paydetails'] = d
            #session.commit() # not needed for find as not saving changes            
        
        # Note that the return is not part of the if/else block
        # Ensure it's indented to the left
        return result # return the result as a dictionary

    def find_all(self, session):

        # Print info for debugging
        print("Finding all paydetails ...")

        # Create a blank dictionary to return the result
        result = {}

        # Get the session to query the Product class and get all (may wish to sort)
        rows = session.query(Paydetails).all()

        if not rows:
            result['message'] = "No paydetails found!"
        else:
            # Convert list of Alchemy objects to a list of dictionaries
            list_paydetails = [] # Create an empty list to append prod dicts
            for x in rows: # rows is a list of Alchemy objects - process one by one
                d = {} # Create an empty dict and add items to it
                d['pay_details_id'] = x.pay_details_id
                d['hourly_rate'] = x.hourly_rate
                d['total_hours'] = x.total_hours
                d['net_pay'] = x.net_pay
                d['total_deductions'] = x.total_deductions
                d['total_pay'] = x.total_pay
                d['pay_slip_id'] = x.pay_slip_id
                list_paydetails.append(d) # Append the employee dict to the employee list
                pass    

            # Store the prod list in the result dict under key "products"               
            result['products'] = list_paydetails

        # return the result as a dictionary
        return result 

    
    def find_ids(self, session):
        """
        This is a special method similar to find_all but returns product_ids only, 
        not the full details
        """

        # Print info for debugging
        print("\nFinding all paydetails ids ...")

        # Create a blank dictionary to return the result
        result = {}

        # Get the list of products from the database
        rows = session.query(Paydetails).all()

        if not rows:
            result['message'] = "No paydetails found!"
        else:
            # Convert list of Alchemy objects to a list of dictionaries
            list_ids = []
            for x in rows:
                list_ids.append(x.pay_details_id)
                pass               

            # Store the list of ids in the result dict under key "employee_ids"
            result['pay_details_id'] = list_ids

        return result # return the result as a dictionary

    

    def update(self, session, pay_details_id, data):

        # Print info for debugging
        print("Updating paydetails ...")
        print(pay_details_id)
        print(data)

        result = {}

        # Find the product record  
        payd = session.query(Paydetails).get(pay_details_id)

        # What happens if the product is not found?
        if payd:
            # product was found
            # Need to find out which field has changed!
            # Just update all fields
            #prod.product_id = data['product_id'] # Not the primary key!  
            payd.hourly_rate = data['hourly_rate']
            payd.total_hours = data['total_hours'] 
            payd.net_payd = data['net_pay']
            payd.total_deductions = data['total_deductions']
            payd.total_pay = data['total_pay']
            payd.pay_slip_id = data['pay_slip_id']

            session.commit() # Don't forget to commit 

            # Store an appropriate message in the result dict under key "message"
            result['message'] = "Paydetails updated!"     
        else:
            result['message'] = "Paydetails not found!"

        return result # return the result as a dictionary
        
    def delete(self, session, pay_details_id):

        # Print info for debugging
        print("\nDeleting Paydetails ...")
        print(pay_details_id)
 
        # Create a blank dictionary to return the result
        result = {}

        # Find the record and get the session to delete it  
        payd = session.query(Paydetails).get(pay_details_id)
        # What happens if the product is not found?         
        if payd:
            session.delete(payd)          
            session.commit()   # Don't forget to commit    

            # Store an appropriate message in the result dict under key "message"
            result['message'] = "Paydetails deleted"  
        else:  
            result['message'] = "Paydetails not found"

        return result # return the result as a dictionary        