"""
This script is the main start point of the voice assistant
"""
from NLP.nlp import tokenizer
from NLP.classifier import classifier_main


def run(command_core):
    """
    :param command_core: The core attribute of the recieved command
    :return: run the integrity of the process
    """
    txt_path = 'NLP/data/user_requests/req2.txt'
    f = open(txt_path, 'w', encoding='utf8')
    f.write(command_core)
    f.close()
    xml_path = tokenizer.request_tokenizing(txt_path, 'NLP/data/user_requests')
    results = classifier_main.classify_zero_or_one(xml_path, 'NLP/data/apps_data')
    print(results)
    if results['level'] == 0:
        print(results['level'])
        return 0, results['app'], results['args']
    if results['level'] == 1:
        print(results['level'])
        if (float(results['score']) >= 0.25 or float(results['s_score']) >= 0.25) \
                and (results['app'] == results['s_app']):
            return 1, results['app'], results['args']

        elif results['app'] != results['s_app']:
            if results['s_score'] >= 0.25:
                return 1, results['s_app'], results['args']
        else:
            return 2, 'None', 'None'
