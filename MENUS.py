

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("eZPass")

root.resizable(0, 0)


aLabel=ttk.Label(root, text="eZPass")
aLabel.grid(column=0, row=0)

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







def mainMenu():

    action = ttk.Button(root, text="Login", command=loginClick)
    action.grid(column=1, row=0)
    action1 = ttk.Button(root, text="Sign Up", command=signupClick)
    action1.grid(column=2, row=0)



action = ttk.Button(root, text="Login", command=loginClick)
action.grid(column=1, row=0)
action1 = ttk.Button(root, text="Sign Up", command=signupClick)
action1.grid(column=2, row=0)

root.mainloop()
