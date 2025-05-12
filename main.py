import speech_recognition as sr
import os
import pyttsx3

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
            query = r.recognize_google(audio,language = "en-in")
            print(f"User said {query}")
            return query
        except Exception as e:
            return "Some error occured,Sorry from Jarvis"

if __name__ == "__main__" :
    '''speak("Hello World !!")
    speak("Hello I am Jarvis A I")'''
    while True:
        print("Listening...")
        query = take_command()
        #speak(query)