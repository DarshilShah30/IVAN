import pymongo
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import urllib.parse

def intersection(a, b): 
    c = [value for value in a if value in b] 
    return c

#username = urllib.parse.quote_plus('student')
#password = urllib.parse.quote_plus('Test@1234')
#print(username,password)
# database connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#myclient = pymongo.MongoClient("mongodb://10.20.20.21:27017/local?authSource=admin")
#myclient = pymongo.MongoClient('mongodb://10.20.20.21:27017/', user='madmin', password='madmin@123', authSource='admin', authMechanism='SCRAM-SHA-1')
#myclient = pymongo.MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
mydb = myclient["local"]
mycol = mydb["IVAN"]

def check_db(query):
    try:
        """sentences = nltk.sent_tokenize(query)
        #sentiment analysis
        sid = SentimentIntensityAnalyzer()
        new_query = ""
        for sentence in sentences:
            ss = sid.polarity_scores(sentence)
            # only negative sentences are taken in attention
            if ss['neg']>ss['pos'] or ss['neu']==1:
                new_query = new_query + sentence"""
        tokens = word_tokenize(query.lower())
        q = ['email','network','scanner','printer','pc','laptop']
        # comparing root node first
        if intersection(tokens,q):
            c = mycol.find_one({"que":intersection(tokens,q)[0]})
            # comparing child nodes 
            if intersection(tokens,c['child']):
                x = mycol.find_one({"que":intersection(tokens,c['child'])[0]})
                return(x['ans'])
            else:
                return(c['ans'])
        else:
            # when no root nodes are detected
            for t in tokens:
                c = mycol.find_one({"que":t})
                if c is not None:
                    return(c['ans'])
                    break
        # not in database
        if c is None:
            return None
    except:
        return None
                
                

    
        
        

