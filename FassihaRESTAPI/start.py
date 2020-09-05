"""
This script is the main start point of the voice assistant
"""
from NLP.nlp import tokenizer
from NLP.classifier import classifier_main

def run():
    txt_path = 'NLP/data/user_requests/req.txt'
    xml_path = tokenizer.request_tokenizing(txt_path, 'NLP/data/user_requests')
    a, b, c = classifier_main.classify_zero_or_one(xml_path, 'NLP/data/apps_data')
    print(a, b, c)
    return a, b, c
