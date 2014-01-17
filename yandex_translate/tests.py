#!/usr/bin/python
# coding:utf-8
import unittest
from yandex_translate import *


class YandexTranslateTest(unittest.TestCase):

    def setUp(self):
        self.translate = YandexTranslate('trnsl.1.1.20130421T140201Z.323e508a'
                                         '33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e')

    def test_langs(self):
        languages = self.translate.langs
        self.assertGreater(len(languages), 1)

    def test_underscore_langs(self):
        languages = self.translate._langs
        self.assertEqual(languages, set(
            [
                u'el', u'en', u'ca', u'it',
                u'hy', u'cs', u'et', u'az',
                u'es', u'ru', u'nl', u'pt',
                u'no', u'tr', u'lv', u'lt',
                u'ro', u'pl', u'be', u'fr',
                u'bg', u'hr', u'de', u'da',
                u'fi', u'hu', u'sr', u'sq',
                u'sv', u'mk', u'sk', u'uk',
                u'sl'
            ]
        ))

    def test_blocked_key(self):
        translate = YandexTranslate('trnsl.1.1.20130723T112255Z.cfcd2b1ebae9f'
                                    'ff1.86f3d1de3621e69b8c432fcdd6803bb87ef0e963')
        with self.assertRaises(YandexTranslateException):
            languages = translate.detect('Hello!')

    def test_language_detection(self):
        language = self.translate.detect(text='Hello, world!')
        self.assertEqual(language, 'en')

    def test_translate(self):
        result = self.translate.translate(u'Hello!', 'ru')
        self.assertEqual(result['text'][0], u'Здравствуйте!')
        self.assertEqual(result['code'], 200)

    def test_translate_in_another_direction(self):
        result = self.translate.translate(u'Здравствуйте', 'en')
        self.assertEqual(result['text'][0], u'Hello')
        self.assertEqual(result['code'], 200)

    def test_language_detection_error(self):
        with self.assertRaises(YandexTranslateException,
                               msg="ERR_LANG_NOT_SUPPORTED"):
            self.translate.detect('なのです')

    # Yandex.Translate tries to translate this as english-to-russian
    # def test_translate_error(self):
    #     with self.assertRaises(YandexTranslateException,
    #                            msg="ERR_LANG_NOT_SUPPORTED"):
    #         self.translate.translate('なのです', 'ru')

    def test_without_key(self):
        with self.assertRaises(YandexTranslateException,
                               msg="Please, provide key for ' \
                               'Yandex.Translate API: ' \
                               'https://translate.yandex.ru/apikeys"):
            translate = YandexTranslate()

    def test_error_long_text(self):
        with self.assertRaises(YandexTranslateException, 
                               msg="ERR_TEXT_TOO_LONG"):
            self.translate.translate('hi! '*4098, 'ru')

    def test_invalid_key(self):
        with self.assertRaises(YandexTranslateException,
                               msg="ERR_KEY_INVALID"):
            translate = YandexTranslate('my-invalid-key')
            language = translate.detect('Hello!')

if __name__ == '__main__':
    unittest.main()
