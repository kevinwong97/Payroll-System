
import tkinter as tk
from tkinter import messagebox

# From file xxx.py import class Xxxx
from employee_gui import EmployeeGUI
from paydetails_gui import PaydetailsGUI
from PIL import ImageTk, Image  


class MenuGUI2():

    def __init__(self):   

        print("Creating Menu GUI ...")
        
        self.current_gui = None # Reference to current GUI 

        # Step 1. Create main window of the application
        # 900x500 pixels in the middle of the screen
        # Can minimise to 0x0 pixels
        self.root = tk.Tk()
        self.root.title("Menu")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        print("Main window coordinates (width, height, x, y) :", 
              width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        # Step 2. Add a menu

        # Create a toplevel menu
        menubar = tk.Menu(self.root)

        # File menu (pulldown)
        # Create a pulldown menu
        filemenu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        filemenu.add_command(label="Main Menu", command=self.main_menu_gui)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="File", menu=filemenu)
       
        # Employee menu (pulldown)
        # Create a pulldown menu
        employee_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        # do not use self.create_employee_gui()
        employee_menu.add_command(label="Employee", 
            command=self.create_employee_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Employee", menu=employee_menu)
      
        # Product menu (pulldown)
        # Create a pulldown menu
        paydetails_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        paydetails_menu.add_command(label="Pay Details", 
            command=self.create_paydetails_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Pay Details", menu=paydetails_menu)

        # Reports menu (pulldown)
        reports_menu = tk.Menu(menubar, tearoff=0)
        reports_menu.add_command(label="Report", 
                                 command=self.create_report_gui)
        menubar.add_cascade(label="Reports", menu=reports_menu)

        # Display the menu
        self.root.config(menu=menubar)

        pass
            
    # Functions to create child frames 
    # when menu options are selected

    def create_employee_gui(self):
        if self.current_gui:
            self.current_gui.destroy()
        
        employee_gui = EmployeeGUI()
        self.current_gui = employee_gui.create_gui(self.root)
        pass

    def create_paydetails_gui(self):
        if self.current_gui:
            self.current_gui.destroy()
        
        paydetails_gui = PaydetailsGUI()
        self.current_gui = paydetails_gui.create_gui(self.root)
        pass

    def create_report_gui(self):
        pass        
    

    def create_main_gui(self, root):
        main_frame = tk.Frame(root)
        main_frame.pack()
        return main_frame

    def main_menu_gui(self):
        if self.current_gui:
            self.current_gui.destroy()

        self.current_gui = create_main_gui(self.root)
        pass  
    

# ###########
# Main method
# ###########

if __name__ == '__main__':
    """
    The main method is only executed when the file is 'run' 
    (not imported in another file)
    """
    #
    # Instantiate the main application gui 
    # it will create all the necessary GUIs
    gui = MenuGUI2()
    # Run the mainloop 
    # the endless window loop to process user inputs
    gui.root.mainloop()
    pass        