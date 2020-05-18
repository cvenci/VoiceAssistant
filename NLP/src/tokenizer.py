"""
Reading the input from the voice reco phase and
transferring it to a structured XML file ready
to be parsed and used by the classifier to
determine the type of the command in the input
"""

from nltk.tokenize import WordPunctTokenizer
import xml.etree.cElementTree as ET
from xml.dom import minidom  # pycharm error

f = open('../data/user_requests/req.txt')
line = f.readline()
tokenizer = WordPunctTokenizer()
tokens = tokenizer.tokenize(line)
root = ET.Element('root')
tokElem = ET.SubElement(root, 'tokenization')
i = 1
for t in tokens:
    word = ET.SubElement(tokElem, 'word', id=str(i), value=str(t))
    i += 1

xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
with open("../data/user_requests/req.xml", "w", encoding='utf-8') as f:
    f.write(xmlstr)
