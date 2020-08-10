# import NLP.nlp.tokenizer as tk
# tk.request_tokenizing('NLP/data/user_requests/req.txt', stop_words_path='NLP/data/arabic_stopwords.txt', save_path='NLP/data/user_requests')

"""from nltk.tokenize import WordPunctTokenizer
from nltk.stem import ISRIStemmer

tokenizer = WordPunctTokenizer()
t = tokenizer.tokenize('المدرسة')
print(t)
stemmer = ISRIStemmer()
s = stemmer.stem(t[0])
print(s)
"""
line = '   something   '
line = line.lstrip(' ').rstrip(' ')
line = line.replace('s', 't')
print(line)
