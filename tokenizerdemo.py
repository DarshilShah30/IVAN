import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


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
