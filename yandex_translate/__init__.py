#!/usr/bin/python
#-*-coding:utf-8-*-

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
        >>> type(translate.api_urls)
        <type 'dict'>
        >>> len(translate.api_urls)
        3
        """
        self.api_urls = {
            'get_langs': 'http://translate.yandex.net/api/v1/tr.json/getLangs?%s',
            'detect': 'http://translate.yandex.net/api/v1/tr.json/detect?%s',
            'translate': 'http://translate.yandex.net/api/v1/tr.json/translate?%s',
        }

    @property
    def langs(self):
        """
        Returns a array of languages for translate
        @in: None
        @out: Array strings
        >>> translate = YandexTranslate()
        >>> languages = translate.langs
        >>> type(languages)
        <type 'list'>
        >>> len(languages) > 0
        True
        """
        result = urlopen(self.api_urls['get_langs']).read()
        return loads(result.decode("utf-8"))['dirs']

    def detect(self, text, format='plain'):
        """
        Specifies the language of the text
        @in: text='Hello, world', format=['plain', 'html']
        @out: String with language code
        >>> translate = YandexTranslate()
        >>> result = translate.detect(text='Hello, world!')
        >>> result['code']
        200
        >>> result['lang']
        u'en'
        """
        data = urlencode({'text': text, 'format': format})
        result = urlopen(self.api_urls['detect'] % data).read()
        return loads(result.decode("utf-8"))

    def translate(self, lang, text, format='plain'):
        """
        Translate text to passed language
        @in: language='ru', text='Hello, world!', format=['plain', 'html']
        @out: dict={'lang': 'en-ru', 'text': 'Hello, world!', 'code': 200}
        >>> translate = YandexTranslate()
        >>> result = translate.translate(lang='ru', text='Hello, world!')
        >>> result['code']
        200
        >>> result['lang']
        u'en-ru'
        """
        data = urlencode({'text': text, 'format': format, 'lang': lang})
        result = urlopen(self.api_urls['translate'] % data).read()

        try:
            json = loads(result.decode("utf-8"))
        except ValueError:
            raise YandexTranslateException(result)

        if json['code'] == 413:
            raise YandexTranslateException('ERR_TEXT_TOO_LONG')
        elif json['code'] == 422:
            raise YandexTranslateException('ERR_UNPROCESSABLE_TEXT')
        elif json['code'] == 501:
            raise YandexTranslateException('ERR_LANG_NOT_SUPPORTED')
        else:
            return json
