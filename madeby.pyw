from tkinter import *
import tkvideo

dis2=Tk()
dis2.geometry('1080x620+300+200')
dis2.title('Made By')
dis2.resizable(False,False)

my_newlabel = Label(dis2)
my_newlabel.pack()
player = tkvideo.tkvideo("about.mp4", my_newlabel, loop = 1, size = (1080,620))
player.play()

dis2.mainloop()