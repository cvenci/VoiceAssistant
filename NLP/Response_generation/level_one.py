from NLP.classifier.classifier_main import xml_req_parse


def arguments_extraction(req_xml, app, app_stm):
    """
    :param req_xml: path to the request XML
    :param app: returned app from classifier
    :param app_stm: returned stemmed app from the classifier
    :return: arguments of the request
    """
    req_words = xml_req_parse(req_xml)
    