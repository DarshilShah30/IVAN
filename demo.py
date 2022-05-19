import pymongo
import datetime
import pyttsx3
#from gtts import gTTS
import os
from os import system
import argparse
import json
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import webbrowser
import wikipedia
#from google import google
import urllib.parse
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
from tokenizerdemo import tokenizer
from wakeworddetection import wakeword
from bson import ObjectId
import simpleaudio as sa
import random
import checkdb



mode = "text"
voice = "pyttsx3"
#voice = "gTTS"
terminate = ['bye','bye-bye', 'buy', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']
calculator = ['calculator', 'calculate', 'c', 'calc', '+', '-', '/', 'x', 'modulo']
weather = ['weather', 'temperature', 'humidity', 'calsius', 'fahrehiet', 'degrees']
meaning = ['meaning', 'means', 'define', 'defination', 'explain', 'explained']
date = []

noanswer = ["I don't know about that.",
            "I don't understand.",
            "Please be specific about your problem."]

filename = 'for-sure.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
#play_obj.wait_done() 


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
now = datetime.datetime.now()

#mylist1 = json.loads(mylist)

def get_arguments():
    parser = argparse.ArgumentParser()
    optional = parser.add_argument_group('params')
    optional.add_argument('-v', '--voice', action='store_true', required=False,
                          help='Enable voice mode')
    optional.add_argument('-g', '--gtts', action='store_true', required=False,
                          help='Enable Google Text To Speech engine')
    arguments = parser.parse_args()
    return arguments

def offline_speak(jarvis_speech):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(jarvis_speech)
    engine.runAndWait()

def speak(jarvis_speech):
    offline_speak(jarvis_speech)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk to J.A.R.V.I.S: ")
        audio = r.listen(source)
    try:
        print ("you said :" + r.recognize_google(audio))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        speak("I couldn't understand what you said! Would you like to repeat?")
        return(listen())
    except sr.RequestError as e:
        print("Could not request results from " +
              "Google Speech Recognition service; {0}".format(e))

def update():
    question = response.lower()
    ps("Tell me about it: ")
    answer = input()
    ps("I am updating my database...")
    mycol.insert_one({ "que" : question, "ans" : answer })
    ps("Successfully Updated my database !!!")

def ps(print_and_speak):
    print(print_and_speak)
    speak(print_and_speak)

def intersection(a, b): 
    c = [value for value in a if value in b] 
    return c

def goto(linenumber):
    global line
    line = linenumber

def getinput():
    args = get_arguments()

    if (args.voice):
        try:
            import speech_recognition as sr
            mode = "voice"
        except ImportError:
            print("\nInstall SpeechRecognition to use this feature." +
                  "\nStarting text mode\n")
    if (args.gtts):
        try:
            from gtts import gTTS
            from pygame import mixer
            voice = "gTTS"
        except ImportError:
            import pyttsx3
            print("\nInstall gTTS and pygame to use this feature." +
                  "\nUsing pyttsx3\n")
    else:
        import pyttsx3   

def googledefine():
    try:
        h = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"}
        r = requests.get("https://www.google.com/search?q="+response, headers=h).text
        soup = BeautifulSoup(r,"lxml")
        div = soup.select_one("div.lr_dct_ent")
        expl = [li.text for li in div.select("ol.lr_dct_sf_sens li")]
        s = expl[0].split(".")
        if (s[0] == '1'):
            return (s[1])
        else:
            return (s[0])
    except:
        return None

def address():
    try:
        h = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"}
        r = requests.get("https://www.google.com/search?q="+response, headers=h).text
        soup = BeautifulSoup(r,"lxml")
        div = soup.select_one("div.g")
        div1 = soup.select_one("div.Z0LcW")
        if div1 is None:
            div2 = soup.select_one("div.vk_bk span")
            ps(div2.text)
        else:
            ps(div1.text)
        return 1
    except:
        return None

def wikisearch():
    try:
        ps(wikipedia.summary(response, sentences=3))
        return 1
    except:
        return None
        
def notindatabase():
    ps("do you want me to  update my database?")
    if mode=="voice":
        response = listen()
    else:          
        choice = input()
        tokens = nltk.word_tokenize(choice)
        doupdate = {'update', 'database', 'yes', 'y', 'yo', 'yup'}
        donotupdate = {'no', 'not', 'never', 'n'}
        u = intersection(tokens,doupdate)
        v = intersection(tokens,donotupdate)
        if u == [] and v != []:
            ps("ok, your choice.")
        elif u!= [] and v == []:
            update()
        else:
            ps("Say something specific like yes or no!")


                
if __name__ == '__main__':
    getinput()
    count = 0
    
    while True:
            if mode == "voice":
                response = listen()
            else:
                response = input("Talk to J.A.R.V.I.S: ")
                
            start = datetime.datetime.now()
            tokens = nltk.word_tokenize(response)
            if intersection(tokens,terminate):
                ps("Bye Bye !!!")
                break
            else:
                if intersection(tokens,calculator):
                    import calculatordemo as c
                    res = c.calc(response)
                    ps(res)
                    end = datetime.datetime.now()

                elif intersection(tokens,weather):
                    import weatherdemo as w
                    w.weather(response)
                    end = datetime.datetime.now()
                    
                else:
                    #x = mycol.find_one({"que":response.lower()},{"ans":1,"_id":0})
                    x = checkdb.check_db(response)
                    if x is None:
                        x = googledefine()
                        y = 1
                        end = datetime.datetime.now()
                            
                        if x is None:
                            end = datetime.datetime.now()
                            z = address()
                            if z is None:
                                end = datetime.datetime.now()
                                y = wikisearch()
                            if y is None and z is None:
                                end = datetime.datetime.now()
                                if count == 1:
                                    ps(random.choice(noanswer))
                                    #notindatabase()
                                else:
                                    ps("Can you be more specific please...")
                                    count = count + 1
                        else:
                            ps(x)
                            
                    else:
                        end = datetime.datetime.now()
                        ps(x)
                      
                       
    
            elapsed = end - start
            print("----------------------->Completed in",elapsed.seconds,".",elapsed.microseconds,"seconds<-------------------")   

wakeword()           
         


#pprint.pprint(mycol.find_one({"q":response},{"ans":1,"_id":0}))

