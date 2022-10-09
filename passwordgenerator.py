# importing important libraries
from tkinter import *
import pyperclip
import random

# initializing the tkinter
passwd = Tk()

# setting the width and height of the window (window size)
passwd.geometry("600x600")    # x is small case here

# declaring a variable of string type and this variable will be
# used to store the password generated
passstr = StringVar()

# store the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)


# function to generate the password
def generate():

    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
            '*', '(', ')']

    # declaring the empty string
    password = ""

    # loop to generate the random password of the length entered
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passstr.set(password)

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Creating a text label widget
Label(passwd, text="Strong Password Generator Application", font="calibri 20 bold").pack()

# Creating a text label widget
Label(passwd, text="Enter the password length").pack(pady=3)

# Creating a entry widget to take password length entered by the
# user
Entry(passwd, textvariable=passlen).pack(pady=3)

# button to call the generate function
Button(passwd, text="Click here to Generate Password", command=generate).pack(pady=7)

# entry widget to show the generated password
Entry(passwd, textvariable=passstr).pack(pady=3)

# button to call the copytoclipboard function
Button(passwd, text="Click here to copy your password", command=copytoclipboard).pack()

# mainloop() is an infinite loop used to run the application when
# it's in ready state
passwd.mainloop()
