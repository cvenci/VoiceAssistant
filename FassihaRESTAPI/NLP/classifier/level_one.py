"""
Calculating the similarity between the user query
and the xml description of applications and affect
the query to an application (as a basic query)
or to the advanced queries model
"""

from nltk.stem.isri import ISRIStemmer


# naive methode
def app_req_similarity(app_words, req_words):
    """
    :param app_words:
    :param req_words:
    :return:Return the similarity (a score) between the request and a given app
            2 approaches are used (with and without stemming)
    """

    stemmer = ISRIStemmer()
    count_dict = {}
    stemmed_count_dict = {}

    # start calculating similarity
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
    print(score, stemmed_score)
    return score, stemmed_score
