"""*Reading and preparing the xml request to be classified
    *passing the request to levels to be classified
    *receiving the classification response and processing the response"""

from xml.etree import ElementTree as ET
def xml_req_parse(req_file_path):
    """return tuple containing the request word set"""
    req_words = []
    req_tree = ET.parse(req_file_path)
    req_root = req_tree.getroot()
    for child in req_root.find('tokenization'):
        if child.attrib['stop_word'] == 'False':
            if child.attrib['value'][0:2] == 'ال':
                req_words.append(child.attrib['value'][2:])
            else:
                req_words.append(child.attrib['value'])
    return req_words
