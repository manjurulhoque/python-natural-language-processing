from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import urllib.request

response = urllib.request.urlopen('http://php.net/')

html = response.read()

soup = BeautifulSoup(html, "html5lib")

text = soup.get_text(strip=True)

tokens = [t for t in text.split()] # splitting text

# There are some words like The, Of, a, an, and so on. These words are stop words

clean_tokens = tokens[:] # copying

# removing stopwords
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

frequency = nltk.FreqDist(clean_tokens)

# for word, count in frequency.items():
#     print(str(word) + " : " + str(count))

frequency.plot(20, cumulative=False)