#!/usr/bin/python
#-*-coding:utf-8-*-
import unittest
from httpretty import *
from yandex_translate import *


class YandexTranslateTest(unittest.TestCase):
    def setUp(self):
        self.translate = YandexTranslate('trnsl.1.1.20130421T140201Z.323e508a33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e')

    def test_langs(self):
        languages = self.translate.langs
        self.assertGreater(len(languages), 1)

    def test_cached_languages(self):
        languages = self.translate.langs
        self.translate.api_urls['langs'] = 'http://none.local/%s'
        cached_languages = self.translate.langs
        self.assertEqual(languages, cached_languages)

    def test_language_detection(self):
        language = self.translate.detect(text='Hello, world!')
        self.assertEqual(language, 'en')

    def test_translate(self):
        result = self.translate.translate('Hello, world!', 'ru')
        self.assertEqual(result['text'][0], u'Здравствуй, мир!')
        self.assertEqual(result['code'], 200)

    def test_language_detection_error(self):
        with self.assertRaises(YandexTranslateException, msg="ERR_LANG_NOT_SUPPORTED"):
            self.translate.detect('なのです')

    def test_translate_error(self):
        with self.assertRaises(YandexTranslateException, msg="ERR_LANG_NOT_SUPPORTED"):
            self.translate.translate('なのです', 'ru')

    def test_languages_network_error(self):
        with self.assertRaises(YandexTranslateException, msg="ERR_SERVICE_NOT_AVAIBLE"):
            self.translate.api_urls['langs'] = 'http://none.local/%s'
            self.translate.langs

    def test_detection_network_error(self):
        with self.assertRaises(YandexTranslateException, msg="ERR_SERVICE_NOT_AVAIBLE"):
            self.translate.api_urls['detect'] = 'http://detect.local/?%s'
            self.translate.detect(text='Hello, world!')

    def test_translate_network_error(self):
        self.translate.api_urls['translate'] = 'http://none.local/%s'
        with self.assertRaises(YandexTranslateException, msg="ERR_SERVICE_NOT_AVAIBLE"):
            self.translate.translate('Hello, world!', 'en')

    def test_without_key(self):
        with self.assertRaises(YandexTranslateException, msg="Please, provide key for Yandex.Translate API: https://translate.yandex.ru/apikeys"):
            translate = YandexTranslate()

    @httprettified
    def test_languages_invalid_json(self):
        HTTPretty.register_uri(HTTPretty.GET, self.translate.api_urls['langs'],
                               body='[this{is)invalid JSON}',
                               content_type="application/json")
        with self.assertRaises(YandexTranslateException):
            self.translate.langs

    @httprettified
    def test_detection_invalid_json(self):
        HTTPretty.register_uri(
            HTTPretty.GET, self.translate.api_urls['detect'],
            body='[this{is)invalid JSON}',
            content_type="application/json")
        with self.assertRaises(YandexTranslateException):
            self.translate.detect(text='Hello, world!')

    @httprettified
    def test_translate_invalid_json(self):
        HTTPretty.register_uri(
            HTTPretty.GET, self.translate.api_urls['translate'],
            body='[this{is)invalid JSON}',
            content_type="application/json")
        with self.assertRaises(YandexTranslateException):
            self.translate.translate(text='Hello, world!', lang='ru')


if __name__ == '__main__':
    unittest.main()
