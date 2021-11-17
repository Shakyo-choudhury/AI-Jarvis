import pyttsx3
import speech_recognition as sr
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
   engine.say(text)
   engine.runAndWait()


def take_command():
   try:
       with sr.Microphone() as source:
           print("computing......................")
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           command = command.lower()
           if 'sars' in command:
               command = command.replace('sars', '')
               print(command)
   except:
       pass
   return command


def speak(float):
   engine.say(float)
   engine.runAndWait()