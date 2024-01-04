import tkinter as tk
from tkinter import messagebox
import tkvideo
import ast

# Constants
USERNAME = 'username'
PASSWORD = 'password'
CONFIRM_PASSWORD = 'Confirm Password'
DATA_FILE = 'datasheet.txt'

def create_entry(disp, x, y, text):
    """Create an Entry widget with specific properties and events."""
    entry = tk.Entry(disp, width=30, fg='#f41d94', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
    entry.place(x=x, y=y)
    entry.insert(0, text)
    entry.bind('<FocusIn>', lambda e: entry.delete(0, 'end'))
    entry.bind('<FocusOut>', lambda e: entry.insert(0, text) if entry.get() == '' else None)
    return entry

def sign_up():
    """Create a sign up window."""
    disp = tk.Toplevel()
    disp.title("Sign Up")
    disp.geometry('1080x620+300+200')
    disp.resizable(False,False)

    my_newlabel = tk.Label(disp)
    my_newlabel.pack()
    player = tkvideo.tkvideo("assets/launcher/signup.mp4", my_newlabel, loop = 0, size = (1080,620))
    player.play()

    user = create_entry(disp, 770, 200, USERNAME)
    code = create_entry(disp, 770, 270, PASSWORD)
    confirm = create_entry(disp, 770, 340, CONFIRM_PASSWORD)

    def signup():
        """Sign up function."""
        username = user.get()
        password = code.get() 
        confirmm = confirm.get()

        if password == confirmm:
            try:
                with open(DATA_FILE, 'r+') as file:
                    data = ast.literal_eval(file.read())
                    data.update({username: password})
                    file.seek(0)
                    file.write(str(data))
                    file.truncate()
                messagebox.showinfo('Signup', 'Successfully signed up')
                disp.destroy()
            except FileNotFoundError:
                with open(DATA_FILE, 'w') as file:
                    file.write(str({USERNAME: PASSWORD}))
        else:
            messagebox.showerror('Invalid', 'Both passwords should match')

    tk.Button(disp, width=35, pady=7, text='Sign Up', bg='#f41d94', fg='white', border=0, command=signup).place(x=765, y=410)
    tk.Button(disp, width=10, text='Sign In', border=0, bg='#f41d94', cursor='hand2', fg='white', command=disp.destroy).place(x=930, y=465)

    disp.mainloop()
