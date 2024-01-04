from tkinter import *
import tkvideo


window=Tk()
window.geometry('1080x620')
window.resizable(False,False)

def exit():
    window.destroy()

my_newlabel2 = Label(window)
my_newlabel2.pack()
player = tkvideo.tkvideo("assets/launcher/Python Games Arena.mp4", my_newlabel2, loop = 1, size = (1080,620))
player.play()

Button(text='exit',command=exit).place(x=1020,y=570)

window.mainloop()