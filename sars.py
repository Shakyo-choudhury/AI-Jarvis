import datetime
from datetime import date
import json
import random
import math
import cv2
from bit_coin_updates import bitcoin
from my_inputs import take_command, talk
from py_news_api import sports_news_premier_league
from game_guessing import game
from my_weather import api, weather_api
from my_camera import cam
from my_apps import my_app
from wish_me import wishme
from cv2 import *
import random
from tkinter.constants import COMMAND
import speech_recognition as sr
import smtplib
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from email.message import EmailMessage
import requests
import time
import math
import os
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import ttk
from tkinter import *
import json
import cv2
from playsound import playsound
import PIL.Image
import sys
import os
import random
from my_news import pynewsindia
from my_email import get_email_info    
def shakyo():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('ok i will play it for you' + song)
        pywhatkit.playonyt(song)  
    elif 'game' in command:
        talk('ok i will play a game')
        game()
    elif 'what is my favorite language' in command:
        talk('python is my favorite language')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Bro the time is' + time)
    elif 'google' in command:
        son = command.replace('google', '')
        talk('ok i will play it for you' + son)
        ini = pywhatkit.info(son, lines=3)
        print(ini)

    elif 'answer the following' in command:
        my_query = command.replace('answer the following', '')
        my_info = pywhatkit.search(my_query)
        print(my_info)
        talk(my_info)
    elif 'say me about' in command:
        person = command.replace('say me about', '')
        info = wikipedia.summary(person, 10)
        print(info)
        talk(info)
    elif 'open meet' in command:
        talk('yes bro i will open it for you')
        webbrowser.open('https://meet.google.com/?authuser=1')
    elif 'bitcoin updates' in command:
        talk("okay i will say all the updates")
        var_bit=1
        while var_bit<2:
            bitcoin()
            var_bit=var_bit+1
    elif 'sports news' in command:
        _gkp=1
        while _gkp<2:
            sports_news_premier_league()
            _gkp=_gkp+1
    elif 'calculator' or 'solve' or 'math' in command:
        talk("oay i will open calculator for you")
        pywhatkit.search("google calculator")
    elif 'send a whatsapp message to a group' in command:
        talk("okay i will send the whatsapp message to the group but you have to fill some information for it")
        group_name=str(input("enter the group name"))
        text_message=str(input("enter the text you want to send"))
        hour_12hr=int(input("enter the hour you want to send the message (12 hour)"))
        minute_min=int(input("enter the minute you wanna send the message"))
        pywhatkit.sendwhatmsg_to_group(group_name,text_message, hour_12hr, minute_min)
    elif 'send a image to a whatsapp group' in command:
        talk("okay but you have to enter the given details")
        grp_name=str(input("enter the group name"))
        image_path=str(input('enter the image path that you wanna send'))
        caption=str(input("enter the caption"))
        pywhatkit.sendwhats_image(grp_name, image_path, caption)
    
    elif 'create a meeting' in command:
        talk('ok i will create a meeting for you')
        webbrowser.open_new_tab('http://meet.google.com/new')
    elif 'open youtube' in command:
         talk('yes bro i will open youtube')
         webbrowser.open("https://www.youtube.com/?authuser=1")
    elif 'who am i' in command:
        talk('you are my master because you have made me using python and hours of hardwork')
    elif 'who are you' in command:
        talk('i am sars an ai made by you, please say me how can i help you ')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open classroom' in command:
        talk('ok bro i will open it for you')
        webbrowser.open('https://classroom.google.com')
    elif 'open spotify' in command:
        talk ('I will open it for you')
        webbrowser.open("https://g.co/kgs/wb4KQQ")
    elif 'open google' in command:
        talk('ok man i will open it for you')
        webbrowser.open('https://www.google.com/?authuser=1')
    elif 'open my messages' in command:
        talk('ok i will open hangouts for you')
        webbrowser.open('https://hangouts.google.com/?authuser=1')
    elif 'repeat after me' in command:
        talk('ok bro i will repeat after you')
        das=take_command()
        talk(das)
    elif 'who are my best friends' in command:
        talk('you do not have any best friends because all are useless in this world and you are too expensive to others')
    elif 'covid hostipals near me' in command:
        talk('ok bro i have found a hospital near you')
        webbrowser.open('https://g.page/RMHofficial?share')
    elif 'send a whatsapp message' in command:
        talk('ok i will send the message but please type the message')
        phno=str(input('enter the reciver phone number : '))
        talk('please say you message')
        msg= take_command()
        talk('ok done')
        hour=int(input('enter in which hour you want to send the message(12hrclock): '))
        minu=int(input('enter in which minute  you want to send the message: '))
        pywhatkit.sendwhatmsg(phno, msg,hour, minu )
    elif 'who is prathamesh' in command:
        talk('prathamesh is a jerk who does not know how to speak and acts as if he is the victim 24/7 total jerk, that guy does not even know how to talk to techers. prathamesh is nothing but a bitch lasagna')
    elif 'how to make pizza' in command:
        talk('ok i will tell you how to make a pizza. you have to just watch the video which i will show you now')
        webbrowser.open('https://youtu.be/BFJ9Fjqa2-k')
    elif 'how to be sad' in command:
        talk('be like shakyo to be sad')
    elif 'the weather in ' in command:
        info1 = pywhatkit.search(command)
        tin=str(info1)
        dash=print('the weather is'+tin) 
        talk(dash)
    elif 'convert the text to handwriting' in command:
        string=str(input("enter the text you want to convert"))
        save_to=str(input("enter the name of the text file you want to save"))
        pywhatkit.text_to_handwriting(string, save_to, rgb=(0, 0, 0)) 
    elif 'who is the worst person on earth' in command:
        talk('shakyo is the worst person on earth, we all hate him and we will kill him he has no right to be alive ')
    elif 'heron formula' in command:
     talk('please give the sides of the triangle in the below form')
     sh1=float(input('enter the first side of the triangle : '))
     sh2=float(input('enter the second side of the triangle : '))
     sh3=float(input('enter the third side of the triangle : '))
     sh4=sh1 + sh2 + sh3
     sh5=sh4/2
     sh6=sh5-sh1
     sh7=sh5-sh2
     sh8= sh5-sh3
     sh9= sh5*sh6*sh7*sh8
     sh10= sh9**0.5
     print('the answer is :', sh10)
     talk(sh10)
    elif 'search ' in command:
        bakwas = command.replace('search', '')
        talk('ok i will search it for you' + bakwas)
        pywhatkit.search(bakwas)
    elif 'repeat after me ' in command:
        talk(command)
    elif 'open google chrome' in command:
        talk('ok i will open it for you')
    elif 'send a mail' in command:
        talk('ok i will send the mail for you')  
        h = 1
        while h < 2:
            get_email_info()
        h = h+1
    elif 'weather' in command:
       weather_api()
    elif 'camera' in command:
        talk('ok i will open camera for you')
        cam()
    elif 'news' in command:
       talk('ok i will tell the news for you')
       k=1
       while k<2:
            pynewsindia()
            k=k+1
    elif 'set alarm'in command:
       talk('ok but you have enter the time below')
   
    elif 'open some apps for me' or 'open apps' in command:
        kg=1
        while kg<2:
            my_app()
            kg=kg+1        
    else:
        talk('the command which you gave is out of my code list kindly assign me something else.')
i = 1
while i < 2:
  wishme()
  i = i+1
while True:
   shakyo()