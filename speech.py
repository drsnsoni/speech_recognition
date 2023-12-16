import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    try:
        print("listening..... ")
        audio_data = r.record(source, duration=10)
        print("Reorganizing.....")
        text = r.recognize_google(audio_data)
        print(text)
    except:
        print("Sorry I Can't Understand :D")
