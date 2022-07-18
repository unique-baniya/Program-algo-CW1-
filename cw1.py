
from tkinter import * # i used tkinter to make the GUI

import pyperclip # we need to install pyperclip  # pip install pip 
import random

root = Tk()
root.geometry("700x500")
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)


def generate(): # Function to generate the password
  pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
      'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
      'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
      'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
      '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
      '*', '(', ')','1','2','3','4','5','6','7','8','9']
  password = ""
  for x in range(passlen.get()):
    password = password + random.choice(pass1)
  passwrd.set(password)

# function to copy the passcode


def copyclipboard():
  random_password = passwrd.get()
  pyperclip.copy(random_password)


# label to state our fonts and all 
Label(root, text="Strong Password Generator", font="Courier 30 bold").pack()
Label(root, text="unique's work", font="Courier 20 italic").pack()
Label(root, text="length of password").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Generate", command=generate).pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=3)
Button(root, text="copy to clipboard", command=copyclipboard).pack()
root.mainloop()
