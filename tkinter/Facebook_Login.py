#<<<<<<<<<----------------Login Page--------------->>>>>>>>>>

#Tkinter

import tkinter as tk
from PIL import Image , ImageTk
import os
import mysql
import mysql.connector
from tkinter import messagebox

#Mysql Connection

db = mysql.connector.connect(host="localhost",user="navaneesh",password="nana111",port="3307",db="facebook")
c= db.cursor()

#Tkinter

root = tk.Tk()
root.title("Facebook")


img = Image.open("tkinter/facebook2.png")
resize = img.resize((350,200))
img2 = ImageTk.PhotoImage(image=resize)

#Labels

l1 = tk.Label(root,image=img2)
l1.place(x=250,y=150)

l2 = tk.Label(root,text="Facebook helps you connect and share",font=("Arial",24,"bold"))
l2.place(x=250,y=350)

l3 = tk.Label(root,text="with the people in your life.",font=("Arial",24,"bold"))
l3.place(x=250,y=400)


#Frames

f1 = tk.Frame(master=root,width=500,height=500,background="#DCDCDC")
f1.place(x=900,y=130)

l4 = tk.Label(master=root,text="Mobile\t:",font=("Arial",15,"bold"),bg="#DCDCDC")
l4.place(x=950,y=203)

l5 = tk.Label(master=root,text="Password:",font=("Arial",15,"bold"),bg="#DCDCDC")
l5.place(x=950,y=302)

e1 = tk.Entry(master=root)
e1.place(x=1060,y=200,height=35,width=300)

e2 = tk.Entry(master=root)
e2.place(x=1060,y=300,height=35,width=300)

#Function

def create_acc():
    root.destroy()
    os.system("python tkinter/signup_page.py")
    

b1 = tk.Button(master=root,text="Create New Account",font=("Arial",12,"bold"),fg="white",bg="#66CD00",bd=0,width=20,height=2,command=create_acc)
b1.place(x=1050,y=550)

def forgot_password():
    root.destroy()
    os.system("python tkinter/forgotten_passwd.py")

b2 = tk.Button(master=root,text="Forgotten Password ?",font=("Arial",12,"bold"),fg="Blue",width=45,height=2,command=forgot_password)
b2.place(x=920,y=450)

def login():
    mbl = e1.get()
    passwd = e2.get()
    
    query = "select Password from info where Mobile = %s"
    
    val = (mbl,)
    
    c.execute(query,val)
    
    data = c.fetchone()
    
    
        
  
    try :
    
      if data[0] == passwd :
        messagebox.showinfo("Mark Mama","Login Success..!")
        #  l6.config(text="Login Successful...!",fg="Green",font=("MS Serif",15,"bold"))
        #  l6.place(x=1050,y=650)
         
    except :
        pass   
    
    try :
        if data[0] != passwd :
             messagebox.showerror("Mark Mama","Wrong Password..!")
            # l6.config(text="Wrong Password...!",fg="red",font=("MS Serif",15,"bold"))
            # l6.place(x=1050,y=650)
            
    except:
        pass        
            
        
    try :
        if not mbl or not passwd:
             messagebox.showerror("Mark Mama","please Fill all the Details..!")
            # l6.config(text="Please fill all Details..",font=("MS Serif",15,"bold"),fg="red")    
        elif data == None :
            messagebox.showerror("Mark Mama","This Number have no Account.Please create Account First..!")
            # l6.config(text="This number have no Account.Please create Accout First ..!",fg="red",font=("MS Serif",15,"bold"))
        
    except :
        pass  
            

b3 = tk.Button(master=root,text="Log in",font=("Arial",12,"bold"),fg="white",bg="blue",width=45,height=2,command=login)
b3.place(x=920,y=380)

l6 = tk.Label(root,text="")
l6.place(x=950,y=650)


root.mainloop()
