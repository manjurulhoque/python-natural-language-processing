# Get Synonyms from WordNet
from nltk.corpus import wordnet

# synonyms = wordnet.synsets("world")

# print(synonyms[0].definition())
# print(synonyms[0].examples())

synonyms = []

for syn in wordnet.synsets('Computer'):

    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(synonyms)