import pandas as pd
from tkinter import messagebox

b1 = 'BSc Sem 1'
b2 = 'BSc Sem 2'
b3 = 'BSc Sem 3'
b4 = 'BSc Sem 4'
b5 = 'BSc Sem 5'
b6 = 'BSc Sem 6'
m1 = 'MSc Sem 1'
m2 = 'MSc Sem 2'
m3 = 'MSc Sem 3'
m4 = 'MSc Sem 4'


def insert(Eno,Fname,Mname,Lname,File_Name):

    #----------------- Reading the Files -----------------------
    df = pd.read_csv(File_Name + '.csv')
    df2 = pd.read_csv('Attendance/'+File_Name+'/'+File_Name+'.csv')

    #----------------- creating column heading for attendace sheet --------------------------------------
    Atn_col = ['E_NO', 'Name', 'Lec 1', 'Lec 2', 'Lec 3', 'Lec 4', 'Lec 5', 'Lec 6', 'Lec 7']
    Atn = pd.DataFrame(df2, columns= Atn_col)

    #--------------------- creating column for information sheet --------------------------------
    col_names = ['E_NO', 'F_Name' , 'M_Name' , 'L_Name']
    info = pd.DataFrame(df, columns=col_names)

    #------------------------ inserting value to the information sheet ---------------------------
    info.loc[len(info)] = [Eno, Fname, Mname, Lname]
    info = info.drop_duplicates(subset=['E_NO'], keep='first') #---- Check the the entry of duplication of data on base of E_No

    #------------------------------- inserting value to the the attendance sheet ----------------------------------
    Atn.loc[len(Atn)] = [Eno, Fname, 0, 0, 0, 0, 0, 0, 0]
    Atn = Atn.drop_duplicates(subset=['E_NO'], keep='first')#---- Check the the entry of duplication of data on base of E_No

    #---------------- SAVING the data to the .csv file ------------------------------
    info.to_csv(File_Name+'.csv', index=False)  #----- to info sheet
    messagebox.showinfo("Succesfull", "Student Information is inster into Information Sheet")

    Atn.to_csv('Attendance/'+File_Name+'/'+File_Name+'.csv', index=False) #------- To attendance sheet
    messagebox.showinfo("Succesfull","Student Information is inster into Attendance Sheet")



#--------------- Check For the insterted course and semester ---------------------------------------
def test(Eno,Fname,Mname,Lname,Course,Semester):

    if Course == " BSc " and Semester == "1":
        file_name = b1
        insert(Eno, Fname, Mname, Lname, file_name)

    elif Course == " BSc " and Semester == "2":
        file_name = b2
        insert(Eno, Fname, Mname, Lname, file_name)

    elif Course == " BSc " and Semester == "3":
        file_name = b3
        insert(Eno, Fname, Mname, Lname, file_name)

    elif Course == " BSc " and Semester == "4":
        file_name = b4
        insert(Eno, Fname, Mname, Lname, file_name)

    elif Course == " BSc " and Semester == "5":
        file_name = b5
        insert(Eno, Fname, Mname, Lname, file_name)

    elif Course == " BSc " and Semester == "6":
        file_name = b6
        insert(Eno, Fname, Mname, Lname, file_name)

    elif Course == " MSc " and Semester == "1":
        file_name = m1
        insert(Eno, Fname, Mname, Lname, file_name)

    elif Course == " MSc " and Semester == "2":
        file_name = m2
        insert(Eno, Fname, Mname, Lname, file_name)

    elif Course == " MSc " and Semester == "3":
        file_name = m3
        insert(Eno, Fname, Mname, Lname, file_name)

    elif Course == " MSc " and Semester == "4":
        file_name = m4
        insert(Eno, Fname, Mname, Lname, file_name)






class ins_stud_info:
    def __init__(self,Eno,Fname,Mname,Lname,Course,Semester):
        self.Eno = Eno
        self.Fname = Fname
        self.Mname = Mname
        self.Lname = Lname
        self.Course = Course
        self.Semester = Semester

        test(Eno,Fname,Mname,Lname,Course,Semester)

