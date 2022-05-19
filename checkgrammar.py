from pattern.en import conjugate, lemma, lexeme,PRESENT,SG


#print(lemma('making'))
#print(lexeme('making'))
#print (conjugate(verb='made',tense=PRESENT,number=SG)) # he / she / it

verb = ['VB','VBD','VBG','VBN','VBP','VBP','VBZ']

def intersection(a, b): 
    c = [value for value in a if value in b] 
    return c



def checkgrammar(tokens,postags,posarray,bigram,flag):
    new_sent = str(' '.join(tokens))
    #self.tokens = tokens
    #self.posarray = posarray
    #self.bigram = bigram
    #print(tokens)
    #print(postags)
    #print(posarray)
    #print(bigram)

    if ('VB','VBG') in bigram:
        print("Wrong grammar")
        i = posarray.index('VBG')
        word = tokens[i]
        print(tokens[i])
        new_word = lemma(word)
        print(new_word)
        tokens[i] = new_word
        new_sent = str(' '.join(tokens))
        print(new_sent)
        return(new_sent, 0)
    else:
        return(new_sent, 1)
    
        
    

    
