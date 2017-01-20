
#importing the GUI as well as langauges
import tkinter as tk
from tkinter import ttk
#header of the interface, the most top part
root = tk.Tk()
root.title("eZPass")
#doesn't need to be there but it means that the screen won't resize, unless widgets are used
root.resizable(0, 0)

#label for the main menu
aLabel=ttk.Label(root, text="eZPass")
aLabel.grid(column=0, row=0)
#login function with 2 entry widgets and labels as well as a Finish button that goes back to main menu. 2 destroy functions to delete the login and signup from the main menu
def loginClick():
    ttk.Label(root, text="Enter Student ID #"). grid(column=0, row=0)
    ttk.Label(root, text="Enter your Password"). grid(column=0, row=2)
    action.destroy()
    action1.destroy()
    name=tk.StringVar()
    nameEntered = ttk.Entry(root, width=12, textvariable=name)
    nameEntered.grid(column=0, row=1)
    name1=tk.StringVar()
    name1Entered = ttk.Entry(root, width=12, textvariable=name1)
    name1Entered.grid(column=0, row=3)
    finishbutton = ttk.Button(root, text="Finish", command=mainMenu)
    finishbutton.grid(column=0, row=5)
#same as login function but with 1 more entry widget and label, same 2 destroy functions
def signupClick():

    ttk.Label(root, text="Enter Student ID #"). grid(column=0, row=0)
    ttk.Label(root, text="Write your eMail"). grid(column=0, row=2)
    ttk.Label(root, text="Enter a new Password"). grid(column=0, row=4)
    action.destroy()
    action1.destroy()
    name2 = tk.StringVar()
    name2Entered=ttk.Entry(root, width=12, textvariable=name2)
    name2Entered.grid(column=0, row=1)
    name3=tk.StringVar()
    name3Entered= ttk.Entry(root, width=30, textvariable=name3)
    name3Entered.grid(column=0, row=3)
    name4 = tk.StringVar()
    name4Entered= ttk.Entry(root, width=12, textvariable=name4)
    name4Entered.grid(column=0, row=5)
    signupfinishbutton= ttk.Button(root, text="Finish", command=mainMenu)
    signupfinishbutton.grid(column=0, row=7)

#main menu with login and sign up button that go to the other 2 functions above respectively
def mainMenu():

    action = ttk.Button(root, text="Login", command=loginClick)
    action.grid(column=1, row=0)
    action1 = ttk.Button(root, text="Sign Up", command=signupClick)
    action1.grid(column=2, row=0)


#so that the code runs
action = ttk.Button(root, text="Login", command=loginClick)
action.grid(column=1, row=0)
action1 = ttk.Button(root, text="Sign Up", command=signupClick)
action1.grid(column=2, row=0)
#finish of the code
root.mainloop()






