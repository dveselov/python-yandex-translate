#!/usr/bin/python
#-*-coding:utf-8-*-
from yandex_translate import *


translate = YandexTranslate()
print('Current languages: ', translate.langs)
print('Detect language:', translate.detect('Привет, мир!'))
print('Translate:', translate.translate('ru-en', 'Привет, мир!'))
