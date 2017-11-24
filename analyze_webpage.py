from bs4 import BeautifulSoup
import nltk
import urllib.request

response = urllib.request.urlopen('http://php.net/')

html = response.read()

soup = BeautifulSoup(html, "html5lib")

text = soup.get_text(strip=True)

tokens = [t for t in text.split()] # splitting text

# calculate the frequency distribution of those tokens
frequency = nltk.FreqDist(tokens)

# frequency of every word
items = frequency.items()

# most common
most_common = frequency.most_common(1)

# for word, number in items:
#     print(str(word) + " : " + str(number)+"\n")
frequency.plot(20, cumulative=False)
