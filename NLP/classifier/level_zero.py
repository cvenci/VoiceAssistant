from NLP.classifier.rules import VERBAL_PHRASE, OBJECTS, VERBS, TIME_OBJECTS, PLACE_OBJECTS, APP_OBJECTS


def parser(req_words):
    """parse and match the request with the RULES and return an exit status
    the parser build a bottom up verification"""
    tags = []
    for word in req_words:
        if word in VERBS:
            tags.append('VERB')
        elif word in TIME_OBJECTS:
            tags.append('TIME_OBJECT')
        elif word in PLACE_OBJECTS:
            tags.append('PLACE_OBJECT')
        elif word in APP_OBJECTS:
            tags.append('APP_OBJECT')
        else:
            tags.append('NONE')
    print(tags)
    # Verifying the validity of the request by matching it with the rules
    valid = 0
    if len(tags) == 1 and tags[0] == 'VERB':
        valid = 1
    elif tags[1] == 'VERB':
        for i in range(1, len(tags)):
            if tags[i] not in OBJECTS:
                break
            else:
                valid = 1
    print(valid)
    print(OBJECTS)
    print('APP_OBJECTS' in OBJECTS)
