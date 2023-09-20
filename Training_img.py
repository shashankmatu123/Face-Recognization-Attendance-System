import cv2
import os
import numpy as np
from tkinter import messagebox

recognizer = cv2.face.LBPHFaceRecognizer_create()
def Training(path,Spath):
    imagepath = [os.path.join(path, f) for f in os.listdir(path)]

    try:
        faces = []
        ids = []

        id = 0
        for imagepaths in imagepath:
            images = cv2.imread(imagepaths, cv2.IMREAD_GRAYSCALE)
            facenp = np.asarray(images, dtype=np.uint8) #---------------- converting face into numpy array ---------------------
            id = int(os.path.split(imagepaths)[-1].split('.')[1]) #----------------------- split the Eno and store into Id variable --------------------------
            faces.append(facenp)
            ids.append(id)
            cv2.imshow('face', facenp)
            cv2.waitKey(10)

        recognizer.train(faces, np.array(ids))
        recognizer.save(Spath + 'train.yml')

        messagebox.showinfo("Success", "train done.....!!!!!!!")
        cv2.destroyAllWindows()
    except:
        messagebox.showwarning('Warning','There Is No Images in Folder')




class Training_img:

    def __init__(self,path,spath):
        self.path = path
        self.spath = spath

        Training(path,spath)

