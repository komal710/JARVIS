from tkinter import *
from PIL import ImageTk, Image


import pyttsx3
import wikipedia 
import os
import datetime
#import smtplib
import speech_recognition as sr 
#from playsound import playsound
import webbrowser
import pyjokes
import psutil
import pyautogui

print("JARVIS IS STARTING")
mam = "KOMAL"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Madam")
    
    
    speak("JARVIS at your service. Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    
        print(f"User Said:{query}\n")

    except Exception as e:
        print(e)
        speak("Sorry, say that again please"+mam)
        return "None"

    return query    


def screenshot():
    img = pyautogui.screenshot()
    img.save("F:\komal\vscode\image.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CUP is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())



class Widget:
    def __init__(self):
    

        root=Tk()

        root.title('Assistant')
        root.geometry('1680x1050')

        image = Image.open("F:\\komal\\vscode\\image.jpg")

        image = image.resize((550, 870), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(image)
        my_lbl = Label(image = my_img)
        my_lbl.pack(side='right',fill='both', expand='no')

        self.compText = StringVar()
        self.userText = StringVar()
        self.userText.set('Click Run JARVIS to give command')

        userFrame = LabelFrame(root,text="user",font=('Black ops one',10,'bold'))
        userFrame.pack(fill='both',expand='yes')
        left = Message(userFrame, textvariable=self.userText , bg= '#3B3B98', fg='white')
        left.config(font=("Century Gothic",24,'bold'))
        left.pack(fill='both', expand='yes')

        compFrame=LabelFrame(root, text="Jarvis", font=('Black ops one',10,'bold'))
        compFrame.pack(fill='both',expand='yes')
        left2 = Message(compFrame, textvariable=self.compText , bg= '#3B3B98', fg='white')
        left2.config(font=("Century Gothic",24,'bold'))
        left2.pack(fill='both', expand='yes')

        self.compText.set('Hello I am JARVIS, What I can do for you?')

        btn=Button(root,text='Run JARVIS',  font=('Calibri',30,'bold'),bg='#4B4B4B', fg='white',command=self.clicked ).pack(fill='x',expand='no')
        btn2=Button(root,text='Close', font=('Calibri',30,'bold'),bg='#4B4B4B', fg='white',command=root.destroy).pack(fill='x',expand='no')


        root.mainloop()

    def clicked(self):
        print("Working...")
        query = takeCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        

        while True:
            query = takeCommand().lower()

            if 'open youtube' in query:
                speak("Alright, opening youtube")
                url = "youtube.com"
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open(url)

            elif 'play songs' in query:
                speak("Alright, here is some music for you")
                songs_dir = 'F:\\komal\\vscode\\music'
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))
            elif 'time' in query:
                time()
            
            elif 'date' in query:
                date()
            elif 'wikipedia' in query:
                speak("Searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query)
                print(result)
                speak(result)
        
            elif 'search in chrome' in query:
                speak("What should i search ?")
                chrome_path = ''
                search = takeCommand().lower()
                webbrowser.get(chrome_path).open_new_tab(search+'.com')
            elif 'logout' in query:
                os.system("shutdown -1")
            
            elif 'shutdown' in query:
                os.system("shutdown /s /t 1")
            
            elif 'restart' in query:
                os.system("shutdown /r /t 1")
            
            elif 'remember that' in query:
                speak("what should i remember?")
                data = takeCommand()
                speak("you said me to remember that"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            elif 'do you know anything' in query:
                remember = open('data.txt','r')
                speak("you said me to remember that" +remember.read())
            elif 'screenshot' in query:
                screenshot()
                speak("Done!")
            elif 'cpu' in query:
                cpu()
            elif 'joke' in query:
                jokes()

            elif 'offline' in query:
                speak("Bye Bye Madam")

                hour = datetime.datetime.now().hour
                if hour>=6 and hour <12:
                    speak("Good Morning Madam. Have a nice day")
                    quit()
                elif hour>=12 and hour<16:
                    speak("Good Day Madam")
                    quit()
                
                elif hour>=16 and hour<21:
                    speak("Hope you have a great evening"+mam)
                    quit()
                    
                else:
                    speak("Have a good night Madam. Sleep Tight.")
                    quit()


if __name__ == '__main__':
    speak('INITIALIZING JARVIS')
    wishme()
    widget = Widget()
    