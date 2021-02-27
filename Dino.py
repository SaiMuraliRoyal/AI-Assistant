import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil #pip insall psutil
import pyjokes #pip install pyjokes
import os
import pyautogui #pip install puautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha


engine = pyttsx3.init() #initialising
wolframalphaID = 'UPH5WW-424R87YXPP'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I :%M: %S") #for 12-hour format
    #Time = datetime.datetime.now().strftime("%H :%M: %S") for 24-hour format
    speak("The current time is : ")
    speak(Time)


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak('The current date is:')
    speak(date)
    speak(month)
    speak(year)

def dino():
    speak("I am dyno 1.O , I was created by M Sai Murali on Feb 27 2021, I am created such a way that you won't need to work with your hands anymore")

def greeting():
    speak("Welcome to the hand free world , i am dyno")
    time()
    date()

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<24:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("Dyno is at your service, How can i help you today")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()


    server.login("Sender\'s Email",'Password')
    sever.sendmail("Senders Email" , to,contetnt)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    print(usage)
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    print(battery)
    speak("Battery of the system is")
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/Sai Murali Royal/Desktop/screenshot.png')    

def command():
    l = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        l.pause_threshold = 1 
        audio = l.listen(source)
    
    try:
        print("Decoding.................")
        query = l.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Can you please come again")
        return "None"
    return query

if __name__ == "__main__":

    greeting()

    while True:
        query = command().lower()

        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()

        elif 'wikipedia' in query :
            speak("Searching......")
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)
        
        elif 'who is' in query:
            query = query.replace('who is', '')
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)


        elif "send email" in query:
            try:
                speak("What is the content")
                content = command()
                speak("Whom do you want to send")
                reciever = input("Enter the recievers mail address")
                #reciever = '991900434@klu.ac.in'
                to = reciever
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to complete the process")

        elif 'search in browser' in query:
            speak("What should i search for you")
            chromepath = 'C:/Users/Sai Murali Royal/AppData/Local/Vivaldi/Application/vivaldi.exe %s'

            search = command().lower()
            wb.get(chromepath).open_new_tab(search+'.com')


        elif "search in youtube" in query:
            speak("What do you want to see or listen?")
            ytsearch = command().lower()
            speak('You will be in youtube in few seconds!!')
            wb.open("https://www.youtube.com/results?search_query="+ytsearch)
        
        
        elif "search in google" in query:
            speak("What would you like to know about?")
            gsearch = command().lower()
            speak("Searching......")
            wb.open('https://www.google.com/search?q='+gsearch)

        elif 'cpu' in query:
            cpu()

        elif "joke" in query:
            joke()
        
        elif "exit" in query:
            speak("Going Offline")
            quit()
        
        elif 'word' in query:
            speak("Opening MS Word.....")
            msword = r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
            os.startfile(msword)
        
        elif 'write a note' in query:
            speak("What would you like to write??")
            notes = command()
            file = open('note.txt','w')
            speak('Would you like to include Date and Time?')
            ans = command()
            if 'yes' in ans or 'sure' in ans:
                tme = datetime.datetime.now().strftime("%H :%M: %S")
                file.write(tme)
                file.write(':-')
                file.write(notes)
                speak("Notes Added Successfully")
            else:
                file.write(notes)
                speak("Notes Added Successfully")
            
        elif 'show notes' in query:
            speak("Opeining Notes")
            file = open('note.txt','r')
            print(file.read())
            speak(file.read())
        
        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query:
            songs_dir = 'C:/Users/Sai Murali Royal/Music'
            music = os.listdir(songs_dir)
            speak("What would you like to listen????")
            speak("Select a number...")
            ans = command().lower()
            
            if 'number' in ans:
                n = int(ans.replace('number',''))
            elif 'random' or 'choose' in ans:
                n = random.randint(1,15)
            os.startfile(os.path.join(songs_dir,music[n]))


        elif 'play videos' in query:
            videos_dir = 'C:/Users/Sai Murali Royal/Videos'
            video = os.listdir(videos_dir)
            speak("What would you like to experiance????")
            speak("Select a number...")
            ans = command().lower()
            
            if 'number' in ans:
                n = int(ans.replace('number',''))
            elif 'random' or 'choose' in ans:
                n = random.randint(1,20)
            os.startfile(os.path.join(videos_dir,video[n]))    
        
        
        elif 'remember that' in query:
            speak("What should i remember??")
            reminder = command()
            speak("I'll make you remember that"+reminder)
            remind = open('reminder.txt','w')
            remind.write(reminder)
            reminder.close()

        elif 'do i have any reminders' in query:
            remind = open("reminder.txt",'r')
            speak("I had remembered that "+remind.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=2bfbafa5088b4fb19b79ff9b67a6dee0")
                data = json.load(jsonObj)
                i=1

                speak("Here the top headlines from the entertainment field")
                print("-----------TOP HEADLINES----------------------")
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
             
            except Exception as e: 
                print(str(e))
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("You asked me to locate"+location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalphaID)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx+1:]
            rs = client.query(" ".join(query))
            answer = next(rs.results).text
            print("The answer is "+ answer)
            speak("The answer is "+ answer)

        elif "what is" in query: 

            client = wolframalpha.Client(wolframalphaID)
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("Not found what you wanted")
        
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening your commands")
            s = int(command())
            time.sleep(s)
            print(s)
            speak("I'm going to sleep")

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'shutdowm' in query:
            os.system('shutdown /s /t 1')

        elif 'who is owner' in query or 'created' in query:
            dyno()

        elif 'love' in query:
            speak("Love is a 7th sense that destry all other senses,"
            "Be aware of love"
            "love is injurious to health"
            "simply love is a waste of time")

        else:
            speak("come again my friend")

        
