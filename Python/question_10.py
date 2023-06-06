
#Write a program to count the number of verbs, nouns, pronouns, and adjectives in a given particular phrase or
#paragraph, and return their respective count as a dictionary.

import nltk
from collections import Counter

def pos_count(text):

    dic ={'nouns':0,'pronouns':0,'verbs':0,'adjectives':0}
    
    tokens = nltk.word_tokenize(text.lower()) #tokenixe the paragraph
    text = nltk.Text(tokens)
    tags = nltk.pos_tag(text) #tagging words with part of speech

    counts = Counter(tag for word,tag in tags) #counting the part of speech tags
    
    dic['nouns'] = counts['NN']
    dic['pronouns'] = counts['PRP'] + counts['PRP$']
    dic['verbs'] = counts['VB']
    dic['adjectives'] = counts['JJ']
    return dic


text1 = "In winter, we truly like to drink a hot and tasty beverage"
text2 = "Wow, Harry and Meghan really surprised the queen with their sudden decision"

print(pos_count(text1))
print(pos_count(text2))