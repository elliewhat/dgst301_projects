import random
from textblob import TextBlob

#This opens the text file Harry Potter and the Goblet of Fire chapters 1-5
with open('HP4.txt', 'r') as file:
    text = file.read()
    
blob = TextBlob(text)
#creating the blank groups will allow my code to pull from the text file and create the content for it
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
 #This will be the structure of my poem, the code will randomly pull a determiner, adjective, and then noun       
for i in range(5):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    d = random.choice(determiner)
    print (d,a,n)
#I went with 5 lines because I felt like it was a good length, not too long but not too short.  
#I tried to do 8-10 lines and it was just too long and wasn't making sense
#I kept it short because every time I tried to add something else or arrange it a different way, it didn't work or sounded weird
