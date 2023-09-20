from tkinter import *
import tkinter as tk
from tkinter import messagebox
import cv2
import numpy as np
import os
import csv
import pandas
#------------- Importing the inster stud info program ------------------
from ins_stud_info import *
#------ importing the capture program -----------------------------
from sub_cap import *
#-------------------------------importing the Trainig program ----------------------------
from Training_img import *
#------------------------------ importing recognition $ attendance program -----------------------
from recog_atten import *


face_clasefier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#-------------------- Capture Class -------------------------
class capture:
    def captr(self):
        Eno = eno.get()
        Fname = fname.get()
        Mname = mname.get()
        Lname = lname.get()
        Course = course.get()
        Semester = semester.get()

        print(Eno,Fname,Course,Semester)
        if(Eno=="" or Fname=="" or Mname=="" or Lname=="" or Course=="  " or Semester=="  "):
            messagebox.showerror("Error","Fill all the Student information")
        else:
            if Course==" MSc " and int(Semester)>4: #---------------------- MSc Semester validation -------------------------
                messagebox.showerror("Error", "Select the << MSC >> Semester Between <<< 1 To 4 >>> ")
            else:
                # -------------- insert program to insert into info.csv and attendance folder ------------------------
                ins_stud_info(Eno,Fname,Mname,Lname,Course,Semester)
                # ------ Sub_cap program -------- for capturing--------------
                sub_cap(Course, Semester, Fname, Eno)
                root.quit()





#-------------------------------------- Train the image --------------------------

class train:
    def trn(self):
        Course = course.get()#////////////////// get the student Course ---------------
        Semester = semester.get()#****************Get the Semeter of the student ---------------------

        #-------- Geting the path to train the spacific data -------------------------------------
        if Course == " BSc " and Semester == "1":
            path = 'D:/face recognization/face_prg/BSc Sem 1/'
            spath = 'D:/face recognization/face_prg/train_data/'
            Training_img(path, Spath) #----- Training Program -----------

        elif Course == " BSc " and Semester == "2":
            path = 'D:/face recognization/face_prg/BSc Sem 2/'
            Spath = 'D:/face recognization/face_prg/train_data/'
            Training_img(path, Spath) #----- Training Program -----------

        elif Course == " BSc " and Semester == "3":
            path = 'D:/face recognization/face_prg/BSc Sem 3/'
            Spath = 'D:/face recognization/face_prg/train_data/'
            Training_img(path, Spath) #----- Training Program -----------

        elif Course == " BSc " and Semester == "4":
            path = 'D:/face recognization/face_prg/BSc Sem 4/'
            Spath = 'D:/face recognization/face_prg/train_data/'
            Training_img(path, Spath) #----- Training Program -----------

        elif Course == " BSc " and Semester == "5":
            path = 'D:/face recognization/face_prg/BSc Sem 5/'
            Spath = 'D:/face recognization/face_prg/train_data/'
            Training_img(path, Spath) #----- Training Program -----------

        elif Course == " BSc " and Semester == "6":
            path = 'D:/face recognization/face_prg/BSc Sem 6/'
            Spath = 'D:/face recognization/face_prg/train_data/'
            Training_img(path, Spath) #----- Training Program -----------

        elif Course == " MSc " and Semester == "1":
            path = 'D:/face recognization/face_prg/MSc Sem 1/'
            Spath = 'D:/face recognization/face_prg/train_data/MSc1_train_data/'
            Training_img(path, Spath)  #----- Training Program -----------

        elif Course == " MSc " and Semester == "2":
            path = 'D:/face recognization/face_prg/MSc Sem 2/'
            Spath = 'D:/face recognization/face_prg/train_data/MSc1_train_data/'
            Training_img(path, Spath)  #----- Training Program -----------

        elif Course == " MSc " and Semester == "3":
            path = 'D:/face recognization/face_prg/MSc Sem 3/'
            Spath = 'D:/face recognization/face_prg/train_data/MSc1_train_data/'
            Training_img(path, Spath)  #----- Training Program -----------

        elif Course == " MSc " and Semester == "4":
            path = 'D:/face recognization/face_prg/MSc Sem 4/'
            Spath = 'D:/face recognization/face_prg/train_data/MSc1_train_data/'
            Training_img(path, Spath)  #----- Training Program -----------

        else:
            #------------------------- Creating error is Course Or sem is not selected ---------------------------------
            messagebox.showerror("Error","First Select the Course And Semester")




#--------------------------------------------- Face Recognization -------------------------------------------------
class recog:
    def recognition(self):

        recog_atten()


# --------------------- Class Object ---------------------------------
c = capture()
t = train()
r = recog()

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#----------------- Designoing Part -------------------------------------

root = Tk()
root.title("Face RecogniZation")
root.geometry("1340x700+10+10")


lb1 = Label(root, text="Welcom To the Face Recognization Project",fg="Blue",font=("",35,"bold","italic"),bg="white").pack(fill=X)
lb2 = Label(root, text="Student Details : ",font=("",30,"bold"),fg="darkblue").place(x=20,y=70)

#------------------first Name---------------------
lb3 = Label(root, text="First Name - ",font=("",25,"bold"),fg="darkblue").place(x=85,y=150)
fname= StringVar()
entry1=Entry(root, textvariable=fname,width=30,font=("",18,"bold"),bg="lightgreen").place(x=290,y=160)
#-----------------Middle Name-----------------------
lb4 = Label(root, text="Middle Name - ",font=("",25,"bold"),fg="darkblue").place(x=50,y=200)
mname= StringVar()
entry2=Entry(root, textvariable=mname,width=30,font=("",18,"bold"),bg="lightgreen").place(x=290,y=210)

#----------------Last Name-------------------------
lb5 = Label(root, text="Last Name - ",font=("",25,"bold"),fg="darkblue").place(x=85,y=250)
lname= StringVar()
entry3=Entry(root, textvariable=lname,width=30,font=("",18,"bold"),bg="lightgreen").place(x=290,y=260)

#-------------------Enrolment No--------------------
lb6 = Label(root, text="Enrolment No - ",font=("",25,"bold"),fg="darkblue").place(x=35,y=320)
eno= StringVar()
entry4=Entry(root, textvariable=eno,width=30,font=("",18,"bold"),bg="lightgreen").place(x=290,y=330)



#----------------------------------------Course Name------------------------------------------
lb6 = Label(root, text="Course - ",font=("",25,"bold"),fg="darkblue").place(x=135,y=385)
OPTIONS = [
"  ",
" BSc ",
" MSc "
]
course = StringVar(root)
course.set(OPTIONS[0])
set = OptionMenu(root, course, *OPTIONS)
set.configure(font=("",15,"bold"),bg="blue",fg="white",width=10)
set.place(x=290,y=390)

#---------------------Semester----------------------
lb7= Label(root, text="Semester -", font=("",25,"bold"),fg="darkblue").place(x=100,y=440)
semester = StringVar(root)

OPTIONS = [
"  ",
"1","2","3","4","5","6"
]
semester = StringVar(root)
semester.set(OPTIONS[0])

set = OptionMenu(root, semester, *OPTIONS)
set.configure(font=("",15,"bold"),bg="blue",fg="white",width=10)
set.place(x=290,y=445)

#------------------------------------ SHOW * -------------------------------------------------------

temp = 40
for x in range (1,21,1):
    temp = temp +30
    Label(root, text=" * ", font=("",30,"bold"),fg="darkblue").place(x=825,y= temp)

#--------------------------************* Buttons *******************------------------------
drw1 = Label(root, text=" V ", font=("",30,"bold"),fg="darkblue").place(x=1105,y=80)
stp1 = Label(root, text=" Step 1", font=("",27,"bold"),fg="darkblue").place(x=1070,y=120)
btn1 = Button(root, text="<< Submit & Capture >> ", width=20 , height=2 , bg="green" , fg="white" , font=("",12,"bold") , command=c.captr).place(x=1030,y=175)

drw2 = Label(root, text=" V ", font=("",30,"bold"),fg="darkblue").place(x=1105,y=260)
stp2 = Label(root, text=" Step 2", font=("",27,"bold"),fg="darkblue").place(x=1070,y=300)
btn2 = Button(root, text="<< Train Data >>" , width=20 , height=2 , bg="blue" , fg="silver" , font=("",12,"bold") , command=t.trn ).place(x=1030,y=355)

drw3 = Label(root, text=" V ", font=("",30,"bold"),fg="darkblue").place(x=1105,y=450)
stp3 = Label(root, text=" Step 3", font=("",27,"bold"),fg="darkblue").place(x=1070,y=490)
btn3 = Button(root, text="<< Recognization >>" , width=20 , height=2 , bg="purple" , fg="white" , font=("",12,"bold") , command= r.recognition ).place(x=1030,y=540)

root.mainloop()
