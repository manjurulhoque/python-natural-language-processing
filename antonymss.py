# Get antonyms from WordNet
from nltk.corpus import wordnet

antonyms = []

for syn in wordnet.synsets('small'):

    for lemma in syn.lemmas():
        if lemma.antonyms():
            #synonyms.append(lemma.name())
            print(lemma.antonyms())

# print(synonyms)