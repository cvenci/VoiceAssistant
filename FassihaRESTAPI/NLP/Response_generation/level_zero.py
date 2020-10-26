"""
Here we generate a response for the level0 request, to be sent to the client
"""
# Initialization of key words of every available app
exit_keys = ["اخرج", "اغلق"]
weather_keys = ['طقس', 'احوال', 'جويه']
clock_keys = ["ساعة", "منبه"]
calculator_keys = ["حاسبه"]
music_keys = ["موسيقى"]
facebook_keys = ["فيسبوك"]
instagram_keys = ["انستغرام"]


def generate(results):
    """
    :param results: results received from the classifier
    :return: A response dictionary corresponding to a response object
    """
    response = {'level': results['level'], 'command': results['command']}
    if results['verb'] in exit_keys:
        results['app_id'] = -1
        results['core'] = 'خروج'
        return results
    if results['app'] in weather_keys:
        response['app_id'] = 1
        response['core'] = 'فتح تطبيق الطقس'
    elif results['app'] in clock_keys:
        response['app_id'] = 2
        response['core'] = 'فتح تطبيق الساعة'
    elif results['app'] in calculator_keys:
        response['app_id'] = 3
        response['core'] = 'فتح تطبيق الحاسبة'
    elif results['app'] in facebook_keys:
        response['app'] = 4
        response['core'] = 'فتح تطبيق فيسبوك'
    elif results['app'] in instagram_keys:
        response['app_id'] = 5
        response['core'] = 'فتح تطبيق انستغرام'
    elif results['app'] in music_keys:
        response['app_id'] = 6
        response['core'] = 'فتح تطبيق الموسيقى'
    else:
        response['app_id'] = 0
        response['core'] = 'نعتذر التطبيق الذي طلبتموه غير متاح'

    response['args'] = results['args']

    return response
