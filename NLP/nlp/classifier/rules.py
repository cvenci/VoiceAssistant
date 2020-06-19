"""This file provide a set of rules to be parsed by the level0 requests classifier"""
RULES = ['S->VERBAL_PHRASE',
         'VERBAL_PHRASE->VERB/VERB OBJECTS',
         'OBJECTS->TIME_OBJECT/PLACE_OBJECT/APP_OBJECT/OBJECTS',
         'VERB->افتح/اغلق/ادخل/ابحث',
         'TIME_OBJECT->غدا/امس/الان',
         'PLACE_OBJECT->هنا/الجزائر/امريكا',
         'APP_OBJECT->الطقس/الساعة/اللعبة']
