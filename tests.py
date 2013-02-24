#!/usr/bin/python
#-*-coding:utf-8-*-
import unittest
from yandex_translate import *


class YandexTranslateTest(unittest.TestCase):
    def setUp(self):
        self.translate = YandexTranslate()

    def test_langs(self):
        languages = self.translate.langs
        self.assertGreater(len(languages), 1)

    def test_cached_languages(self):
        languages = self.translate.langs
        self.translate.api_urls['langs'] = 'http://none.local/%s'
        cached_languages = self.translate.langs
        self.assertEqual(languages, cached_languages)

    def test_not_cached_languages(self):
        with self.assertRaises(YandexTranslateException, msg="ERR_SERVICE_NOT_AVAIBLE"):
            self.translate.api_urls['langs'] = 'http://none.local/%s'
            self.translate.langs

    def test_language_detection(self):
        language = self.translate.detect(text='Hello, world!')
        self.assertEqual(language, 'en')

    def test_language_detection_raising(self):
        with self.assertRaises(YandexTranslateException, msg="ERR_LANG_NOT_SUPPORTED"):
            self.translate.detect('なのです')

    def test_translate(self):
        result = self.translate.translate('Hello, world!', 'ru')
        self.assertEqual(result['text'][0], u'Здравствуй, мир!')
        self.assertEqual(result['code'], 200)

    def test_translate_langs_raising(self):
        with self.assertRaises(YandexTranslateException, msg="ERR_LANG_NOT_SUPPORTED"):
            self.translate.translate('なのです', 'ru')

    def test_translate_network_error_raising(self):
        self.translate.api_urls['translate'] = 'http://none.local/%s'
        with self.assertRaises(YandexTranslateException, msg="ERR_SERVICE_NOT_AVAIBLE"):
            self.translate.translate('Hello, world!', 'en')


if __name__ == '__main__':
    unittest.main()
