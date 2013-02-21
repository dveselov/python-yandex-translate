#!/usr/bin/python
#-*- coding:utf-8 -*-

__version__ = "0.1"

try:
    from urllib import urlopen, urlencode
except:
    from urllib.request import urlopen
    from urllib.parse import urlencode
from json import loads


class YandexTranslateException(Exception):
    """
    >>> YandexTranslateException("DoctestError")
    YandexTranslateException('DoctestError',)
    """
    pass


class YandexTranslate(object):
    """
    Class for detect language of text and translate it via Yandex.Api
    >>> translate = YandexTranslate()
    """
    def __init__(self):
        """
        Class constructor
        @in: None
        @out: None
        >>> translate = YandexTranslate()
        >>> len(translate.api_urls)
        3
        >>> len(translate.error_codes)
        3
        """
        self.cache = {
            'languages': None,
        }
        self.api_urls = {
            'get_langs': 'http://translate.yandex.net/api/v1/tr.json/'
            'getLangs?%s',
            'detect': 'http://translate.yandex.net/api/v1/tr.json/detect?%s',
            'translate': 'http://translate.yandex.net/api/v1/tr.json/'
            'translate?%s',
        }
        self.error_codes = {
            413: "ERR_TEXT_TOO_LONG",
            422: "ERR_UNPROCESSABLE_TEXT",
            501: "ERR_LANG_NOT_SUPPORTED",
        }

    @property
    def langs(self):
        """
        Returns a array of languages for translate
        @in: None
        @out: Array strings
        >>> translate = YandexTranslate()
        >>> languages = translate.langs
        >>> len(languages) > 0
        True
        """
        result = urlopen(self.api_urls['get_langs']).read()
        return loads(result.decode("utf-8"))['dirs']

    def detect(self, text, format='plain'):
        """
        Specifies the language of the text
        @in: text='Hello, world', format=['plain', 'html']
        @out: dict={'code': 200, 'lang': 'en'}
        >>> translate = YandexTranslate()
        >>> result = translate.detect(text='Hello, world!')
        >>> result['code']
        200
        >>> len(result['lang'])
        2
        >>> translate.detect('なのです')
        Traceback (most recent call last):
        YandexTranslateException: ERR_LANG_NOT_SUPPORTED
        """
        data = urlencode({'text': text, 'format': format})
        result = loads(
            urlopen(self.api_urls['detect'] % data).read().decode("utf-8"))
        if not result['lang']:
            raise YandexTranslateException(self.error_codes[501])
        return result

    def translate(self, text, lang, format='plain'):
        """
        Translate text to passed language
        @in: text='Hello, world!', language='ru', format=['plain', 'html']
        @out: dict={'lang': 'en-ru', 'text': 'Hello, world!', 'code': 200}
        >>> translate = YandexTranslate()
        >>> result = translate.translate(lang='ru', text='Hello, world!')
        >>> result['code']
        200
        >>> len(result['lang'])
        5
        """
        data = urlencode({'text': text, 'format': format, 'lang': lang})
        result = urlopen(self.api_urls['translate'] % data).read()

        try:
            json = loads(result.decode("utf-8"))
        except ValueError:
            raise YandexTranslateException(result)

        if json['code'] in self.error_codes:
            raise YandexTranslateException(self.error_codes[json['code']])
        else:
            return json
if __name__ == "__main__":
    import doctest
    doctest.testmod()
