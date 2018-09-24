import random
from textblob import TextBlob

#This opens the text file Harry Potter and the Goblet of Fire chapters 1-5
with open('HP4.txt', 'r') as file:
    text = file.read()
    
blob = TextBlob(text)

adjectives = []
nouns = []
determiner = []
for word,pos in blob.tags:
    #print(word,pos)
    if (pos == 'JJ'):
        adjectives.append(word)
    if (pos == 'NNS'):
        nouns.append(word)
    if (pos == 'DT'):
        determiner.append(word)
        
for i in range(5):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    d = random.choice(determiner)
    print (d,a,n)
#I went with 5 lines because I felt like it was a good length, not too long but not too short
