
from NLP.nlp.classifier import rules
r = rules.RULES
def parser(RULES, req_words=''):
    """parse and match the request with the RULES and return an exit status"""
    print(RULES)
parser(r)