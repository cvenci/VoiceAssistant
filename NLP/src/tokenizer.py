from nltk.tokenize import WordPunctTokenizer
import xml.etree.cElementTree as ET

f = open('../data/user_requests/req.txt')
line = f.readline()
tokenizer = WordPunctTokenizer()
tokens = tokenizer.tokenize(line)
root = ET.Element('root')
for t in tokens:
    word = ET.SubElement(root,'word')
tree = ET.ElementTree(root)
tree.write('try.xml')
