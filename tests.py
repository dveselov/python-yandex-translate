#!/usr/bin/python
#-*-coding:utf-8-*-
from yandex_translate import *


translate = YandexTranslate()
print(translate.get_langs())
print(translate.detect('Привет, мир!'))
print(translate.translate('ru-en', 'Привет, мир!'))
