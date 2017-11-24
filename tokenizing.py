from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

sentence = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

# tokenize sentence
print(sent_tokenize(sentence))

# tokenize words
print(word_tokenize(sentence))
