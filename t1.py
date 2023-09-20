import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import vlc
from os import system
import cv2
import  pandas as pd



engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('XT7YY2-LTE5RTQ4R7')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)

def identify():
    Train_folder="BSc6_train_data"
    Atten_folder = 'BSc Sem 6'
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("train_data/" + Train_folder + "/train.yml")
    df = pd.read_csv(Atten_folder + ".csv")
    print("1")
    cam = cv2.VideoCapture(0)
    Id = 0
    Name = ''
    c=-1
    res = []
    while c<=50 :
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            c=c+1
            cv2.rectangle(frame, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            confidence = int(100 * (1 - conf / 300))
            if (confidence > 70):
                Name = df.loc[df['E_NO'] == Id]['F_Name'].values
                res.append(confidence)
            else:
                res.append(0)

        cv2.imshow("Frame",frame)
        if cv2.waitKey(1)==13:
            break

    cout = 0
    temp =0
    for x in res:
        if x == 0:
            cout = cout + 1
        temp = temp + 1

    if(cout < (temp/2)+1):
        tex_mod= "The Person is "+Name
    else:
        tex_mod="UnKnown face"
    speak(tex_mod)
    print(res)

    cv2.imshow("Frame",frame)
    cam.release()
    cv2.destroyAllWindows()
    cam.release()

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


greetMe()
speak('Hello Sir, I am your digital assistant JAZZ!')
speak('How may I help you?')


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('Sure Sir!')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay sir')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('wait a second sir')
            webbrowser.open('www.gmail.com')
            speak('done')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'mail' in query:
            speak('Who is the recipient? ')
            recipient =  myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = "I am the jazz anas bot its Just For test, Thank You..."

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("7043027540a@gmail.com", 'LoriyaAnas@123')
                    server.sendmail('7043027540a@gmail.com', "anasloriya.info@gmail.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'play music' in query:
            music_folder = 'F://SONGS//'
            list = os.listdir(music_folder)
            os.startfile(os.path.join(music_folder,list[0]))

            speak('Okay, here is your music! Enjoy!')

        elif 'stop music' in query:
            os.system('TASKKILL /F /IM Music.UI.exe')

        elif 'identify the person' in query:
            identify()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=1)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')