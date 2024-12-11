#<<<<<<<<---------Forgotten Password--------->>>>>>>>

#Libraries

import tkinter as tk
from PIL import Image, ImageTk
import mysql
import mysql.connector
import os
from tkinter import messagebox

#Mysql Connection

db = mysql.connector.connect(host="localhost",user="navaneesh",password="nana111",port="3307",db="facebook")
c = db.cursor()

#Tkinter

root = tk.Tk()
root.title("Change Password")

f1 = tk.Frame(master=root,width=530,height=550,background="#DCDCDC")
f1.place(x=790,y=110)

img = Image.open("tkinter/facebook2.png")
resize = img.resize((350,200))
img2 = ImageTk.PhotoImage(image=resize)

#Labels

l1 = tk.Label(root,image=img2)
l1.place(x=250,y=150)

l2 = tk.Label(root,text="Find Your Account ?",font=("Arial",20,"bold"),background="#DCDCDC")
l2.place(x=915,y=150)

l3 = tk.Label(root,text="Please enter your Mobile number",font=("Arial",15),background="#DCDCDC")
l3.place(x=890,y=250)

e1 = tk.Entry(master=root)
e1.place(x=860,y=300,height=50,width=400)

l4 = tk.Label(root,text="Please enter your New Password",font=("Arial",15),background="#DCDCDC")
l4.place(x=890,y=360)

e2 = tk.Entry(master=root)
e2.place(x=860,y=410,height=50,width=400)

# l6 = tk.Label(root,text="",background="#DCDCDC")
# l6.place(x=900,y=530)

#Function

def change_pass():
    
    mbl = int(e1.get())
    new_passwd = e2.get()
    
    
    
    query5 = "select Mobile from info where Mobile = %s"
    val = (mbl,)
    c.execute(query5,val)
    data = c.fetchone()
    if data !=None: 
        if not mbl or not new_passwd :
        #  l6.config(text="Please fill all the details..!",fg="red",font=("MS Serif",15,"bold"))
         messagebox.showerror("Mark Mama","Please Fill all the details..!")
         
        elif len(new_passwd) < 8 :
            # l6.config(text="Password contain atleast 8 characters",fg="red",font=("MS Serif",15,"bold")) 
            messagebox.showerror("Mark Mama","Password contain atleast 8 characters..!")
            
        elif new_passwd.isalnum() == True:
            # l6.config(text="Password must contain atleast one special character",fg="red",font=("MS Serif",15,"bold"))
            messagebox.showerror("Mark Mama","Password must contain atleast one special character..!")
        else:
            
            query23 = "update info set Password = %s where Mobile = %s"
            val = (new_passwd,mbl)
            c.execute(query23,val)
            db.commit()
            # l6.config(text="Password changed Successfully..!",fg="green",font=("MS Serif",15,"bold"))
            messagebox.askquestion("Mark Mama","Are you sure ?")
            messagebox.showinfo("Mark Mama","Password Changed SuccessFully")
    else:
        #  l6.config(text="No Account Found.Check Your Number..!",fg="red",font=("MS Serif",15,"bold"))  
         messagebox.showerror("Mark Mama","No Account Found..Check Your Mobile Number..!") 
          
            
            
        
   
    
b1 = tk.Button(root,text="Change Password",fg="white",bg="blue",font=("Arial",10,"bold"),height=2,width=20,command=change_pass)
b1.place(x=980,y=510)

def change_page():
    root.destroy()
    os.system("python tkinter/Facebook_Login.py")
    

b2 = tk.Button(root,text="Go login Page",fg="white",font=("Arial",10,"bold"),bg="green",height=2,width=20,command=change_page)
b2.place(x=980,y=560)


root.mainloop()