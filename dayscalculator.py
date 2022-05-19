from datetime import date
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import time

now_year = int(time.strftime("%Y"))
now_month = int(time.strftime("%m"))
now_day = int(time.strftime("%d"))
now_date = date(now_year,now_month,now_day)

def tokenizer(data):
    mystopwords = set(stopwords.words('english'))
    words = word_tokenize(data)
    wordsFiltered = []
    mystopwords.add('currency')
    mystopwords.add('convert')
    #print(stopWords)
    for w in words:
        if w not in mystopwords:
            wordsFiltered.append(w)
    return wordsFiltered





f_date = date(2012, 11, 12) # Use format (YY, MM, DD)
l_date = date(2015, 12, 14)
print(f_date)
delta = now_date - f_date
total_days = delta.days
print(total_days)
years = int(total_days/365)
total_days = total_days - (365*years)
months = int(total_days/30)
day = int(total_days - (months*30))

print(years, "Year(s),", months, "Month(s) and", day, "Day(s)")



