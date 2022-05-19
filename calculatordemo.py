import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import urllib.parse
import requests
from bs4 import BeautifulSoup

def tokenizer(data):
    mystopwords = set(stopwords.words('english'))
    words = word_tokenize(data)
    wordsFiltered = []
    mystopwords.add('calculate')
    mystopwords.add('answer')
    mystopwords.add('how')
    mystopwords.add('much')
    #print(stopWords)
    for w in words:
        if w not in mystopwords:
            wordsFiltered.append(w)
           # print(wordsFiltered)
    return wordsFiltered

def calc(res):
    try:
        query = tokenizer(res)
        q = ("".join(query))
        res = urllib.parse.quote(q)
        h = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"}
        r = requests.get("https://www.google.com/search?q="+res, headers=h).text
        soup = BeautifulSoup(r,"lxml")
        div = soup.select_one("div.g")
        div = soup.select_one("div.z7BZJb")
        ans = soup.select_one("span.qv3Wpe")
        return(q+" is equal to "+ans.text)
    except:
        return("I don't know the answer.")

    
