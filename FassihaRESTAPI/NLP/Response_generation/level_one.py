def generate(results):
    response = {'level': results['level'], 'command': results['command']}
    if results['app_id'] == 'weather.xml':
        response['app_id'] = 1
        response['core'] = 'فتح تطبيق الأحوال الجوية'
    elif results['app_id'] == 'alarm_clock.xml':
        response['app_id'] = 2
        response['core'] = 'فتح تطبيق الساعة'
    elif results['app_id'] == 'calculator.xml':
        response['app_id'] = 3
        response['core'] = 'فتح تطبيق الألة الحاسبة'
    elif results['app_id'] == 'music.xml':
        response['app_id'] = 6
        response['core'] = 'فتح تطبيق الموسيقى'
    response['args'] = results['args']
    return response
