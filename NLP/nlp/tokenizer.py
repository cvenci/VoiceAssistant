"""
Reading the input from the voice reco phase and
transferring it to a structured XML file ready
to be parsed and used by the classifier to
determine the type of the command in the input
"""

from nltk.tokenize import WordPunctTokenizer
import xml.etree.cElementTree as ET
from xml.dom import minidom  # pycharm error


def request_tokenizing(req_text_path, stop_words_path='../data/arabic_stopwords.txt',
                       save_path= '../data/user_requests'):
    """Read the request text file and produce
    tokenizaton XML file for the request"""
    f = open(req_text_path)
    line = f.readline()
    f.close()
    # reading stop words
    stop_words_file = open(stop_words_path)
    stop_words = stop_words_file.read().splitlines()
    stop_words_file.close()

    #NLP
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(line)
    root = ET.Element('root')
    tokElem = ET.SubElement(root, 'tokenization')
    i = 1
    sw = False
    for t in tokens:
        if str(t) in stop_words:
            sw = True
        ET.SubElement(tokElem, 'word', id=str(i), value=str(t), stop_word=str(sw))
        i += 1
        sw = False

    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
    with open(save_path + '/req.xml', 'w', encoding='utf-8') as f:
        f.write(xmlstr)
    f.close()

# request_tokenizing('../data/user_requests/req.txt')
