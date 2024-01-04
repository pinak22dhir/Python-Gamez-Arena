import tkinter as tk
from tkinter import messagebox
import ast
import tkvideo
import os

from signupwindow import sign_up

# Constants
USERNAME = 'username'
PASSWORD = 'password'
DATA_FILE = 'datasheet.txt'

def create_entry(disp, x, y, text):
    """Create an Entry widget with specific properties and events."""
    entry = tk.Entry(disp, width=30, fg='#f41d94', font=('Microsoft YaHei UI Light',11))
    entry.place(x=x, y=y)
    entry.insert(0, text)
    entry.bind('<FocusIn>', lambda e: entry.delete(0, 'end'))
    entry.bind('<FocusOut>', lambda e: entry.insert(0, text) if entry.get() == '' else None)
    return entry

def sign_in():
    """Sign in function."""
    username = user.get()
    password = code.get()

    try:
        with open(DATA_FILE, 'r') as file:
            data = ast.literal_eval(file.read())
    except FileNotFoundError:
        data = {}

    if username in data and password == data[username]:
        disp.destroy()
        os.startfile('gamewindow.pyw')
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

disp = tk.Tk()
disp.title("Login")
disp.geometry('1080x620+300+200')
disp.configure(bg="black")
disp.resizable(False,False)

my_label = tk.Label(disp)
my_label.pack()
player = tkvideo.tkvideo("assets/launcher/signin.mp4", my_label, loop = 0, size = (1080,620))
player.play()

user = create_entry(disp, 765, 240, USERNAME)
code = create_entry(disp, 765, 320, PASSWORD)

tk.Button(disp, width=35, pady=5, text='Sign In', bg='#f41d94', fg='white', border=0, command=sign_in).place(x=765, y=400)
tk.Button(disp, width=6, text='Sign Up', border=0, bg='#f41d94', fg='white', cursor="hand2", command=sign_up).place(x=965, y=466)

disp.mainloop()
