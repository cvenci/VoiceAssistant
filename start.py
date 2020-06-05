import NLP.nlp.tokenizer as tk
tk.request_tokenizing('NLP/data/user_requests/req.txt', stop_words_path='NLP/data/arabic_stopwords.txt', save_path='NLP/data/user_requests')