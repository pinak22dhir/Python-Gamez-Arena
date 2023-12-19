from tkinter import *
import tkvideo


window=Tk()
window.geometry('1080x620')
window.resizable(False,False)

def quite():
    window.destroy()

my_newlabel2 = Label(window)
my_newlabel2.pack()
player = tkvideo.tkvideo("D:\\Home\\Desktop\\All Stuff\\Chitkara University\\projects\\final games project\\Python Games Arena.mp4", my_newlabel2, loop = 1, size = (1080,620))
player.play()

Button(text='exit',command=quite).place(x=1020,y=570)

window.mainloop()