#!/usr/bin/python
#-*-coding:utf-8-*-
try:
    from urllib import urlopen, urlencode
except:
    from urllib.request import urlopen
    from urllib.parse import urlencode
from json import loads


class YandexTranslate(object):
    def __init__(self):
        self.api_urls = {
            'get_langs': 'http://translate.yandex.net/api/v1/tr.json/getLangs?%s',
            'detect': 'http://translate.yandex.net/api/v1/tr.json/detect?%s',
            'translate': 'http://translate.yandex.net/api/v1/tr.json/translate?%s',
        }

    def get_langs(self):
        result = urlopen(self.api_urls['get_langs']).read()
        return loads(result.decode("utf-8"))['dirs']

    def detect(self, text, format='plain'):
        data = urlencode({'text': text, 'format': format})
        result = urlopen(self.api_urls['detect'] % data).read()
        return loads(result.decode("utf-8"))

    def translate(self, lang, text, format='plain'):
        data = urlencode({'text': text, 'format': format, 'lang': lang})
        result = urlopen(self.api_urls['translate'] % data).read()
        json = loads(result.decode("utf-8"))
        if json['code'] == 413:
            raise 'ERR_TEXT_TOO_LONG'
        elif json['code'] == 422:
            raise 'ERR_UNPROCESSABLE_TEXT'
        elif json['code'] == 501:
            raise 'ERR_LANG_NOT_SUPPORTED'
        else:
            return json
