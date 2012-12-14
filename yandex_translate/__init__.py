#!/usr/bin/python
# -*-coding:utf-8-*-

__version__ = "0.1"

try:
    from urllib import urlopen, urlencode
except:
    from urllib.request import urlopen
    from urllib.parse import urlencode
from json import loads


class YandexTranslateException(Exception):
    pass


class YandexTranslate(object):
    def __init__(self):
        self.api_urls = {
            'get_langs': 'http://translate.yandex.net/api/v1/tr.json/getLangs?%s',
            'detect': 'http://translate.yandex.net/api/v1/tr.json/detect?%s',
            'translate': 'http://translate.yandex.net/api/v1/tr.json/translate?%s',
        }

    @property
    def langs(self):
        result = urlopen(self.api_urls['get_langs']).read()
        return loads(result.decode("utf-8"))['dirs']

    def detect(self, text, format='plain'):
        data = urlencode({'text': text, 'format': format})
        result = urlopen(self.api_urls['detect'] % data).read()
        return loads(result.decode("utf-8"))

    def translate(self, lang, text, format='plain'):
        data = urlencode({'text': text, 'format': format, 'lang': lang})
        result = urlopen(self.api_urls['translate'] % data).read()

        try:
            json = loads(result.decode("utf-8"))
        except ValueError:
            raise YandexTranslateException, result

        if json['code'] == 413:
            raise YandexTranslateException, 'ERR_TEXT_TOO_LONG'
        elif json['code'] == 422:
            raise YandexTranslateException, 'ERR_UNPROCESSABLE_TEXT'
        elif json['code'] == 501:
            raise YandexTranslateException, 'ERR_LANG_NOT_SUPPORTED'
        else:
            return json
