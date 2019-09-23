# menu.py

# http://effbot.org/tkinterbook/menu.htm

from tkinter import *
from employee_gui import *


class MenuGUI():

    def __init__(self, root):

        # Create a toplevel menu
        menubar = tk.Menu(root)

        # File menu
        # Create File pulldown menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command="")
        file_menu.add_command(label="Save", command="")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        # Add File pulldown menu to toplevel menu bar
        menubar.add_cascade(label="File", menu=file_menu)

        # Employee menu
        # Create a menu item
        # Menu items not in a pulldown do not appear on the Mac!
        # Need to add the menu item in a pulldown menu
        #menubar.add_command(label="Employee", command=self.create_employee_gui) 

        # Create Employee pulldown menu
        employee_menu = tk.Menu(menubar, tearoff=0)
        employee_menu.add_command(label="Employee", command=self.create_employee_gui) 
        # Add Employee pulldown menu to toplevel menu bar
        menubar.add_cascade(label="Employee", menu=employee_menu)


        # Exit menu item 
        # Does not work on the Mac, replace with a pull down
        # menubar.add_command(label="Quit", command=self.exit)

        # Create Exit pulldown menu
        exit_menu = tk.Menu(menubar, tearoff=0)
        exit_menu.add_command(label="Exit", command=self.exit) 
        # Add Exit pulldown menu to toplevel menu bar
        menubar.add_cascade(label="Exit", menu=exit_menu)


        # Display the toplevel menu
        root.config(menu=menubar)

    def create_employee_gui(self):
        if self.current_gui:
            self.current_gui.destroy()
        
        employee_gui = EmployeeGUI()
        self.current_gui = employee_gui.create_gui(self.root)
        pass

    def exit(self):
        exit()

if __name__ == '__main__':
    root = tk.Tk()
    MenuGUI(root)
    root.mainloop()
