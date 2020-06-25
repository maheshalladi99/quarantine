from tkinter import *
import os

def reg_user():
    user_info=username.get()
    pass_info=password.get()

    file=open(user_info+".txt","w")
    file.write(user_info)
    file.write(pass_info)
    file.close


    user_entry.delete(0,END)
    pass_entry.delete(0,END)
    
    Label(screen1,text="Registration success",fg="green",font={"Calibri",11}).pack()
    
def Register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x300")

    global username
    global password
    global user_entry
    global pass_entry
    username=StringVar()
    password=StringVar()

    Label(screen1,text="enter details below").pack()
    Label(screen1,text="").pack()
        
    Label(screen1,text="username*").pack()
    user_entry= Entry(screen1,textvariable=username)
    user_entry.pack()
    Label(screen1,text="password*").pack()
    pass_entry= Entry(screen1,textvariable=password)
    pass_entry.pack()

    
    Label(screen1,text="").pack()
    Button(screen1,text="Register",width="30",height="2",command= reg_user).pack()
    Label(text="").pack()

    
def Login():
    print("hai")
    
    
             


def main_screen():
    global screen
    screen=Tk()
    
    screen.geometry("700x300")
    screen.title("nates 1.0")
    Label(text="nates 1.0",bg="grey", width="300",height="2",font={"Calibri",13}).pack()
    Label(text="").pack()
    Button(text="Login",width="30",height="2",command= Login).pack()
    Label(text="").pack()
    Button(text="Register",width="30",height="2",command= Register).pack()

    screen.mainloop()
    
main_screen()
    
