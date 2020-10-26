"""This file provide a set of rules to be parsed by the level0 requests classifier"""
'''
RULES = ['S->VERBAL_PHRASE',
         'VERBAL_PHRASE->VERB/VERB OBJECTS',
         'OBJECTS->TIME_OBJECT/PLACE_OBJECT/APP_OBJECT/OBJECTS'
         ]

# FINALS should be without 'ال' and without the Hamza
FINALS = ['VERB->افتح/اغلق/ادخل/ابحث',
          'TIME_OBJECT->غدا/امس/الان',
          'PLACE_OBJECT->هنا/جزائر/امريكا',
          'APP_OBJECT->تطبيق/طقس/ساعة/لعبة']
'''
# TESTING A NEW APPROACH
VERBAL_PHRASE = ['VERB/VERB OBJECTS']
OBJECTS = ['TIME_OBJECT', 'PLACE_OBJECT', 'APP_OBJECT']

VERBS = ['افتح', 'اغلق', 'ادخل', 'ابحث', 'اخرج']
TIME_OBJECTS = ['غدا', 'امس', 'الان']
PLACE_OBJECTS = ['امريكا', 'جزائر', 'هنا']
APP_OBJECTS = ['لعبة', 'احوال', 'جويه', 'ساعة', 'طقس', 'تطبيق', 'انستغرام', 'حاسبه', 'موسيقى']
