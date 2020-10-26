from NLP.classifier.rules import OBJECTS, VERBS, TIME_OBJECTS, PLACE_OBJECTS, APP_OBJECTS


def parser(req_words):
    """parse and match the request with the RULES and return an exit status
    the parser build a bottom up verification"""
    # verify the validity of every word in the request

    tags = []
    app = ''
    verb = ''
    for word in req_words:
        if word in VERBS:
            tags.append('VERB')
            verb = word
        elif word in TIME_OBJECTS:
            tags.append('TIME_OBJECT')
        elif word in PLACE_OBJECTS:
            tags.append('PLACE_OBJECT')
        elif word in APP_OBJECTS:
            tags.append('APP_OBJECT')
            app = word
        else:
            tags.append('NONE')

    # Verifying the validity of the request by matching it with the rules
    # Note that the request could have valid syntax (valid = 1) but
    # semantically wrong this issue is handled in response generation
    valid = False
    if len(tags) == 1 and tags[0] == 'VERB':
        valid = True
    elif tags[0] == 'VERB':
        for i in range(1, len(tags)):
            if tags[i] not in OBJECTS:
                break
        valid = True

    return valid, app, verb, tags
