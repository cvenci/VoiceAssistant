"""
This script is the main start point of the voice assistant
"""
from NLP.nlp import tokenizer
from NLP.classifier import classifier_main
from NLP.Response_generation import level_zero
from NLP.Response_generation import level_one
from NLP.Response_generation import level_two


def run(command_core):
    """
    :param command_core: The core attribute of the received command
    :return: run the integrity of the process
    """
    txt_path = 'NLP/data/user_requests/req2.txt'
    f = open(txt_path, 'w', encoding='utf8')
    f.write(command_core)
    f.close()

    xml_path = tokenizer.request_tokenizing(txt_path, 'NLP/data/user_requests')
    results = classifier_main.classify_zero_or_one(xml_path, 'NLP/data/apps_data')
    print(results)
    results['command'] = command_core

    if results['level'] == 0:
        response = level_zero.generate(results)
        return response

    results_s = {}
    if results['level'] == 1:
        results_s['level'] = 1
        results_s['command'] = results['command']
        if ((float(results['score']) >= 0.25 or (float(results['s_score']) >= 0.25))
                and (results['app'] == results['s_app'])):
            results_s['app_id'] = results['app']
            results_s['args'] = results['args']
            response = level_one.generate(results_s)
            return response

        elif results['app'] != results['s_app']:
            if results['s_score'] >= 0.25:
                print('also in level 1 but stemmed')
                results_s['app_id'] = results['s_app']
                results_s['args'] = results['args']
                response = level_one.generate(results_s)
                return response
            elif results['score'] >= 0.25:
                results_s['app_id'] = results['app']
                results_s['args'] = results['args']
                response = level_one.generate(results_s)
                return response

        else:
            response = level_two.generate(results)
            return response
