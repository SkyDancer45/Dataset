import speech_recognition as sr
import os
import win32com.client

def say(text):
    speaker= win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen()
        query= r.recognize_google(audio, language='en-in')
        print(query)
if __name__ == "__main__":
    print("Google Speech Recognition")
    say("Hi, I'm Goose!")