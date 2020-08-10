"""
This script provide methods to clean and prepare the TALAA corpus
to the deep learning phase of the response generation
"""
import xml.etree.cElementTree as cet
from xml.dom import minidom
import re


def quick_clean(path='data/corpus.xml'):
    """
    DID THIS BECAUSE THE CORPUS WAS PIECE OF CRAP
    :param path: path to corpus
    :return: less crappy corpus
    """
    f = open(path)
    lines = f.readlines()
    out = open('data/out.txt', 'w')
    for line in lines:
        if '<question>' in line or '<Answer>' in line:
            out.write(line)
    f.close()
    out.close()


def xml_to_better_xml(path_to_talaa='data/out.txt'):
    """
    :param path_to_talaa: path to the corpus
    :return: cleaned file containing only questions and their responses
    """
    root = cet.Element('corpus')
    f = open(path_to_talaa)
    lines = f.readlines()
    i = 1
    type_flag = ''
    for line in lines:
        if '<question>' in line:
            type_flag = 'q'
            line = line.replace('<question>', '')
            line = line.replace('</question>', '')
        elif '<Answer>' in line:
            type_flag = 'a'
            line = line.replace('<Answer>', '')
            line = line.replace('</Answer>', '')
        else:
            continue
        line = line.lstrip().rstrip()
        if type_flag == 'q':
            instance = cet.SubElement(root, 'instance', id=str(i))
            i += 1
        qa = cet.SubElement(instance, type_flag)
        # cleaning line
        line = re.sub(r"([?.!,؟;])", r" \1 ", line)
        line = re.sub(r'[" "]+', " ", line)
        qa.text = line

    xmlstr = minidom.parseString(cet.tostring(root)).toprettyxml(indent="    ")
    with open('data/cleaned_corpus.xml', 'w', encoding='utf-8') as f:
        f.write(xmlstr)
    f.close()


xml_to_better_xml()
# def more_clean(path_to_talaa='../data/cleaned_corpus.xml'):
