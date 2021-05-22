import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pythoncom
from playsound import playsound
import requests
from bs4 import BeautifulSoup
import pywhatkit
import pyowm
import random
import sys
import smtplib
import pyjokes
import time
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
#print(voices[1].id)
def speak(audio):
    pass
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am zarvis ,please tell me how can i help u")
def takeCommand():
    #it takes microphone input from the user and returns the string as the output
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                      
        print("listening...")
        audio = r.record(source,duration=3)
        try:
            query=r.recognize_google(audio)
            print(query)
        except:
            print("some error occurred!")
        return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('prankitsrivastava03@gmail.com','8808772103')
    server.sendmail('prankitsrivastava03@gmail.com',to,content)



if __name__ =="__main__":
        wishMe()
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('searching  wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("ok sir  .   by your order  . i am opening youtube")
                webbrowser.open("www.youtube.com")
            elif 'hello veronica' in query:
                print('hello veronica')
                speak("hi sir .   you called me quite after a long time  .   what should ido to entertain you  .  sir")
            elif 'open google' in query:
                speak("ok sir  .   because of low internet speed   .  it may take some time to open")
                webbrowser.open("www.google.com")
            elif 'open stack overflow' in query:
                webbrowser.open("https://stackoverflow.com//")
            elif 'open whatsapp web' in query:
                webbrowser.open("www.google.com{web.whatsapp.com}")
            elif 'play music' in query:
                webbrowser.open("youtube.com")
            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir,the time is {strTime}")
            elif 'how are you ' in query:
                speak("i an absolutely fine ,sir")
            elif 'close all the operations' in query:
                speak("you dont worry about that sir  .  i will see that is done")
                sys.exit()
            elif 'talking' in query:
                speak("sir   .  i am you personal assistant  veronica    .  i am ready to dodo any thing at your order sir ")
            elif 'who are you' in query:
                speak("you dont recognized me sir    !!  i am veronica   .    your personalassistant sir  !!")
            elif 'about me' in query:
                speak("sir your  name is prankit srivastava   .    and   . you are mydeveloper   .   i am at you order sir   .   if you want then i caneven play game with you sir"
)
            elif 'play ludo' in query:
                speak("sir  .  i am opening ludo .    if you want i can also play ludo withyou   .  sir ")
                webbrowser.open('https://www.facebook.com//ludokinggame//')
            elif 'lazy' in query:
                speak("i am totally your carbon copy sir")
            elif 'annoying' in query:
                speak("sorry   .  sir i will try not to say that again")
            elif 'bekhayali' in query:
                playsound('E:\\musicly\\flying.mp3')
            elif 'tujhe kitna' in query:
                playsound('E:\\musicly\\tiger.mp3')
            elif 'hai apna dil' in query:
                playsound('E:\\musicly\\ky.mp3')
            elif 'humsafar' in query:
                playsound('E:\\musicly\\ke.mp3')
            elif 'ham pagal nahin ' in query:
                playsound('E:\\musicly\\jatt.mp3')
            elif 'temperature of' in query:
                query=query.replace('temprature of',"")
                search=query
                url=f"https://www.google.com/search?q={search}"
                r=requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current{search}is{temp}")
                print(f"current{search}is{temp}")
            elif 'who is harshit' in query:
                speak("harshit bhaiya is your jaani dushman sir")
            elif 'now you can leave veronica' in query:
                speak("by you order i am going to take a nap .   but i will be always at you command")
                sys.exit()
            elif 'snake' in query:
                speak("sure sir    .  i would also like to play that game with you sir")
                def gameWin(comp, you):
                    if comp == you:
                        return None
                    elif comp =='s':
                        if you=='w':
                            return False
                        elif you=='g':
                            return True
                    elif comp=='w':
                        if you=='g':
                            return False
                        elif you=='s':
                            return True
                    elif comp=='g':
                        if you=='s':
                            return False
                        elif you=='w':
                            return True
                print("computer Turn:Snake(s) water(w) gun(g)?")
                randNo = random.randint(1,3)
                comp=""
                if randNo == 1:
                    comp = 's'
                elif randNo == 2:
                    comp = 'w'
                elif randNo == 3:
                    comp='g'
                you = input("your Turn: Snake(s) water(w) or gun(g)?")
                print(comp,you)
                a = gameWin(comp, you)
                print(f"computer choose{comp}")
                print(f"you choose {you}")
                if a==None:
                    print("the game is a tie")
                    speak("thats a tie sir!!")
                elif a:
                    print("you win")
                    speak("fortunately!! you won sir ")
                else:
                    print("you loose")
                    speak("ha ha ha!! you lose sir")
            elif 'dog' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="vanyasrivastava12@gmail.com"
                    sendEmail(to,content)
                    speak("email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'email to harshit bhaiya' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="harshitkapoor.Kapoor94@gmail.com"
                    sendEmail(to,content)
                    speak("email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'email to upendra bhaiya' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="upendrasharma1109@gmail.com"
                    sendEmail(to,content)
                    speak("email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'email to akash bhaiya' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="akashtripathi004@gmail.com"
                    sendEmail(to,content)
                    speak("email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'joke' in query:
                joker=(pyjokes.get_joke())
                engine.setProperty('rate',100)
                print(joker)
                speak(joker)
            elif 'didi' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('+917309101364',body,hour,minutes)

                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")


            elif 'message akash bhaiya' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('+916306050573',body,hour,minutes)

                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")

            elif 'message harshit bhaiya' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('+919670873598',body,hour,minutes)

                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")

            elif 'pagal didi' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('+919555859225',body,hour,minutes)

                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")


            