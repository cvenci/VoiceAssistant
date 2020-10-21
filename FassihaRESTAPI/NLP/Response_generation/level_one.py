def generate(results):
    response = {'level': results['level'], 'command': results['command']}
    if results['app_id'] == 'weather.xml':
        response['app_id'] = 1
        response['core'] = 'فتح تطبيق الأحوال الجوية'
    else:
        response['app_id'] = 2
        response['core'] = 'فتح تطبيق الساعة'
    response['args'] = results['args']

    return response
