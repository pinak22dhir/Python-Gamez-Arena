from tkinter import *
import tkvideo
import os


def about():
    os.startfile('about.pyw')
def Space_invaders():
    os.startfile('Games\\Space_Invaders\\main.pyw')
def snake():
    os.startfile('Games\\Snake\\main2.pyw')
    dis1.destroy()
def fair_and_square():
    os.startfile('Games\\fairnsquare\\fairnsquare.exe')
def balls():
    os.startfile('Games\\balls_64\\Balls.exe')
def karlson():
    os.startfile('Games\\Karlson64\\Karlson.exe')
def last_train():
    os.startfile('Games\\LastTrainHome\\LastTrainHome\\LastTrain.exe')
def smthng7():
    os.startfile('Games\\TreeTeam64\\TreeTeam.exe')
def home():
    os.startfile('main.pyw')
    dis1.destroy()

dis1=Tk()
dis1.title("Python Gamez Arena")
dis1.geometry('1080x620+300+200')
dis1.resizable(False,False)

my_newlabel2 = Label(dis1)
my_newlabel2.pack()
player = tkvideo.tkvideo("Media\\pf.webm", my_newlabel2, loop = 1, size = (1080,620))
player.play()

Button(dis1,width=20,pady=2,text='Home',bg='#54e1fe',fg='#f8efda',border=0,command=home).place(x=20,y=10)
Button(dis1,width=20,pady=2,text='About',bg='#54e1fe',fg='#f8efda',border=0,command=about).place(x=190,y=10)

Button(dis1,width=40,pady=2,text='Space Invaders',bg='#54e1fe',fg='#f8efda',border=0,command=Space_invaders).place(x=28,y=60)
Button(dis1,width=40,pady=2,text='Snake',bg='#54e1fe',fg='#f8efda',border=0,command=snake).place(x=28,y=90)
Button(dis1,width=40,pady=2,text='Fair And Square',bg='#54e1fe',fg='#f8efda',border=0,command=fair_and_square).place(x=28,y=120)
Button(dis1,width=40,pady=2,text='Balls',bg='#54e1fe',fg='#f8efda',border=0,command=balls).place(x=28,y=150)
Button(dis1,width=40,pady=2,text='Karlson',bg='#54e1fe',fg='#f8efda',border=0,command=karlson).place(x=28,y=210)
Button(dis1,width=40,pady=2,text='Last Train Home',bg='#54e1fe',fg='#f8efda',border=0,command=last_train).place(x=28,y=240)
Button(dis1,width=40,pady=2,text='Tree Team',bg='#54e1fe',fg='#f8efda',border=0,command=smthng7).place(x=28,y=270)

dis1.mainloop()
