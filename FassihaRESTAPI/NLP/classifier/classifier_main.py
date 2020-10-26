"""*Reading and preparing the xml request to be classified
    *passing the request to levels to be classified
    *receiving the classification response and processing the response"""

from os import listdir
from os.path import isfile, join
from xml.etree import ElementTree as ET
import operator

from NLP.classifier.level_zero import parser
from NLP.classifier.level_one import app_req_similarity


def xml_req_parse(req_file_path):
    """
    :param req_file_path: path to the request xml file to be parsed
    :return: a list of normalized request words & list of stemmed request words
    """
    req_words = []
    stem_req_words = []

    req_tree = ET.parse(req_file_path)
    req_root = req_tree.getroot()
    for child in req_root.find('tokenization'):
        if child.attrib['stop_word'] == 'False':
            child.attrib['value'].replace('أ', 'ا')
            child.attrib['value'].replace('ة', 'ه')
            if child.attrib['value'][0:2] == 'ال':
                req_words.append(child.attrib['value'][2:])
            else:
                req_words.append(child.attrib['value'])
            stem_req_words.append(child.attrib['stem'])
    return req_words  # stem_req_words


def xml_app_parse(app_file_path):
    """
    :param app_file_path:
    :return: tuple containing key words of a giving app
    """
    app_words = []
    app_tree = ET.parse(app_file_path)
    app_root = app_tree.getroot()
    for child in app_root.find('word_set'):
        child.attrib['value'].replace('أ', 'ا')
        child.attrib['value'].replace('ة', 'ه')
        app_words.append(child.attrib['value'])
    return app_words


def classify_zero_or_one(xml_req_path, apps_path='../data/apps_data/'):
    """
    :param apps_path: path to the apps XML files
    :param xml_req_path: path to the request file to classify
    :return: classify the request to be treated as level 0 or 1
    """
    req_words = xml_req_parse(xml_req_path)
    app_files = [f for f in listdir(apps_path) if isfile(join(apps_path, f))]
    sim_scores = {}
    stemmed_sim_score = {}
    results = {}
    level0, app, verb, level0_tags = parser(req_words)
    if level0:
        results['level'] = 0
        results['verb'] = verb
        results['app'] = app
        results['args'] = level0_tags
        return results

    for app in app_files:
        app_words = xml_app_parse(join(apps_path, app))
        sc, ssc = app_req_similarity(app_words, req_words)
        sim_scores[app] = sc
        stemmed_sim_score[app] = ssc
    max_sc_app = max(sim_scores.items(), key=operator.itemgetter(1))
    max_ssc_app = max(stemmed_sim_score.items(), key=operator.itemgetter(1))

    results['level'] = 1

    if float(max_sc_app[1]) >= 0.30:
        results['app'] = max_sc_app[0]
        results['score'] = max_sc_app[1]
    else:
        results['app'] = 'None'
        results['score'] = 0

    if float(max_ssc_app[1]) >= 0.30:
        results['s_app'] = max_ssc_app[0]
        results['s_score'] = max_ssc_app[1]
    else:
        results['s_app'] = 'None'
        results['s_score'] = 0
    results['args'] = ''

    return results


# a, b, c , e, f= classify_zero_or_one('../data/user_requests/req2.xml', '../data/apps_data')
# print(a, b, c)
