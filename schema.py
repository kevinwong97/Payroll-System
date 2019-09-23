# schema.py


# Import packages
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
# Used by classes PurchaseOrder and PurchaseOrderItem
from sqlalchemy.orm import relationship 

# Get a base class from which all mapped classes should inherit
Base = declarative_base()

# Employee class should inherit from Base class
class Employee(Base): 

    # Define the name of the table i.e. employee (all lower case, singular)
    __tablename__ = 'employee'

    # Define the column names, types, primary key, foreign keys, null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    employee_id = Column(Integer, primary_key=True) # primary key
    firstname = Column(String(255), nullable=False) # non null
    lastname = Column(String(255), nullable=False) # non null
    title = Column(String(255), nullable=False) # non null, unique
    email = Column(String(255), nullable=False) # non null, unique
    work_phone = Column(String(20), nullable=False) # non null, unique
    date_employed = Column(String(15), nullable=False) # non null, unique
    employer_id = Column(Integer, ForeignKey("employer.employer_id")) # foreign key
    

# Define other classes in the database

# Supplier class should inherit from Base class
class Paydetails(Base):

    # Define the name of the table i.e. supplier (all lower case, singular)
    __tablename__ = 'pay_details'

    # Define the column names, types, primary key, foreign keys, null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    pay_details_id = Column(Integer, primary_key=True) # primary key
    hourly_rate = Column(Integer, nullable=False)
    total_hours = Column(Integer, nullable=False)
    net_pay = Column(Integer, nullable=False)
    total_deductions = Column(Integer, nullable=False)
    total_pay = Column(Integer, nullable=False)
    pay_slip_id = Column(Integer, ForeignKey("pay_slip.pay_slip_id")) # foreign key
    
    pay_slip = relationship("Payslip", back_populates="pay_details")
# Product class should inherit from Base class    
class Employer(Base):

    # Define the name of the table 
    __tablename__ = 'employer' # i.e. supplier (all lower case, singular)

    # Define the column names, types, primary key, foreign keys, null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    employer_id = Column(Integer, primary_key=True) # primary key
    firstname = Column(String(255), nullable=False) # non null
    lastname = Column(String(255), nullable=False) # non null
    title = Column(String(255), nullable=False) # non null, unique
    email = Column(String(255), nullable=False, unique=True) # non null, unique
    work_phone = Column(String(20), nullable=False, unique=True) # non null, unique
    date_employed = Column(String(15), nullable=False) # non null, unique
    
# PurchaseOrder class should inherit from Base class     
class Payslip(Base):

    # Define the name of the table
    __tablename__ = 'pay_slip' # i.e. purchase_order (all lower case, singular)

    # Define the column names, types, primary key, foreign keys, null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    pay_slip_id = Column(Integer, primary_key=True) # primary key
    payslip_date = Column(String(15), nullable=False)
    employee_id = Column(Integer, ForeignKey("employee.employee_id")) # foreign key
    

    # Define the 1:m relationship between purchase_order and purchase_order_items
    # format: field_name = relationship("ClassName", back_populates="field_name")
    # "back_populates" means populate the other side of the mapping
    # "cascade="all, delete-orphan" needed for 
    # cascading the deletion of a purchase_order to its purchase_order_items
    # "all" means the child object should follow along with its parent in all cases, 
    # and be deleted once it is no longer associated with that parent
    pay_details = relationship("Paydetails", back_populates="pay_slip", cascade="all, delete-orphan")


# PurchaseOrderItem class should inherit from Base class
#class PurchaseOrderItem(Base):

    # Define the name of the table # i.e. purchase_order_item (all lower case, singular)
    #__tablename__ = 'purchase_order_item' 

    # Define the column names, types, primary key, foreign keys, null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate

    # If having its own single column primary key
   # purchase_order_item_id = Column(Integer, primary_key=True) # Primary key
   #purchase_order_id = Column(Integer, ForeignKey("purchase_order.purchase_order_id")) # Foreign key
    #product_id = Column(Integer, ForeignKey("product.product_id"))

    #quantity = Column(Integer, nullable=False)
    # date_required = Column(Date, nullable=False)

    # Define the m:1 relationship between purchase_order_items and purchase_order
    # format: field_name = relationship("ClassName", back_populates="field_name")
    # "back_populates" required to populate the other side of the mapping
    