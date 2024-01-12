from tkinter import *
from tkinter import messagebox
import tkvideo
import ast

def sign_up():
    disp=Toplevel()
    disp.title("Sign Up")
    disp.geometry('1080x620+300+200')
    disp.resizable(False,False)

    my_newlabel = Label(disp)
    my_newlabel.pack()
    player = tkvideo.tkvideo("Media\\signup.mp4", my_newlabel, loop = 0, size = (1080,620))
    player.play()

    ###################################################################################################################
    def signup():
           username=user.get()
           password=code.get() 
           confirmm=confirm.get()

           if password==confirmm:
               try:
                   file=open('User_data\\datasheet.txt','r+')
                   d=file.read()
                   r=ast.literal_eval(d)

                   dict2={username:password}
                   r.update(dict2)
                   file.truncate(0)
                   file.close()

                   file=open('User_data\\datasheet.txt','w')
                   w=file.write(str(r))

                   messagebox.showinfo('Signup','Successfully Sign-Up')
                   disp.destroy()

               except:
                   file=open('User_data\\datasheet.txt',"w")
                   pp=str({'username':'password'})
                   file.write(pp)
                   file.close()
           else:
               messagebox.showerror('Invalid','Both password should match')

#####################################################################################################################

    def sign():
        disp.destroy()
#################################################################################################################
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')

    user=Entry(disp,width=30,fg='#f41d94',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=770,y=200)
    user.insert(0,'username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    #######################################################################################################################

    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')

    code=Entry(disp,width=30,fg='#f41d94',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=770,y=270)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    #########################################################################################################################

    def on_enter(e):
        confirm.delete(0,'end')
    def on_leave(e):
        if confirm.get()=='':
            confirm.insert(0,'Confirm Password')

    confirm=Entry(disp,width=30,fg='#f41d94',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    confirm.place(x=770,y=340)
    confirm.insert(0,'Confirm Password')
    confirm.bind('<FocusIn>',on_enter)
    confirm.bind('<FocusOut>',on_leave)

    ###############################################################################################################################

    Button(disp,width=35,pady=7,text='Sign Up',bg='#f41d94',fg='white',border=0,command=signup).place(x=765,y=410)

    signin=Button(disp,width=10,text='Sign In',border=0,bg='#f41d94',cursor='hand2',fg='white',command=sign)
    signin.place(x=930,y=465)


    disp.mainloop()
