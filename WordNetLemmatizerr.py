"""
Word lemmatizing is similar to stemming, but the difference is the result of lemmatizing is a real word
"""
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# print(lemmatizer.lemmatize('increases'))

# to get verbs
print(lemmatizer.lemmatize('good', pos="v"))
# to get noun
print(lemmatizer.lemmatize('better', pos="n"))
# to get adjective
print(lemmatizer.lemmatize('good', pos="a"))
# to get adverb
print(lemmatizer.lemmatize('good', pos="r"))