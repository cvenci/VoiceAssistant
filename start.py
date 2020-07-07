# import NLP.nlp.tokenizer as tk
# tk.request_tokenizing('NLP/data/user_requests/req.txt', stop_words_path='NLP/data/arabic_stopwords.txt', save_path='NLP/data/user_requests')
from os import listdir
from os.path import isfile, join
mypath = 'NLP/data/apps_data'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(files)
print(join(mypath, files[0]))