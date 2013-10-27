python-yandex-translate ![Build Status](https://travis-ci.org/dieselpoweredkitten/python-yandex-translate.png)
=======================

Python module for Yandex.Translate API.

This module is fully-compatible with Python 2.7+ and 3.3+ versions.


Installation
======================
Use `pip`:

```bash
pip install yandex.translate
```

Or `easy_install`:

```bash
easy_install yandex.translate
```


Usage
=======================


```python
from yandex_translate import *
translate = YandexTranslate('Your API key here.')
print('Current languages:', translate.langs)
print('Detect language:', translate.detect('Привет, мир!'))
print('Translate:', translate.translate('Привет, мир!', 'ru-en'))  # or just 'en'
```

This will output:

```
Current languages:  ['ru-en', 'ru-pl', 'ru-uk', 'ru-de', 'ru-fr', 'ru-es', 'ru-it', 'ru-tr', 'en-ru', 'en-uk', 'en-de', 'en-tr', 'pl-ru', 'pl-uk', 'uk-ru', 'uk-en', 'uk-pl', 'uk-de', 'uk-fr', 'uk-es', 'uk-it', 'uk-tr', 'de-ru', 'de-en', 'de-uk', 'fr-ru', 'fr-uk', 'es-ru', 'es-uk', 'it-ru', 'it-uk', 'tr-ru', 'tr-en', 'tr-uk']

Detect language: {'code': 200, 'lang': 'ru'}

Translate: {'text': ['Hello, world!'], 'code': 200, 'lang': 'ru-en'}
```
