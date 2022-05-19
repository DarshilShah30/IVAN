from pprint import pprint
import requests
import pyttsx3
from gtts import gTTS
#from pygame import mixer
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

#r = requests.get("http://api.accuweather.com/localweather/v1/349727?apikey={e4UMGowR6EYpXJ9wbO52lIqwAmYDjgIe}")
#pprint(r.json())

mode = "voice"
voice = "pyttsx3"
mystopwords = set(stopwords.words('english'))

def tokenizer(data):
    mystopwords = set(stopwords.words('english'))
    words = word_tokenize(data)
    wordsFiltered = []
    mystopwords.add('weather',)
    mystopwords.add('temperature')
    mystopwords.add('humidity')
    mystopwords.add('calsius')
    mystopwords.add('fahrehiet')
    mystopwords.add('degrees')
    mystopwords.add('wind')
    mystopwords.add('speed')
    mystopwords.add('outside')
    #print(stopWords)
    for w in words:
        if w not in mystopwords:
            wordsFiltered.append(w)
    return wordsFiltered
        
def cel(a):
    c = (a - 273.15)
    return int(c)

def fer(b):
    f = (b - 273.15) * 9/5 + 32
    return int(f)

def offline_speak(jarvis_speech):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(jarvis_speech)
    engine.runAndWait()

def speak(jarvis_speech):
    offline_speak(jarvis_speech)

def ps(print_and_speak):
    print(print_and_speak)
    speak(print_and_speak)

def weather(res):
    try:
        try:
            city = tokenizer(res)
            city = city[0]
        except:
            city = 'Gandhinagar'
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=d51302f2b5db64fc7b08f3643701654e")    
        data = r.json()
        #pprint(data)
        w = data['wind']['speed'] * 18/5
        wind = "{:.2f}".format(w)
        mytokens = nltk.word_tokenize(res)
        if 'weather' in mytokens and 'temperature' not in mytokens:
            ps("There is "+data['weather'][0]['description']+" outside.")
            ps("Temperature of "+city+" is "+str(cel(data['main']['temp']))+" degree celsius.")
            ps("Humidity is "+str(data['main']['humidity'])+" percent.")
            ps("Wind speed is "+str(wind)+" kilometer per hour.")
        if 'temperature' in mytokens and 'weather' not in mytokens:
            if 'fahrenheit' in mytokens:
                ps("Temperature of "+city+" is "+str(fer(data['main']['temp']))+" degree fahrenheit.")
            else:
                ps("Temperature of "+city+" is "+str(cel(data['main']['temp']))+" degree celcius.")
        if 'humidity' in mytokens and 'weather' not in mytokens:
            ps("Humidity is "+str(data['main']['humidity'])+" percent.")
        if 'wind' in mytokens and 'weather' not in mytokens:
            ps("Wind speed is "+str(wind)+" kilometer per hour.")
    except:
        ps("I don't understand.")

    



