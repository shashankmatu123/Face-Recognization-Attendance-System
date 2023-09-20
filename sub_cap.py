import cv2
import csv
from tkinter import messagebox


face_clasefier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def capture(Course,Semester,Fname,Eno):
    #cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_clasefier.detectMultiScale(gray, 1.3, 5)

        if faces is ():
            print("face Not Found")
        else:
            for (x, y, w, h) in faces:
                crop_face = gray[y:y + h, x:x + w]

            face = cv2.resize(crop_face, (400, 300))

            # ------------------------------------------------ Folder Validation check ----------------------------------------------------------

            if (Course == " BSc " and Semester == "1"):  # ****************** checking the student cousre to save in that folder --------------------

                for (x, y, w, h) in faces:
                    count += 1
                    file_path = "E:/python/face_prg/BSc Sem 1/" + str(Fname) + str(count) + "." + str(Eno) + ".jpg"
                    cv2.imwrite(file_path, face)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # cv2.waitKey(100)
                if cv2.waitKey(1) == 13 or count == 20:
                    count = 0
                    break
            elif Course == " BSc " and Semester == "2":

                for (x, y, w, h) in faces:
                    count += 1
                    file_path = "E:/python/face_prg/BSc Sem 2/" + str(Fname) + str(count) + "." + str(Eno) + ".jpg"
                    cv2.imwrite(file_path, face)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                if cv2.waitKey(1) == 13 or count == 20:
                    count = 0
                    break
            elif Course == " BSc " and Semester == "3":

                for (x, y, w, h) in faces:
                    count += 1
                    file_path = "E:/python/face_prg/BSc Sem 3/" + str(Fname) + str(count) + "." + str(Eno) + ".jpg"
                    cv2.imwrite(file_path, face)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                if cv2.waitKey(1) == 13 or count == 20:
                    count = 0
                    break
            elif Course == " BSc " and Semester == "4":

                for (x, y, w, h) in faces:
                    count += 1
                    file_path = "E:/python/face_prg/BSc Sem 4/" + str(Fname) + str(count) + "." + str(Eno) + ".jpg"
                    cv2.imwrite(file_path, face)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                if cv2.waitKey(1) == 13 or count == 20:
                    count = 0
                    break
            elif Course == " BSc " and Semester == "5":

                for (x, y, w, h) in faces:
                    count += 1
                    file_path = "E:/python/face_prg/BSc Sem 5/" + str(Fname) + str(count) + "." + str(Eno) + ".jpg"
                    cv2.imwrite(file_path, face)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                if cv2.waitKey(1) == 13 or count == 20:
                    count = 0
                    break
            elif Course == " BSc " and Semester == "6":

                for (x, y, w, h) in faces:
                    count += 1
                    file_path = "E:/python/face_prg/BSc Sem 6/" + str(Fname + "." + Eno) + "." + str(count) + ".jpg"
                    cv2.imwrite(file_path, face)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                if cv2.waitKey(1) == 13 or count == 20:
                    count = 0
                    break

            cv2.imshow('frame', frame)
    count = 0
    messagebox.showinfo("Success","image Capturing is Done..!!!")
    cap.release()
    cv2.destroyAllWindows()
    distroy()

def distroy():
    cap.release()
    cv2.destroyAllWindows()





class sub_cap:

    def __init__(self,course,semester,fname,eno):
        self.course = course
        self.semester = semester
        self.fname = fname
        self.eno = eno

        capture(course,semester,fname,eno)
