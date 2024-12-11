#<<<<<<------------ SIGN UP PAGE ----------->>>>>>>>>>

#Libaries

import tkinter as tk
from PIL import Image,ImageTk
import os
import mysql.connector
from tkinter import messagebox

#Mysql Connection

db = mysql.connector.connect(host="localhost",user="navaneesh",password="nana111",port="3307",db="facebook")
c = db.cursor()

#Tkinter

root = tk.Tk()

img = Image.open("tkinter/facebook2.png")
resize = img.resize((350,200))
img2 = ImageTk.PhotoImage(image=resize)

#Labels
f1 = tk.Frame(master=root,width=600,height=1200,background="#DCDCDC")
f1.place(x=541,y=0)


l1 = tk.Label(root,image=img2,background="#DCDCDC")
l1.place(x=660,y=0)

l2 = tk.Label(root,text="Create A New Account",font=("Arial",20,"bold"),background="#DCDCDC")
l2.place(x=680,y=200)

l3 = tk.Label(root,text="It's Quick And Easy",font=("Arial",15),background="#DCDCDC")
l3.place(x=740,y=250)

l4 = tk.Label(root,text="Name\t:",font=("Arial",15),background="#DCDCDC")
l4.place(x=680,y=330)

l5 = tk.Label(root,text="Sex\t:",font=("Arial",15),background="#DCDCDC")
l5.place(x=680,y=380)

l6 = tk.Label(root,text="Mobile\t:",font=("Arial",15),background="#DCDCDC")
l6.place(x=680,y=430)

l7 = tk.Label(root,text="Password :",font=("Arial",15),background="#DCDCDC")
l7.place(x=680,y=480)

l8 = tk.Label(root,text="People who use our service may have uploaded your contact information to Facebook. Learn more.",font=("Arial",10),background="#DCDCDC")
l8.place(x=550,y=550)

l9 = tk.Label(root,text="By clicking Sign Up, you agree to our Terms, Privacy Policy and Cookies Policy.",font=("Arial",10),background="#DCDCDC")
l9.place(x=600, y=600)

#Entry

e1 = tk.Entry(root)
e1.place(x=785,y=330,height=35,width=200)

e2 = tk.Entry(root)
e2.place(x=785,y=380,height=35,width=200)

e3 = tk.Entry(root)
e3.place(x=785,y=430,height=35,width=200)

e4 = tk.Entry(root)
e4.place(x=785,y=480,height=35,width=200)

#Function

def signup():
    name   = e1.get()
    sex    = e2.get()
    mobile = e3.get()
    passwd = e4.get()
    
    query2 = "select Mobile from info where Mobile = %s"
    
    val = (mobile,)
   
    c.execute(query2,val)
    
    data = c.fetchone()
    
    if not name or not sex or not mobile or not passwd:
        # l10.config(text="Please fill above all details",fg="red",font=("MS Serif",10,"bold")) 
        messagebox.showerror("Mark Mama","Please fill above all details..!")  
        
    elif name.isalnum() == False:
        # l10.config(text="Name field not allow special characters",fg="red",font=("MS Serif",10,"bold"))
        messagebox.showerror("Mark Mama","Name field not allow special characters..!")  
        
    elif sex.lower() not in ("male","female"):
        # l10.config(text="Please enter correct sex details",fg="red",font=("MS Serif",10,"bold"))
        messagebox.showerror("Mark Mama","Please enter correct sex details..!")  
        
    elif len(mobile) > 10 or len(mobile) < 10 :    
        # l10.config(text="Please enter correct Mobile number",fg="red",font=("MS Serif",10,"bold"))
        messagebox.showerror("Mark Mama","Please enter correct Mobile number..!")  
        
    elif mobile.isnumeric() == False:    
        # l10.config(text="Please enter correct Mobile number",fg="red",font=("MS Serif",10,"bold")) 
         messagebox.showerror("Mark Mama","Please enter correct Mobile number..!")   
        
    elif len(passwd) < 8 :
        # l10.config(text="Password contain atleast 8 characters",fg="red",font=("MS Serif",10,"bold")) 
         messagebox.showerror("Mark Mama","Password contain atleast 8 characters..!")  
        
    elif passwd.isalnum() == True:
        # l10.config(text="Password must contain atleast one special character",fg="red",font=("MS Serif",10,"bold"))
        messagebox.showerror("Mark Mama","Password must contain atleast one special character..!")  
        
    else:
    
        if data == None :  
            query = "insert into info values(%s,%s,%s,%s)"
            val = (name,sex,mobile,passwd)
            c.execute(query,val)
            db.commit()
            # l10.config(text="Congratulations..! Your Account Created Succesfully",fg="Green",font=("MS Serif",10,"bold")) 
            messagebox.showinfo("Mark Mama","Congratulations..! Your Account Created Succesfully..!")          
        else:
            #  l10.config(text="This Number already have an Account",fg="red",font=("MS Serif",10,"bold"))  
             messagebox.showerror("Mark Mama","This Number already have an Account...!")       
          
     
#Button

b1 = tk.Button(root,text="Sign Up",font=("Arial",12,"bold"),fg="white",bg="#66CD00",bd=0,width=20,height=2,command=signup)
b1.place(x=730,y=655)

def login():
    root.destroy()
    os.system("python tkinter/Facebook_Login.py")

b2 = tk.Button(root,text="Go Login Page",font=("Arial",12,"bold"),fg="white",bg="blue",bd=0,width=20,height=1,command=login)
b2.place(x=730,y=730)

# l10 = tk.Label(root,text="",background="#DCDCDC")
# l10.place(x=680,y=700)


root.mainloop()
