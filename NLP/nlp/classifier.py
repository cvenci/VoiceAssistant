"""
Calculating the similarity between the user query
and the xml description of applications and affect
the query to an application (as a basic query)
or to the advanced queries model
"""
# naive method
from nltk.stem.isri import ISRIStemmer
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
    """return tuple containing the request words"""
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


def similarity(app_words, req_words):
    """Return the similarity (a score) between the request and a given app
    2 approaches are used (with and without stemming)"""
    stemmer = ISRIStemmer()
    count_dict = {}
    stemmed_count_dict = {}
    # calculating stemmed and normal similarity
    for rw in req_words:
        if rw in app_words:
            if rw in count_dict:
                count_dict[rw] += 1
            else:
                count_dict[rw] = 1
        rw_stemmed = stemmer.stem(rw)
        if rw_stemmed in app_words:
            if rw_stemmed in stemmed_count_dict:
                stemmed_count_dict[rw_stemmed] += 1
            else:
                stemmed_count_dict[rw_stemmed] = 1
    # calculating score
    score = 0
    stemmed_score = 0
    for k in count_dict.keys():
        score = score + int(count_dict[k])
    score = score / len(req_words)
    for k in stemmed_count_dict.keys():
        stemmed_score = stemmed_score + int(stemmed_count_dict[k])
    stemmed_score = stemmed_score / len(req_words)
    return score, stemmed_score


sc, ssc = similarity(app_xml_parse('../data/apps_data/weather.xml'), request_xml_parse('../data/user_requests/req2.xml'))
print(sc, ssc)
