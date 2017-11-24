import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# messages = [line.rstrip() for line in open('SMSSpamCollection')]
#
# for count, message in enumerate(messages[:10], 1):
#     print(count, message)
#     print('\n')

messages = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])

# print(messages.describe())

# print(messages.groupby('label').describe())

messages['length'] = messages['message'].apply(len)

print(messages.head())