import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import pyjokes
import pyautogui
import psutil
import translate
import requests
from bs4 import BeautifulSoup
import json # location
import geocoder
import instaloader
import PyPDF2
import operator
import speedtest



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    if hour>=0 and hour<12:
        speak(f"Good Morning! Sir, its {strTime} AM in morning")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon! Sir, its {strTime} PM in mid day")   

    else:
        speak(f"Good Evening! Sir, its {strTime} PM in end day")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 600
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ashumissra1@gmail.com', 'my-pass')
    server.sendmail('ashumissra1@gmail.com', to, content)
    server.close()

def joke():
    for i in range(2):
        speak(pyjokes.get_jokes()[i])

def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = str(soup.find_all(attrs={"itemprop": "headline"}))
    headlines1 = soup.find_all(attrs={"itemprop": "headline"})
    headlines=headlines.replace('<span itemprop="headline">',"  ,  ")
    headlines=headlines.replace("</span>","   ,   ")
    
    for headline in headlines1:
        print(headline.text)
    speak(headlines)

def pdf_reader():
    book=open("E:\STUDY COLLEGE\Discrete Structures & Theory of Logic.pdf","rb")
    pdfReader=PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"there are total of {pages} pages enter page no  which one i should read")
    pg= int(input("Enter Page No. :"))
    page= pdfReader.getPage(0)
    text= page.extractText()
    print(text)
    speak(text)


if __name__ == "__main__":
    wishMe()
    while True:
       
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'E:\\MOVIES'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                to ="paritoshmishra9999@gmail.com"
                speak("what should i say?")   
                content =takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")    
        
        elif 'anuj' in query:
            speak("hlo buddy i know you you are a kutta and suar")

        elif 'bye' in query or 'exit' in query or 'go to sleep' in query or 'stop' in query or 'quit' in query:
            speak("good bye")
            exit() 

        elif 'hello' in query or 'hi' in query:
            print("Hi , ask your work don't waste my time")
            speak("Hi , ask your work don't waste my time")

        elif "who are you" in query or "about you" in query or "your detail" in query or 'explain yourself' in query:
            about = "I am Jarvis an Python based computer program but i can help a lot atleast better than fake people "
            print(about)
            speak(about)
        
        elif 'make you' in query or 'created you' in query or 'develop you' in query or 'your father' in query:
            ans = "Paritosh Mishra copied me and i am the future"
            print(ans)
            speak(ans)
        
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_u = takeCommand()
            if 'fine' in ans_u or 'happy' in ans_u or 'okey' in ans_u:
                speak('okey..')  
            elif 'not' in ans_u or 'sad' in ans_u or 'upset' in ans_u:
                speak('oh sorry..') 

        elif "google" in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            print(cm)
            url = 'https://google.com/search?q=+cm'
            webbrowser.open(url)
            
        # elif "send message" in query or "send whatsapp" in query:
        #     speak("what should i messgae")
        #     msg=takeCommand()
        #     print(msg)
        #     kit.sendwhatmsg("numer-for-msg", msg,2,25)

        elif "set alarm" in query:
            nn= int(datetime.datetime.now().hour)
            if nn==22 :
                music_dir=""
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif "joke" in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            img = pyautogui.screenshot()
            img.save('C:\\Users\\PARITOSH MISHRA\\Pictures\\Screenshots\\jravisshot.jpg')
              
        elif "shut down the system" in query:
            os.system("shutdown /r /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dld,SetSuspendState 0,1,0")

        elif 'cpu' in query or "status" in query or "state" in query:
            usage = str(psutil.cpu_percent())
            speak("CPU is at"+usage+"percentage usage")
            battery = psutil.sensors_battery()
            speak("battery is at"+str(battery.percent)+"percentage")

        elif 'remember anything' in query:
            remember = open('remember.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'remember' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('remember.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif "news" in query or "headlines" in query or "headline" in query:
            url = 'https://inshorts.com/en/read'
            response = requests.get(url)
            print_headlines(response.text)
            
        elif "location" in query or "where i am" in query or "where we are" in query :
            g = geocoder.ip('me')
            print(f"City: {g.city} State: {g.state} Country: {g.country} Longitude: {g.latlng[0]} Latitude: {g.latlng[1]}")
            speak(f"sir we are at longitude {g.latlng[0]} and latitude {g.latlng[1]} ,,,, {g.city} ,,,, in state {g.state} ,,,, of country {g.country}" )

        elif "insta profile" in query:
            speak("sir please enter the user name correctly")
            name = input("Enter Username :")
            webbrowser.open(f"www.instagram.com/{name}")
            
            speak(f"sir would you like to download the profile pic of this account")
            condition =takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("done sir !")
            else:
                speak("sorry sir!it's private account i can't get access")     

        elif "read pdf" in query:
            pdf_reader()  

        elif "calculation" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("what do you want to calculate for example 2 plus 2")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string =r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add,
                    '-' : operator.sub,
                    '*' : operator.mul,
                    'divide': operator.__truediv__,
                }[op]
            def eval(op1,oper,op2):
                op1,op2=int(op1), int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("your result is")
            print(eval(*(my_string.split())))
            speak(eval(*(my_string.split())))

        elif "temperature" in query or "wheather" in query:
            url=f"https://www.google.com/search?q={query}"
            r= requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp= data.find("div",class_="BNeawe").text
            speak(f"{query} is {temp}")

        elif "internet speed" in query:
            speak("checking sir wait a minute")
            st=speedtest.Speedtest()
            dl=st.download()/(1028*1028)
            up=st.upload()/(1028*1028)
            speak(f"sir we have {dl} MB per second of downloading speed and {up} MB per second of uploading speed")
