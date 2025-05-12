from time import strftime

import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio,language = "en-in")
            print(f"User said {query}")
            return query
        except Exception as e:
            return "Some error occured,Sorry from Jarvis"

if __name__ == "__main__" :
    #speak("Hello World !!")
    speak("Hello I am Jarvis A I")
    while True:
        print("Listening...")
        query = take_command()
        #speak(query)
        sites = [['youtube',"https://www.youtube.com/"],["Twitter","https://twitter.com/"],["WikiPedia","https://en.wikipedia.org/wiki/Wiki"],["Chat GPT","https://openai.com/index/chatgpt/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            speak("Opening music")
            musicPath = r"C:\Users\Akshay\Downloads\music.mp3"
            os.startfile(musicPath)
        if "time" in query:
            strfTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Sir the time is {strfTime}")