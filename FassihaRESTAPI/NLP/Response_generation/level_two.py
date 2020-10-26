import NLP.Response_generation.Deeplearning.use_model as um
from xml.etree import cElementTree as ET


def generate_from_corpus(request,
                         path_to_talaa="NLP/Response_generation/Deeplearning/data/search_corpus.xml"):
    """
    :param request: request to generate response for
    :param path_to_talaa: path to the talaa arabic corpus
    :return: the response to a specific query if it exist in the corpus, "" if not
    """

    requests = []
    responses = []
    tree = ET.parse(path_to_talaa)
    root = tree.getroot()
    for child in root:
        for child2 in child:
            if child2.tag == "q":
                txt = child2.text.replace("؟", "").lstrip().rstrip()
                txt = txt.replace("ة", "ه").replace("أ", "ا")
                requests.append(txt)
            if child2.tag == "a":
                txt = child2.text.replace("؟", "").lstrip().rstrip()
                txt = txt.replace("ة", "ه").replace("أ", "ا")
                responses.append(txt)

    request.replace("ة", "ه")
    request.replace("أ", "ا")
    response = ""
    print(request in requests)
    if request in requests:

        i = requests.index(request)
        response = responses[i]

    return response


def generate(results):
    print("Generating level2 response")
    corpus_response = generate_from_corpus(request=results['command'])
    if corpus_response != "":
        response = {'level': 2, 'app_id': 0, 'args': 'None', 'command': results['command'],
                    'core': corpus_response}
    else:
        response = {'level': 2, 'app_id': 0, 'args': 'None', 'command': results['command'],
                    'core': um.predict(results['command'])}
    return response
