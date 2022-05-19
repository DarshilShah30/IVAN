import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
mystopwords = set(stopwords.words('english'))
print(len(mystopwords))
mystopwords.add('currency')
mystopwords.add('convert')
print(len(mystopwords))

   
