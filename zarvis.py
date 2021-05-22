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
    speak("I am veronica ,please tell me how can i help u")
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
    server.login('enter the mail from which you have to send mail','your password')
    server.sendmail('same email',to,content)


if __name__=="__main__":
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
                speak("hi sir .   you called me quite after a long time  .   what should i do to entertain you  .  sir")
            elif 'open google' in query:
                speak("ok sir  .   because of low internet speed   .  it may take some time to open")
                webbrowser.open("www.google.com")
            elif 'open stack overflow' in query:
                webbrowser.open("https://stackoverflow.com//")
            elif 'open whatsapp web' in query:
                webbrowser.open("www.google.com{web.whatsapp.com}")
            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir,the time is {strTime}")
            elif 'how are you ' in query:
                speak("i an absolutely fine ,sir")
            elif 'close all the operations' in query:
                speak("you dont worry about that sir  .  i will see that is done")
                sys.exit()
            elif 'talking' in query:
                speak("sir   .  i am you personal assistant  veronica    .  i am ready to do do any thing at your order sir ")
            elif 'who are you' in query:
                speak("you dont recognized me sir    !!  i am veronica   .    your personal assistant sir  !!") 
            elif 'about me' in query:
                speak("sir your  name is vanya   .    and   . you are my developer   .   i am at you order sir   .   if you want then i can even play game with you sir")
            elif 'play ludo' in query:
                speak("sir  .  i am opening ludo .    if you want i can also play ludo with you   .  sir ")
                webbrowser.open('https://www.facebook.com/games/ludo-king/?fbs=110&fb_appcenter=1')
            elif 'lazy' in query:
                speak("i am totally your carbon copy sir")
            elif 'annoying' in query:
                speak("sorry   .  sir i will try not to say that again")
            elif 'gta' in query:
                playsound('C://Users//VANYA SRIVASTAV//DOWNLOADS//gta.mp3')
            elif 'temperature of' in query:
                query=query.replace('temprature of',"")
                search=query
                url=f"https://www.google.com/search?q={search}"
                r=requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current{search}is{temp}")
                print(f"current{search}is{temp}")
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
            elif 'email from ' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="vanyasrivastava12@gmail.com"
                    sendEmail(to,content)
                    speak("email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'email to xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="xxxx"
                    sendEmail(to,content)
                    speak("email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'email to xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="xxxx"
                    sendEmail(to,content)
                    speak("email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'email to xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="xxxx"
                    sendEmail(to,content)
                    speak("email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'email to xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="xxxx"
                    sendEmail(to,content)
                    speak("email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'email to xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="xxxx"
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
            elif 'email to xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    content=takeCommand()
                    to="xxxx"
                    sendEmail(to,content)
                    speak("email has been sent!")
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'message prankit' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('enter the number to send the whatsapp mess',body,hour,minutes)
                    
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")


            elif 'message xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('xxxx',body,hour,minutes)
                    
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")


            elif 'message xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('xxxx',body,hour,minutes)
                    
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")


            elif 'message xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('xxxx',body,hour,minutes)
                    
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")


            elif 'message xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('xxxx',body,hour,minutes)
                    
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")


            elif 'message xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('xxxx',body,hour,minutes)
                    
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'message xxxx' in query:
                try:
                    speak("ok   .  sir  .  what should i say?")
                    body=takeCommand()
                    speak("sir please tell me the hour")
                    hour=takeCommand()
                    hour=int(hour)
                    speak("sir please tell me the minutes")
                    minutes=takeCommand()
                    minutes=int(minutes)
                    pywhatkit.sendwhatmsg('xxxx',body,hour,minutes)
                    
                except Exception as e:
                    print(e)
                    speak("sorry i am not able to send that sir")
            elif 'weather' in query:
                speak("sir please tell the place")
                city=takeCommand()
                Api_key="ec26defa6485d4ab82cd1043c504c48e"
                final_url="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,Api_key)
                result=requests.get(final_url)
                data=result.json()
                speak(f"the current pressure of {city} is")
                weather=data['main']['pressure']
                speak(weather)
                speak("atmospheres")
                weathe=data['main']['humidity']
                speak(f"the current pressure of{city} is ")
                speak(weathe)
                speak("percent")
                weat=data['wind']['speed']
                speak(f"the current wind speed in{city} is ")
                speak(weat)
                speak("meter per second")
            elif "clock" in query:
                speak ("sir i am showing you the digital clock")
                root=Tk()
                root.title("Clock")

                def time():
                    string=strftime('%H:%M:%S%p')
                    label.config(text=string)
                    label.after(1000,time)
                label=Label(root,font=("ds-digital",80),background="black",foreground="cyan")
                label.pack(anchor='center')

                time()

                mainloop()
        
        
        


