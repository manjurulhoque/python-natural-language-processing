"""
Word stemming means removing affixes from words and return the root word.
Ex: The stem of the word working => work.
"""
from nltk.stem import PorterStemmer, LancasterStemmer

stemmer = PorterStemmer()

print(stemmer.stem("increases"))
