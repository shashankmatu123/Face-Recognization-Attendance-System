from pandas import DataFrame
import pandas as pd
import numpy as np
import cv2
import datetime
import time
from tkinter import messagebox

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M')
cam = cv2.VideoCapture(0)
face_clasefier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#--------------------------------------------- Attendance ------------------------------------------------------------

def attendance(Fname,Atten_file):

    Names1 = pd.read_csv('Attendance/'+Atten_file+'/'+Atten_file+'_'+date+'.csv', index_col=0)
    df = DataFrame(Names1, columns=['E_NO','Name', 'Lec 1', 'Lec 2','Lec 3','Lec 4','Lec 5','Lec 6','Lec 7'])

    if(timeStamp>='09:00' and timeStamp<='10:00'):
        df.loc[(df.Name == Fname), 'Lec 1'] = '1'
        df.to_csv('Attendance/'+Atten_file+'/'+Atten_file+'_'+date+'.csv')
    elif(timeStamp>='10:00' and timeStamp<='11:00' ):
        df.loc[(df.Name == Fname), 'Lec 2'] = '1'
        df.to_csv('Attendance/' + Atten_file + '/' + Atten_file + '_' + date + '.csv')
    elif (timeStamp>='11:00' and timeStamp<='12:00'):
        df.loc[(df.Name == Fname), 'Lec 3'] = '1'
        df.to_csv('Attendance/' + Atten_file + '/' + Atten_file + '_' + date + '.csv')
    elif (timeStamp>='12:00' and timeStamp<='14:00'):
        df.loc[(df.Name == Fname), 'Lec 4'] = '1'
        df.to_csv('Attendance/' + Atten_file + '/' + Atten_file + '_' + date + '.csv')
    elif (timeStamp>='14:00' and timeStamp<='15:00'):
        df.loc[(df.Name == Fname), 'Lec 5'] = '1'
        df.to_csv('Attendance/' + Atten_file + '/' + Atten_file + '_' + date + '.csv')
    elif (timeStamp>='15:00' and timeStamp<='16:00'):
        df.loc[(df.Name == Fname), 'Lec 6'] = '1'
        df.to_csv('Attendance/' + Atten_file + '/' + Atten_file + '_' + date + '.csv')




#---------------------------------------------------------- Rocognizer ---------------------------------------------------

def recognize(Train_folder,Atten_folder):
    temp = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # ----------- cv2.createLBPHFaceRecognizer() --------------
    try:
        recognizer.read("train_data/"+Train_folder+"/train.yml")
    except:
        temp = 1
        messagebox.showwarning("Warning",'There is no Train data of '+Atten_folder)

    if temp == 0:#-------------- it check wether the train.yml of specific course is present or not --------------------------
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        df = pd.read_csv(Atten_folder + ".csv")
        font = cv2.FONT_HERSHEY_SIMPLEX
        cam = cv2.VideoCapture(0)
        Id = 0
        Name = ''
        c = 1

        while c <= 200:
            ret, frame = cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)


            for (x, y, w, h) in faces:

                cv2.rectangle(frame, (x, y), (x + w, y + h), (225, 0, 0), 2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                confidence = int(100 * (1 - conf / 300))
                if (confidence > 70):
                    Name = df.loc[df['E_NO'] == Id]['F_Name'].values
                    text = str(Id) + "-" + Name
                else:
                    Id = 'Unknown Face'
                    text = str(Id)

                cv2.putText(frame, str(text), (x, y + h), font, 1, (255, 255, 255), 2)

            cv2.imshow('Frame',frame)
            c = c + 1
            if cv2.waitKey(1)==13:
                break

    #------------------ Function Call of Attendance -------------------------------------
    if temp == 0:
        try:
            attendance(Name[0], Atten_folder)
        except:
            pass
    else:
        pass



#--------------------------- function for creating and checking the attendance sheet is avelable or not --------------------------------------------
def create(Atten_file):
    try:
        df = pd.read_csv('Attendance/'+Atten_file+'/'+Atten_file+'_'+date+'.csv')
    except:
        df = pd.read_csv('Attendance/'+Atten_file+'/'+Atten_file+'.csv')
        df.to_csv('Attendance/'+Atten_file+'/'+Atten_file+'_'+date+'.csv', index=False)

    #messagebox.showinfo('Done','Todays Attendance sheet is created')



#----------------------------------- Test Basic Function -------------------------------------
def test():
    c = 1
    while True:
        if c==1:
            Train_folder = 'BSc1_train_data'
            Atten_folder = 'BSc Sem 1'

            create(Atten_folder)#------ Create Function call for creating the attendance sheet --------------------------
            recognize(Train_folder,Atten_folder)#--------------- recognize function 4 face capture ---------------------------

            cam.release() #_---------- Relese camera -----------------
            cv2.destroyAllWindows() #------------------ Distroy all windows --------------------------------

            print(Atten_folder)

        elif c==2:
            Train_folder = 'BSc2_train_data'
            Atten_folder = 'BSc Sem 2'

            create(Atten_folder)
            recognize(Train_folder, Atten_folder)

            cam.release()
            cv2.destroyAllWindows()

            print(Atten_folder)

        elif c==3:
            Train_folder = 'BSc3_train_data'
            Atten_folder = 'BSc Sem 3'

            create(Atten_folder)
            recognize(Train_folder, Atten_folder)

            cam.release()
            cv2.destroyAllWindows()

            print(Atten_folder)

        elif c==4:
            Train_folder = 'BSc4_train_data'
            Atten_folder = 'BSc Sem 4'

            create(Atten_folder)
            recognize(Train_folder, Atten_folder)

            cam.release()
            cv2.destroyAllWindows()

            print(Atten_folder)

        elif c==5:
            Train_folder = 'BSc5_train_data'
            Atten_folder = 'BSc Sem 5'

            create(Atten_folder)
            recognize(Train_folder, Atten_folder)

            cam.release()
            cv2.destroyAllWindows()

            print(Atten_folder)

        elif c==6:
            Train_folder = 'BSc6_train_data'
            Atten_folder = 'BSc Sem 6'

            create(Atten_folder)
            recognize(Train_folder, Atten_folder)

            cam.release()
            cv2.destroyAllWindows()

            print(Atten_folder)

        elif c==7:
            Train_folder = 'MSc1_train_data'
            Atten_folder = 'MSc Sem 1'

            create(Atten_folder)
            recognize(Train_folder, Atten_folder)

            cam.release()
            cv2.destroyAllWindows()

            print(Atten_folder)

        elif c==8:
            Train_folder = 'MSc2_train_data'
            Atten_folder = 'MSc Sem 2'

            create(Atten_folder)
            recognize(Train_folder, Atten_folder)

            cam.release()
            cv2.destroyAllWindows()

            print(Atten_folder)

        elif c==9:
            Train_folder = 'MSc3_train_data'
            Atten_folder = 'MSc Sem 3'

            create(Atten_folder)
            recognize(Train_folder, Atten_folder)

            cam.release()
            cv2.destroyAllWindows()

            print(Atten_folder)

        elif c==10:
            Train_folder = 'MSc4_train_data'
            Atten_folder = 'MSc Sem 4'

            create(Atten_folder)
            recognize(Train_folder, Atten_folder)

            cam.release()
            cv2.destroyAllWindows()

            print(Atten_folder)

        else:

            break

        c = c + 1



class recog_atten:
    def __init__(self):

        test() #----------------- 1st Test function call -----------------------
