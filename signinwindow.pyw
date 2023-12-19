from tkinter import *
from tkinter import messagebox
import ast
import tkvideo
from signupwindow import sign_up
import os

display= Tk()
display.title("Login")
display.geometry('1080x620+300+200')
display.configure(bg="black")
display.resizable(False,False)

my_label = Label(display)
my_label.pack()
player = tkvideo.tkvideo("signin.mp4", my_label, loop = 0, size = (1080,620))
player.play()

###########################################################################################################

###########################################################################################################
def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    if username in r.keys() and password==r[username]:
        display.destroy()
        os.startfile('gamewindow.pyw')
        # screen=Toplevel(display)
        # screen.title('app')
        # screen.geometry('925x500+300+200')
        # screen.config(bg='white')

        # Label(screen,text='hello',bg='#fff',font=('calibri(Body)',50,'bold')).pack(expand=True)

        # screen.mainloop()
    else:
        messagebox.showerror('invalid','Invalid username of password')
#########################################################################################################################################
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user=Entry(display,width=30,fg='#f41d94',font=('Microsoft YaHei UI Light',11))
user.place(x=765,y=240)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'password')


code=Entry(display,width=30,fg='#f41d94',font=('Microsoft YaHei UI Light',11))
code.place(x=765,y=320)
code.insert(0,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Button(display,width=35,pady=5,text='sign in',bg='#f41d94',fg='white',border=0,command=signin).place(x=765,y=400)

sign_up= Button(display,width=6,text='sign up',border=0,bg='#f41d94',fg='white',cursor="hand2",command=sign_up)
sign_up.place(x=965,y=466)


display.mainloop()