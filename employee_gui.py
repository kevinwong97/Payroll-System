

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox
import calendar 
# #################################################
# Import any of your classes defined in other files
# #################################################

import database as db # Import database.py to get a session to a particular db
# From file xxx.py import class Xxxx
from dateutil.parser import parse
from employee_dao import EmployeeDAO # To communicate with Employee table
from validation import Validation # To validate the entries made on the form

# #################
# EmployeeGUI Class
# #################

class EmployeeGUI():
    """
    GUI class to perform CRUD operations on the employee table in the database.
    """   

    def __init__(self):   
    
        # Instantiate a data access object 
        # Contains methods to access the database
        self.emp_dao = EmployeeDAO()

        # Instantiate a validation object
        # Contains methods to validate input fields
        self.validator = Validation()

        # Form fields
        # Instantiate stringvars - hold  data entered in  fields of form
        self.employee_id = tk.StringVar()
        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()
        self.title = tk.StringVar()
        self.email = tk.StringVar()
        self.work_phone = tk.StringVar()
        self.date_employed = tk.StringVar()
        self.employer_id = tk.StringVar()

        # List of employee ids - lb for listbox
        self.lb_ids = None

        # Messagebox title
        self.mb_title_bar = "Employee CRUD"

        pass 

    def create_gui(self, root):
        """
        Create a high level frame which contains the entire GUI 
        (of this part of the application) and adds it to the root window.
        Notice that the "root" window is passed the second parameter in the 
        method header.
        Also notice that the first (and mandatory) parameter to all methods 
        is "self" i.e. a reference to the object instantiated from the class.

        Widgets like labels, entries, etc  (including inner frames) are added 
        to the high level frame 
        At the end, the function return a reference to the frame that was 
        created for the calling program to be able to access it.

        Parameters (apart from self):
            root: main window of application

        Return: 
            emp_frame: the frame containing all the widgets for the employee CRUD 

        """

        # Good practice to print something at the start of the method 
        # e.g. which method is being executed, the values of parameters passes, 
        # etc
        # Good for tracing the execution of the program while debugging it
        # After debugging, you may want to "comment out" some of the 
        # print statements so that they do not execute and print too 
        # much stuff in the console
        print("Creating employee GUI ...")

        # emp_frame = tk.Frame(root).pack() 
        # cannot write the above as pack() does not return anything
        # and need the variable name to refer to it elsewhere
        # DO NOT SPECIFY ANY WIDTH AND HEIGHT OF THE FRAMES 
        # HERE FOR FLEXIBILITY REASONS
        # The height and width or the root window can be specified 
        # in the main GUI (or in the main() method)
        emp_frame = tk.Frame(root)
        emp_frame.pack()

        # Add a frame to contain the form widgets
        # For 'tkinter frame' options, 
        # refer to  http://effbot.org/tkinterbook/frame.htm
        # For 'tkinter pack' options, 
        # refer to http://effbot.org/tkinterbook/pack.htm
        # To put a number of widgets in a column one on top of the other, 
        # just use pack() without any options
        # Use the fill=tk.X option to make all widgets as wide as the parent widget
        # To pack widgets side by side, use the side option 
        # e.g. side=tk.LEFT, tk.BOTTOM, tk.RIGHT (default is tk.TOP)
        # Use the fill=tk.Y option to make all widgets as tall as the parent widget
        # have also fill=tk.BOTH option
        # The anchor= option is used to position the widget in the container, 
        # default is tk.CENTER
        # Internal padding around widgets: ipadx= and ipady=  default is 0
        # External padding arounf widgets: padx= pady=  default is 0
        form_frame = tk.Frame(emp_frame)
        form_frame.pack()
    
        # row 0:  title label
        # The variable name is not needed
        # For 'tkinter label' options, 
        # refer to  http://effbot.org/tkinterbook/label.htm
        # By default, the text is centered
        # To right align use anchor=e (east) not justify=RIGHT which is used 
        # for aligning multiple lines
        # Labels have padx= and pady= options but no ipadx= and ipady=
        # Check the ulr above, to finc out more about the many options 
        # available for configuring labels!!!
        # STICK TO THE DEFAULT VALUES,  
        # UNLESS YOU HAVE A GOOD REASON TO CHANGE THEM!!!!!!!!!!!!!!!!
        # For 'tkinter grid' options, 
        # refer to http://effbot.org/tkinterbook/grid.htm
        # For spanning multiple rows and columns, 
        # use rowspan= and columnspan= options (default is 1)
        # Use the sticky= option for positioning 
        # (instead of anchor= as used in pack) - 
        # (default is centered) values are: n, w, e, w, nw, etc
        # Internal padding around widgets: ipadx= and ipady=  default is 0
        # External padding around widgets: padx= pady=  default is 0
        # Use the width= option to specify how wide in terms of number of characters
        tk.Label(form_frame, font=('arial', 10), 
                 text = "Employee").grid(row=0, column=0, columnspan=3)

        # row 1: employee_id label, employee_id entry and list_of_ids label
        tk.Label(form_frame, text= "Employee Id", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=1, column=0)
        # Need to use both padx and pady to leave a vertical space between rows of labels
        # And a space between the  label and its entry field
        # For 'tkinter Entry' options, 
        # refer to http://effbot.org/tkinterbook/entry.htm
        # Entry has no padding options
        # Use the width= option to specify how wide in terms of number of characters
        tk.Entry(form_frame, textvariable=self.employee_id, width=30, bd=1, 
                 state=tk.DISABLED).grid(row=1, column=1)
        # employee_id is disabled to prevent user from entering a value
        # employee_id is generated by the database because AUTOINCREMENT 
        # was specified in the database schema
        tk.Label(form_frame, text= "Employee IDs", 
                 font=('arial', 10)).grid(row=1, column=2)
        
        # row 2: firstname label, firstname entry and listbox of ids
        tk.Label(form_frame, text= "First name", font=('arial', 10), 
                 width=20, anchor="e", bd=1, pady=10, padx=10).grid(row=2, column=0)
        tk.Entry(form_frame, textvariable=self.firstname, 
                 width=30, bd=1).grid(row=2, column=1)
        # For 'tkinter Listbox' options, 
        # refer to http://effbot.org/tkinterbook/listbox.htm
        # Use the height= option to specify the height, default is 10
        # Use the width= option to specify the number of characters, default is 20
        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=2, column=2, rowspan=5) 
        # 'self' means instance attribute rather than local variable
        # since python allows using variables before they are declared
        # it does not matter whether lb_ids has been declared or not at the 
        # top of the file before the methods definition
        # Set the method to be called when an item is clicked on the listbox 
        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)

        # row 3: lastname label and entry (the listbox will go through)
        tk.Label(form_frame, text= "Last name", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=3, column=0)
        tk.Entry(form_frame, textvariable=self.lastname, 
                 width=30, bd=1).grid(row=3, column=1)

        # row 4: title label and combobox (the listbox will go through)
        tk.Label(form_frame, text= "Title", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=4, column=0)
        # Readonly combobox - prevent the user from adding values
        # For 'tkinter Combobox' options, 
        # refer to https://docs.python.org/3.1/library/tkinter.ttk.html
        # Cannot find a good reference!
        # The state= option is either "normal" for read/write or "readonly" 
        # to prevent the user from adding values
        VALUES = ('Mr','Mrs','Ms', 'Miss', 'Dr')
        ttk.Combobox(form_frame, state="readonly", textvariable=self.title, 
                  values=VALUES, width=10).grid(row=4, column=1, sticky="w")
        # Display first value - prevents a blank value being displayed (and selected!)          
        self.title.set(VALUES[0]) 
        
        # row 5: email label and combobox (the listbox will go through)
        tk.Label(form_frame, text= "Email", font=('arial', 10), 
                 width=20, anchor="e", bd=1, pady=10, padx=10).grid(row=5, column=0)
        tk.Entry(form_frame, textvariable=self.email, width=30, bd=1).grid(row=5, column=1)

        # row 6: work_phone label and combobox (the listbox will go through)
        tk.Label(form_frame, text= "Work Phone", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=6, column=0)
        tk.Entry(form_frame, textvariable=self.work_phone, 
                 width=30, bd=1).grid(row=6, column=1)
        
        #row 7 : date employed
        tk.Label(form_frame, text= "Date Employed", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=7, column=0)
        tk.Entry(form_frame, textvariable=self.date_employed, 
                width=30, bd=1).grid(row=7, column=1)
        
        tk.Label(form_frame, text= "Employer Id", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=8, column=0)
        tk.Entry(form_frame, textvariable=self.employer_id, 
                 width=30, bd=1).grid(row=8, column=1)
        # def print_sel():
        #    print(cal.selection_get())
             
        # top = tk.Toplevel(root)

        # cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
        #            cursor="hand1", year=2018, month=2, day=5)

        # cal.pack(fill="both", expand=True)
        # ttk.Button(top, text="ok", command=print_sel).pack()
        
 

        # Buttons
        # There are 3 columns of widgets in the frame and 4 buttons
        # Better insert the button in another frame
        # Also easier to pack them from the left than using a grid with row 
        # and col locations
        # pady to leave a space from frame on top
        button_frame = tk.Frame(emp_frame, pady=10) 
        button_frame.pack()
        # For 'tkinter Button' options, 
        # refer to http://effbot.org/tkinterbook/button.htm
        # Use the anchor= option to position the button
        # External padding around buttons: padx= pady=  default is 0
        # Use the width= option to specify the number of characters, 
        # otherwise calculated based on text width
        tk.Button(button_frame, width=10, text="Clear", 
                  command=self.clear_fields).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Save", 
                  command=self.save).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Delete", 
                  command=self.delete).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Load", 
                  command=self.load).pack(side=tk.LEFT)       

        # Return a reference to the high level frame created
        # Will need the reference to be able to destroy it in the calling function
        return emp_frame

    def clear_fields(self):
        """
        Clear the fields of the form

        Parameters (apart from self): None

        Return: None
        """

        # Just blank all the fields
        self.employee_id.set("")
        self.firstname.set("")
        self.lastname.set("")
        #self.title.set("") # Do not clear if using dropdown
        self.email.set("")
        self.work_phone.set("")
        self.date_employed.set("")
        self.employer_id.set("")
        pass

    def save(self):
        """
        Save the data displayed on the form to the database.
        The employee data to be saved is obtained from the global 
        instance attributes.
        The data is validated by calling another method called validate_fields()
        If the data is invalid, a message box is presented to the user.
        If the data is valid, the data is either saved or updated
        If an employee_id is present, the data is updated
        If not, a new employee record is create in the database
 
        Parameters (apart from self): None
 
        Return: None
            
        """

        print("Saving an employee ...")

        # Get the data
        data = self.get_fields()   

        # Validate the data
        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (len(data['employee_id'])==0):
                # If nothing has been entered in employee_id 
                # i.e. its length is zero characters
                print("Calling create() as employee_id is absent")
                self.create(data)
            else:
                print("Calling update() as employee_id is present")
                self.update(data)
                pass
        else:
            message_text = "Invalid fields.\n" + message 
            messagebox.showwarning(self.mb_title_bar, message_text, icon="warning")
            pass

    def get_fields(self):
        """
        Get the data entered in the fields of the form

        Parameters (apart from self): None

        Return:
            emp: dictionary object containing all the information 
                 about an employee
        """

        emp = {}
        # employee_id is ignored when creating a record
        emp['employee_id'] = self.employee_id.get() 
        emp['firstname'] = self.firstname.get()
        emp['lastname'] = self.lastname.get()
        emp['title'] = self.title.get()
        emp['email'] = self.email.get()
        emp['work_phone'] = self.work_phone.get()
        emp['date_employed'] = self.date_employed.get()
        emp['employer_id'] = self.employer_id.get()
        return emp    

    def validate_fields(self, data):
        """
        Validate the data entered in the fields of the form

        Parameters (apart from self):
            data: dictionary object containing all the information entered on the form

        Return:
             valid_data: a boolean indication whether the data is valid 
                         (True) or not valid (False)
             message: a string containing details about the fields that are not valid
             Note: when these values are returned as a tuple 
                   (valid_data, message) i.e. a list that cannot be changed

        """
           
        # By default set to true, anything wrong will turn it to false   
        valid_data = True 
        # Instantiate an empty list to contain the messages
        message_list = [] 
        # Check for blank fields
        # Do not check employee_id as this is generated by the database
        #if len(data['employee_id']==0:
        #    valid_data = False
        #    message_list.append("employee_id is empty")
        if len(data['firstname'])==0:
            valid_data = False
            message_list.append("firstname is empty")
        if len(data['lastname'])==0:
            valid_data = False
            message_list.append("lastname is empty")
        if len(data['title'])==0:
            valid_data = False
            message_list.append("title is empty")
        if len(data['email'])==0:
            valid_data = False
            message_list.append("email is empty")
        if len(data['work_phone'])==0:
            valid_data = False
            message_list.append("work_phone is empty")
        if len(data['date_employed'])==0:
            valid_data = False
            message_list.append("date_employed is empty")
        if len(data['employer_id'])==0:
            valid_data = False
            message_list.append("employer_id is empty")

        # Other possible checks

        # Implement these as functions in the Validation class so that 
        # other classes can call them
         
        # Check if firstname and lastname contain  
        # only alphabetic characters (and may be certain special characters)
        if not self.validator.is_alphabetic(data['firstname']):
            valid_data = False
            message_list.append("invalid firstname")

        if not self.validator.is_alphabetic(data['lastname']):
            valid_data = False
            message_list.append("invalid lastname")
    
        # Check if title is in a list [Mr, Ms, Mrs, Dr, etc]
        # Alternatively could use a dropbox/combobox to do this
        # However, if the combobox is not set to a default value 
        # (to force the user to select something)
        # A blank value can get through
        if self.title.get() not in ["Mr", "Ms", "Mrs", "Miss", "Dr"]:
            valid_data = False
            message_list.append("title should be Mr, Ms, Mrs, Miss or Dr")

        # Check if email follows a certain pattern 
        # i.e contains an @ followed by a dot
        if not self.validator.is_email(data['email']):
            valid_data = False
            message_list.append("invalid email format")

        # Check if work_phone follows a certain pattern 
        # i.e. (02) 99999999 or (02) 9999 9999 or +61 3 9999 9999 (international)
        #if not self.validator.is_phone_number(data['work_phone']):
        #    valid_data = False
        #    message_list.append("invalid phone number format")
        
            
        # Join the items in the list as a string separated with a comma and a space    
        message = ', '.join(message_list) 

        return valid_data, message # return 2 values

    def create(self, data):
        """
        Create a new record in the database.
        A messagebox is used display the outcome (success or failure) 
        of the create operation to the user.

        Parameters (apart from self):
            data: dictionary object containing employee data to be saved
 
        Return: None
        """

        print("Creating an employee ...")
        print(data)

        session = db.get_db_session() # Get a session (database.py)
        result = self.emp_dao.create(session, data) 
          # result is a tuple e.g. ("Employee added successfully", 1004) 
        #result, employee_id = self.emp.create(data) 
          # if you wish to get the message and employee_id separately
        session.close() # Close the session

        # Display the returned message to the user - use a messagebox
        # For 'tkinter messagebox' options, 
        # refer to http://effbot.org/tkinterbook/tkinter-standard-dialogs.htm
        # Format: message.function(title, message [, options])
        # Functions: showinfo, showwarning, showerror, askquestion, 
        #            askokcancel, askyesno, or askretrycancel
        # Use the icon= option to specify which icon to display 
        # e.g. icon="warning", "error", "info", "question"     
        # Display everything that is returned in the result
        messagebox.showinfo(self.mb_title_bar, result)
 
        pass

    def update(self, data):
        """
        Update a record in the database
        A messagebox is used display the outcome (success or failure) 
        of the update operation to the user.

        Parameters (apart from self):
            data: dictionary object containing employee data to be saved
 
        Return: None
        """

        print("Updating an employee ...")
        print(data)

        session = db.get_db_session() # Get a session (database.py)
        result = self.emp_dao.update(session, data['employee_id'], data)
        session.close() # close the session

        # Display the returned message to the user - use a messagebox  
        # Display everything that is returned in the result      
        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def delete(self):
        """
        Delete a record from the database
        The employee_id of the record to be deleted is obtained from a 
        global attribute.

        A messagebox is used display the outcome (success or failure) 
        of the delete operation to the user.

        Parameters (apart from self): None
 
        Return: None

        """

        # Grab the employee_id from the stringvar
        id = self.employee_id.get() 
        print(id)
        
        # Call the data access object to do the job
        # Pass the id as parameter to the delete() method
        session = db.get_db_session() # Get a session (database.py)
        result = self.emp_dao.delete(session, id)
        session.close() # Close the session

        # Display the returned message to the user - use a messagebox    
        # Display everything that is returned in the result    
        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def load(self):
        """
        Retrieve a list of IDs from the database and load them into a listbox
 
        Parameters (apart from self):
  
        Return: None
        """

        session = db.get_db_session() # Get a session (database.py)
        result = self.emp_dao.find_ids(session) # {"employee_ids": [1, 2, 3]}
        session.close() # Close the session
        print("result", result)
        # Check if there is an entry in the result dictionary
        if "employee_ids" in result: 
            list_ids = result['employee_ids'] # will crash if there is no entry!
            # Set the returned list into the listbox
            # Before doing that, must clear any previous list in the box
            self.lb_ids.delete(0,tk.END)
            print("Setting employee_id in listbox ...")
            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
                #print(x)
            pass

    def on_list_select(self, evt):
        """
        on_list_select() is triggered when a user clicks an item in the listbox.
        This was defined with the statement 
        "self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)" 
        defined above in create_gui()

        Parameters (apart from self):
            evt: object containing information about the mouse click

        Return: None
        """
        # For more information on 'tkinter events', 
        # refer to http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        w = evt.widget
        index = int(w.curselection()[0]) 
          # index = position of the item clicked in the list, first item is item 0 not 1
        value = w.get(index) 
          # value of the item clicked, in our case it's the employee_id
        print(index) 
        print(value)

        # Call find_by_id and populate the stringvars of the form
        session = db.get_db_session() # Get a session (database.py)
        result = self.emp_dao.find_by_id(session, value)   
        session.close() # close the session
        print("result", result) 
           # { "employee" : {"employee_id": "", "firstname": "", etc}}
        emp = result['employee']
        self.populate_fields(emp)
        pass

    def populate_fields(self, emp):
        """
        Populate the fields of the form with data

        Parameters (apart from self):
            emp: dictionary object containing all the information about an employee

        Return:
        """

        # Set the values from the dict to the stringvars
        self.employee_id.set(emp['employee_id'])
        self.firstname.set(emp['firstname'])
        self.lastname.set(emp['lastname'])
        self.title.set(emp['title'])
        self.email.set(emp['email'])
        self.work_phone.set(emp['work_phone'])
        self.date_employed.set(emp['date_employed'])
        self.employer_id.set(emp['employer_id'])
        pass

# ###########
# Main method
# ###########

if __name__ == '__main__':
    """
    The main method is only executed when the file is 'run' 
    (not imported in another file)
    """
     
    # Setup a root window (in the middle of the screen)
    root = tk.Tk()
    root.title("Payroll System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = EmployeeGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass