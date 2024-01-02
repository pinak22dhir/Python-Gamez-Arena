from tkinter import *
import tkvideo
import os

def invaders():
    os.startfile('games\\space_invaders.pyw')
def about():
    os.startfile('about.pyw')
def made():
    os.startfile('credits.pyw')
def snake():
    os.startfile('games\\snake.pyw')
def smthng3():
    os.startfile('D:\\Home\\Desktop\\All Stuff\\Chitkara University\\projects\\final games project\\GAMES\\fairnsquare\\fairnsquare.exe')
def smthng2():
    os.startfile('D:\\Home\\Desktop\\All Stuff\\Chitkara University\\projects\\final games project\\GAMES\\balls_64\\Balls.exe')
def smthng4():
    os.startfile('D:\\Home\\Desktop\\All Stuff\\Chitkara University\\projects\\final games project\\GAMES\\JellyDrift64\\Jelly Drift.exe')
def smthng5():
    os.startfile('D:\\Home\\Desktop\\All Stuff\\Chitkara University\\projects\\final games project\\GAMES\\Karlson64\\Karlson.exe')
def smthng6():
    os.startfile('D:\\Home\\Desktop\\All Stuff\\Chitkara University\\projects\\final games project\\GAMES\\LastTrainHome_1.2\\LastTrainHome\\LastTrain.exe')
def smthng7():
    os.startfile('D:\\Home\\Desktop\\All Stuff\\Chitkara University\\projects\\final games project\\GAMES\\TreeTeam64\\TreeTeam.exe')
def hme():
    os.startfile('signinwindow.pyw')
    dis1.destroy()

dis1=Tk()
dis1.title("Python Gamez Arena")
dis1.geometry('1080x620+300+200')
dis1.resizable(False,False)

my_newlabel2 = Label(dis1)
my_newlabel2.pack()
player = tkvideo.tkvideo("assets/launcher/pf.webm", my_newlabel2, loop = 1, size = (1080,620))
player.play()

Button(dis1,width=20,pady=2,text='Home',bg='#54e1fe',fg='#f8efda',border=0,command=hme).place(x=20,y=10)
Button(dis1,width=20,pady=2,text='About',bg='#54e1fe',fg='#f8efda',border=0,command=about).place(x=190,y=10)
#Button(dis1,width=20,pady=2,text='Leaderboards',bg='#54e1fe',fg='#f8efda',border=0).place(x=360,y=10)

Button(dis1,width=20,pady=2,text='Made by',bg='#54e1fe',fg='#f8efda',border=0,command=made).place(x=900,y=550)

Button(dis1,width=40,pady=2,text='Space Invaders',bg='#54e1fe',fg='#f8efda',border=0,command=invaders).place(x=28,y=60)
Button(dis1,width=40,pady=2,text='Snake',bg='#54e1fe',fg='#f8efda',border=0,command=snake).place(x=28,y=90)
Button(dis1,width=40,pady=2,text='Fair And Square',bg='#54e1fe',fg='#f8efda',border=0,command=smthng3).place(x=28,y=120)
Button(dis1,width=40,pady=2,text='Balls',bg='#54e1fe',fg='#f8efda',border=0,command=smthng2).place(x=28,y=150)
Button(dis1,width=40,pady=2,text='Jelly Drift',bg='#54e1fe',fg='#f8efda',border=0,command=smthng4).place(x=28,y=180)
Button(dis1,width=40,pady=2,text='Karlson',bg='#54e1fe',fg='#f8efda',border=0,command=smthng5).place(x=28,y=210)
Button(dis1,width=40,pady=2,text='Last Train Home',bg='#54e1fe',fg='#f8efda',border=0,command=smthng6).place(x=28,y=240)
Button(dis1,width=40,pady=2,text='Tree Team',bg='#54e1fe',fg='#f8efda',border=0,command=smthng7).place(x=28,y=270)

dis1.mainloop()
