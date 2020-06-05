"""
Calculating the similarity between the user query
and the xml description of applications and affect
the query to an application (as a basic query)
or to the advanced queries model
"""
# naive method
from xml.etree import ElementTree as ET


def app_xml_parse(app_file_path):
    """return tuple containing key words
    of a given app """
    app_words = []
    treeapp = ET.parse(app_file_path)
    rootapp = treeapp.getroot()
    for child in rootapp.find('word_set'):
        app_words.append(child.attrib['value'])
    return app_words


def request_xml_parse(req_file_path):
    """return tuple conntaining the request words"""
    req_words = []
    treereq = ET.parse(req_file_path)
    rootreq = treereq.getroot()
    for child in rootreq.find('tokenization'):
        if child.attrib['stop_word'] == 'False':
            if child.attrib['value'][0:2] == 'ال':
                req_words.append(child.attrib['value'][2:])
            else:
                req_words.append(child.attrib['value'])
    return req_words
