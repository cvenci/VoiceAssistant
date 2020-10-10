"""
Reading the input from the voice reco phase and
transferring it to a structured XML file ready
to be parsed and used by the classifier to
determine the type of the command in the input
"""

from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem import ISRIStemmer
import re
import xml.etree.cElementTree as ET
from xml.dom import minidom


def request_normalizer(req_text_path, save_path='../data/user_request'):
    pass


def request_tokenizing(req_text_path, save_path='../data/user_requests'):
    """
    :param req_text_path: the path to the request .txt file
    :param save_path: the path to save the structured .xml output
    :return: read a request, tokenize & stem it and save the info in structured xml file
    """
    f = open(req_text_path, encoding='utf8')
    line = f.readline()
    f.close()
    # reading stop words
    stop_words = stopwords.words('arabic')

    # deleting punctuation THIS IS A MATTER OF DISCUSSION
    line = re.sub(r'[^\w\s]', '', line)
    # NLP
    tokenizer = WordPunctTokenizer()
    stemmer = ISRIStemmer()

    tokens = tokenizer.tokenize(line)
    root = ET.Element('root')
    tok_elem = ET.SubElement(root, 'tokenization')

    i = 1
    sw = False
    for t in tokens:
        stem = stemmer.stem(t)
        if str(t) in stop_words:
            sw = True
        ET.SubElement(tok_elem, 'word', id=str(i), value=str(t), stop_word=str(sw), stem=stem)
        i += 1
        sw = False

    file_str = save_path + '/'+req_text_path.split('/')[-1].split('.')[0]+'.xml'
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
    with open(file_str, 'w', encoding='utf-8') as f:
        f.write(xmlstr)
    f.close()

    return file_str

# STEMMING THE WORDS : for now we are using ISRIStemmer from nltk witch is a heavy stemmer
# more work will be done in order to test other stemmers
