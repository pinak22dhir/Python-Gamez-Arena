from tkinter import *
import tkvideo
import os

def calc():
    os.startfile('main.pyw')
def about():
    os.startfile('about.pyw')
def made():
    os.startfile('madeby.pyw')
def smthng():
    os.startfile('main2.pyw')
    dis1.destroy()
def hme():
    os.startfile('signinwindow.pyw')
    dis1.destroy()

dis1=Tk()
dis1.title("Python Gamez Arena")
dis1.geometry('1080x620+300+200')
dis1.resizable(False,False)

my_newlabel2 = Label(dis1)
my_newlabel2.pack()
player = tkvideo.tkvideo("pf.webm", my_newlabel2, loop = 1, size = (1080,620))
player.play()

Button(dis1,width=20,pady=2,text='Home',bg='#54e1fe',fg='#f8efda',border=0,command=hme).place(x=20,y=10)
Button(dis1,width=20,pady=2,text='About',bg='#54e1fe',fg='#f8efda',border=0,command=about).place(x=190,y=10)
#Button(dis1,width=20,pady=2,text='Leaderboards',bg='#54e1fe',fg='#f8efda',border=0).place(x=360,y=10)

Button(dis1,width=20,pady=2,text='Made by',bg='#54e1fe',fg='#f8efda',border=0,command=made).place(x=900,y=550)

Button(dis1,width=40,pady=2,text='Space Invaders',bg='#54e1fe',fg='#f8efda',border=0,command=calc).place(x=28,y=60)
Button(dis1,width=40,pady=2,text='Snake',bg='#54e1fe',fg='#f8efda',border=0,command=smthng).place(x=28,y=90)

dis1.mainloop()
