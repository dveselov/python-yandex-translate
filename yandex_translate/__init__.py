#!/usr/bin/python
# coding:utf-8

__version__ = "0.3.2"

import requests
from requests.exceptions import ConnectionError


class YandexTranslateException(Exception):
    """
    Default YandexTranslate exception
    >>> YandexTranslateException("DoctestError")
    YandexTranslateException('DoctestError',)
    """
    pass


class YandexTranslate(object):
    """
    Class for detect language of text and translate it via Yandex.Translate API
    >>> translate = YandexTranslate()
    """

    error_codes = {
        401: "ERR_KEY_INVALID",
        402: "ERR_KEY_BLOCKED",
        403: "ERR_DAILY_REQ_LIMIT_EXCEEDED",
        404: "ERR_DAILY_CHAR_LIMIT_EXCEEDED",
        413: "ERR_TEXT_TOO_LONG",
        422: "ERR_UNPROCESSABLE_TEXT",
        501: "ERR_LANG_NOT_SUPPORTED",
        503: "ERR_SERVICE_NOT_AVAIBLE",
    }

    api_urls = {
        'langs': 'https://translate.yandex.net/api/v1.5/tr.json/getLangs',
        'detect': 'https://translate.yandex.net/api/v1.5/tr.json/detect',
        'translate': 'https://translate.yandex.net/api/v1.5/tr.json/translate',
    }

    def __init__(self, key=None):
        """
        Class constructor
        >>> translate = YandexTranslate('trnsl.1.1.20130421T140201Z.323e508a'
            '33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e')
        >>> len(translate.api_urls)
        3
        >>> len(translate.error_codes)
        4
        >>> len(translate.cache)
        1
        """
        if not key:
            raise YandexTranslateException(self.error_codes[401])
        self.api_key = key

    @property
    def langs(self, cache=True):
        """
        Returns a array of languages for translate
        :returns: List with translate derections
        >>> translate = YandexTranslate('trnsl.1.1.20130421T140201Z.323e508a'
            '33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e')
        >>> languages = translate.langs
        >>> len(languages) > 0
        True
        >>> translate.api_urls['langs'] = 'http://langs.local/%s'
        >>> languages = translate.langs # cached languages
        >>> len(languages) > 0
        True
        >>> translate = YandexTranslate()
        >>> translate.api_urls['langs'] = 'http://langs.local/%s'
        >>> translate.langs
        Traceback (most recent call last):
        YandexTranslateException: ERR_SERVICE_NOT_AVAIBLE
        """
        try:
            response = requests.get(self.api_urls['langs'], params={'key': self.api_key})
            response = response.json()
        except ConnectionError:
            raise YandexTranslateException(self.error_codes[503])
        except ValueError:
            raise YandexTranslateException(response)
        try:
            code = response['code']
            raise YandexTranslateException(self.error_codes[code])
        except KeyError:
            pass
        return response['dirs']

    def detect(self, text, format='plain'):
        """
        Specifies the language of the text
        :param text: A string for language detection
        :param format: String with text format. 'plain' or 'html'.
        :returns: String with language code in ISO format. 'en', for example.
        >>> translate = YandexTranslate('trnsl.1.1.20130421T140201Z.323e508a'
            '33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e')
        >>> result = translate.detect(text='Hello, world!')
        >>> result == 'en'
        True
        >>> translate.detect('なのです')
        Traceback (most recent call last):
        YandexTranslateException: ERR_LANG_NOT_SUPPORTED
        >>> translate.api_urls['detect'] = 'http://detect.local/?%s'
        >>> result = translate.detect(text='Hello, world!')
        Traceback (most recent call last):
        YandexTranslateException: ERR_SERVICE_NOT_AVAIBLE
        """
        data = {
            'text': text,
            'format': format,
            'key': self.api_key,
        }
        try:
            response = requests.post(self.api_urls['detect'], data=data)
            response = response.json()
        except ConnectionError:
            raise YandexTranslateException(self.error_codes[503])
        except ValueError:
            raise YandexTranslateException(response)
        try:
            code = response['code']
            raise YandexTranslateException(self.error_codes[code])
        except KeyError:
            if not response['lang']:
                raise YandexTranslateException(self.error_codes[501])
        return response['lang']

    def translate(self, text, lang, format='plain'):
        """
        Translate text to passed language
        :param text: Source text
        :param lang: Result language. 'en-ru' for English to Russian translation or just 'ru' for autodetect source language and translate it to Russian.
        :param format: 'plain' or 'html', with chars escaping or not.
        >>> translate = YandexTranslate('trnsl.1.1.20130421T140201Z.323e508a'
            '33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e')
        >>> result = translate.translate(lang='ru', text='Hello, world!')
        >>> result['code'] == 200
        True
        >>> result['lang'] == 'en-ru'
        True
        >>> result = translate.translate('なのです', 'en')
        Traceback (most recent call last):
        YandexTranslateException: ERR_LANG_NOT_SUPPORTED
        >>> translate.api_urls['translate'] = 'http://translate.local/?%s'
        >>> result = translate.translate(lang='ru', text='Hello, world!')
        Traceback (most recent call last):
        YandexTranslateException: ERR_SERVICE_NOT_AVAIBLE
        """
        data = {
            'text': text,
            'format': format,
            'lang': lang,
            'key': self.api_key
        }
        try:
            response = requests.post(self.api_urls['translate'], data=data)
            response = response.json()
        except ConnectionError:
            raise YandexTranslateException(self.error_codes[503])
        except ValueError:
            raise YandexTranslateException(response)
        try:
            code = response['code']
            raise YandexTranslateException(self.error_codes[code])
        except KeyError:
            pass
        return response

if __name__ == "__main__":
    import doctest
    doctest.testmod()
