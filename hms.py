#IMPORTING REQUIRED MODULES.

from tkinter import *

from tkinter import messagebox

import mysql.connector as sql

#from tkcalendar import Calendar

#CREATING A MAIN WINDOW NAMED WINDOW

window=Tk()
window.configure(bg="#579BB1")

#PROVIDING NAME TO THE WINDOW

window.title("HOSPITAL MANAGEMENT SYSTEM")

#CREATING AN ICON FOR THE WINDOW

i1=PhotoImage(file="C:/Users/theja/OneDrive/Desktop/1.jpg")
window.iconphoto(False,i1)

#PUTTING UP AN H.M.S IMAGE ON THE MAIN WINDOW WHICH WAS CREATED USING PAINT.

i=PhotoImage(file="C:/Users/theja/OneDrive/Desktop/2.jpg")
l=Label(window,image=i)
l.place(x=400,y=0)
    
#CREATING REQUIRED FUNCTIONS.   

def newpatient():
    w=Toplevel(width=1900,height=800)
    
    w.config(bg="#EB455F")

    def insert():
       con=sql.connect(host='localhost',user='root',passwd='Thejas@2005',database='PATIENT')
       cursor=con.cursor()
       q=(
           "insert into patientinfo(PATIENTID,PATIENTNAME,PATIENTAGE,GENDER,HEIGHT,WEIGHT,DISEASE,PHONENUMBER)"
           "values(%s,%s,%s,%s,%s,%s,%s,%s);"
           )
       d=(str(e0.get()),str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get()),str(e5.get()),str(e6.get()),str(e7.get()))
           
       cursor.execute(q,d)
       con.commit()
       con.close()

       messagebox.showinfo("SUCCESSFUL!","PATIENT DETAILS ADDED")

       

    lo=Label(w,text="PATIENT ID",font=("Berlin Sans FB",20),width=15)
    lo.place(x=10,y=10)
    e0=Entry(w,width=50,bd=5)
    e0.place(x=300,y=20)
    
    l1=Label(w,text="NAME",font=("Berlin Sans FB",20),width=15)
    l1.place(x=10,y=80)
    e1=Entry(w,width=50,bd=5)
    e1.place(x=300,y=90)
   
    l2=Label(w,text="AGE",font=("Berlin Sans FB",20),width=15)
    l2.place(x=10,y=150)
    e2=Entry(w,width=50,bd=5)
    e2.place(x=300,y=160)
   
    l3=Label(w,text="GENDER(M/F)",font=("Berlin Sans FB",20),width=15)
    l3.place(x=10,y=220)
    e3=Entry(w,width=50,bd=5)
    e3.place(x=300,y=230)
    
    
    l4=Label(w,text="HEIGHT (in cm)",font=("Berlin Sans FB",20),width=15)
    l4.place(x=10,y=290)
    e4=Entry(w,width=50,bd=5)
    e4.place(x=300,y=300)
    
    
    l5=Label(w,text="WEIGHT (in kg)",font=("Berlin Sans FB",20),width=15)
    l5.place(x=10,y=360)
    e5=Entry(w,width=50,bd=5)
    e5.place(x=300,y=370)
    

    l6=Label(w,text="DISEASE",font=("Berlin Sans FB",20),width=15)
    l6.place(x=10,y=450)
    e6=Entry(w,width=50,bd=5)
    e6.place(x=300,y=460)
    
    
    l7=Label(w,text="PHONE NUMBER",font=("Berlin Sans FB",20),width=15)
    l7.place(x=10,y=520)
    e7=Entry(w,width=50,bd=5)
    e7.place(x=300,y=530)
    
    b6=Button(w,text="SUBMIT",bd=5,font=("Berlin Sans FB",20),command=insert)
    b6.place(x=200,y=600)
    

def showpatient():
    w1=Toplevel(width=1900,height=800)
    w1.config(bg="#FF7B54")

    
    con=sql.connect(host="localhost",user="root",passwd="Thejas@2005",database="patient")
    cursor=con.cursor()
    cursor.execute("select * from patientinfo;")

    
    lo=Label(w1,text="PATIENT ID",font=("Berlin Sans FB",15),width=13,bg="white")
    lo.grid(row=0,column=0)

    
    l1=Label(w1,text="NAME",font=("Berlin Sans FB",15),width=13,bg="white")
    l1.grid(row=0,column=1)

    
    l2=Label(w1,text="AGE",font=("Berlin Sans FB",15),width=13,bg="white")
    l2.grid(row=0,column=2)

    
    l3=Label(w1,text="GENDER(M/F)",font=("Berlin Sans FB",15),width=13,bg="white")
    l3.grid(row=0,column=3)

    
    l4=Label(w1,text="HEIGHT (in cm)",font=("Berlin Sans FB",15),width=13,bg="white")
    l4.grid(row=0,column=4)

    
    l5=Label(w1,text="WEIGHT (in kg)",font=("Berlin Sans FB",15),width=13,bg="white")
    l5.grid(row=0,column=5)

    
    l6=Label(w1,text="DISEASE",font=("Berlin Sans FB",15),width=13,bg="white")
    l6.grid(row=0,column=6)

    
    l7=Label(w1,text="PHONE NUMBER",font=("Berlin Sans FB",15),width=13,bg="white")
    l7.grid(row=0,column=7)

    
    con=sql.connect(host="localhost",user="root",passwd="Thejas@2005",database="patient")
    cursor=con.cursor()
    cursor.execute("select * from patientinfo;")
    
    i=1
    rs=cursor.fetchall()
    
    for patient in rs[1:]:
        for j in range(len(patient)):
            e=Entry(w1,width=25)
            e.grid(row=i,column=j)
            e.insert(0,patient[j])
        i=i+1    

    con.close()


def covid():
    
    w2=Toplevel(width=1900,height=800)
    w2.config(bg="#439A97")

    
    L1=Label(w2,text="1.Stay up to date on vaccination, including recommended booster doses",font=("Berlin Sans FB",18),bg="#439A97")
    L1.place(x=0,y=10)

    
    L2=Label(w2,text="2.Avoid contact with people who have a suspected or confirmed COVID-19 infection.",font=("Berlin Sans FB",18),bg="#439A97")
    L2.place(x=0,y=70)

    
    L3=Label(w2,text="3.Follow recommendations for isolation if you have suspected or confirmed COVID-19 infection.",font=("Berlin Sans FB",18),bg="#439A97")
    L3.place(x=0,y=140)

    
    L4=Label(w2,text="4.Follow the recommendations for what to do if you are exposed to someone with COVID-19.",font=("Berlin Sans FB",18),bg="#439A97")
    L4.place(x=0,y=210)

    
    L5=Label(w2,text="5.Maintain good personal hygiene by washing hands often with soap and water for at least 20 seconds or by using a hand sanitizer.",font=("Berlin Sans FB",18),bg="#439A97")
    L5.place(x=0,y=280)

    
    L6=Label(w2,text="6.If you are at high risk of getting very sick, talk with a healthcare provider about additional prevention actions.",font=("Berlin Sans FB",18),bg="#439A97")
    L6.place(x=0,y=350)


    L7=Label(w2,text="7.Cover your nose and mouth with handkerchief/tissue while sneezing and coughing.",font=("Berlin Sans FB",18),bg="#439A97")
    L7.place(x=0,y=420)


    L8=Label(w2,text="8.Avoid mass gathering and public places.",font=("Berlin Sans FB",18),bg="#439A97")
    L8.place(x=0,y=490)

    

def ms():
    messagebox.showinfo("SUCCESSFUL!","APPOINTMENT SET")


def ms1():
    messagebox.showinfo("SUCCESSFUL!","PATIENT DETAILS DELETED")
    
    
def appoin():
    w3=Toplevel(width=1900,height=800)
    w3.config(bg="#DC3535")
    
    c=Calendar(w3,selectmode="day",year=2022,month=1,day=1)
    c.place(x=300,y=20)
    
    L7=Label(w3,text="PICK A DATE",font=("Berlin Sans FB",20))
    L7.place(x=10,y=20)
    
    
    L8=Label(w3,text="PICK A TIME",font=("Berlin Sans FB",20))
    L8.place(x=10,y=250)

    
    cb1=Checkbutton(w3,text="09:00:00",font=("Berlin Sans FB",10),bd=5,width=10)
    cb1.place(x=365,y=250)

    
    cb2=Checkbutton(w3,text="10:00:00",font=("Berlin Sans FB",10),bd=5,width=10)
    cb2.place(x=365,y=290)

    
    cb3=Checkbutton(w3,text="11:00:00",font=("Berlin Sans FB",10),bd=5,width=10)
    cb3.place(x=365,y=330)

    
    cb4=Checkbutton(w3,text="12:00:00",font=("Berlin Sans FB",10),bd=5,width=10)
    cb4.place(x=365,y=370)

    
    cb5=Checkbutton(w3,text="17:00:00",font=("Berlin Sans FB",10),bd=5,width=10)
    cb5.place(x=365,y=410)

    
    cb6=Checkbutton(w3,text="18:00:00",font=("Berlin Sans FB",10),bd=5,width=10)
    cb6.place(x=365,y=450)

    
    cb7=Checkbutton(w3,text="19:00:00",font=("Berlin Sans FB",10),bd=5,width=10)
    cb7.place(x=365,y=490)

    
    cb8=Checkbutton(w3,text="20:00:00",font=("Berlin Sans FB",10),bd=5,width=10)
    cb8.place(x=365,y=530)

    
    b7=Button(w3,text="SELECT",font=("Berlin Sans FB",20),bd=10,command=ms)
    b7.place(x=365,y=600)


def dele():
    w4=Toplevel(width=1900,height=800)
    w4.config(bg="#2DCDDF")

    
    L7=Label(w4,text="ENTER ID OF PATIENT WHOSE DETAILS HAVE TO BE DELETED",font=("Berlin Sans FB",15))
    L7.place(x=0,y=10)

    
    e8=Entry(w4,bd=5,width=40)
    e8.place(x=600,y=10)

    
    def de():
        con=sql.connect(host="localhost",user="root",passwd="Thejas@2005",database="patient")
        cursor=con.cursor()
        cursor.execute("DELETE from patientinfo WHERE patientid="+e8.get())
        ms1() 
        con.close()

        
    b8=Button(w4,text="SUBMIT",font=("Berlin Sans FB",15),bd=5,command=de)
    b8.place(x=500,y=100)
    
#PLACING REQUIRED BUTTONS ON THE SCREEN.
    
b1=Button(window,text="1. ADD NEW PATIENT DETAILS",font=("Berlin Sans FB",20),bd=10,fg="red",width=40,command=newpatient)
b1.place(x=390,y=200)


b2=Button(window,text="2. DELETE PATIENT DETAILS",font=("Berlin Sans FB",20),bd=10,fg="Red",width=40,command=dele)
b2.place(x=390,y=300)


b3=Button(window,text="3.SHOW ALL PATIENT DETAILS",font=("Berlin Sans FB",20),bd=10,fg="Red",width=40,command=showpatient)
b3.place(x=390,y=400)


b4=Button(window,text="4.FIX APPOINTMENT ",font=("Berlin Sans FB",20),bd=10,fg="Red",width=40,command=appoin)
b4.place(x=390,y=500)


b5=Button(window,text="KNOW COVID-19 PROTOCOLS IN THE PREMISES",font=("Berlin Sans FB",20),bd=10,fg="Red",width=40,command=covid)
b5.place(x=390,y=600)


window.mainloop()
