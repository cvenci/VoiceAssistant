"""
Here we generate a response for the level0 request, to be sent to the client
"""


def generate(results):
    """
    :param results: results received from the classifier
    :return: A response dictionary corresponding to a response object
    """
    response = {'level': results['level']}
    if results['app'] == 'الطقس':
        response['app_id'] = 1
        response['core'] = 'فتح تطبيق الطقس'
    else:
        response['app_id'] = 2
        response['core'] = 'فتح تطبيق الساعة'
    response['args'] = results['args']

    return response
