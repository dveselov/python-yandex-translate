python-yandex-translate [![Build Status](https://travis-ci.org/tyrannosaurus/python-yandex-translate.png?branch=master)](https://travis-ci.org/tyrannosaurus/python-yandex-translate)
=======================

Python module for Yandex.Translate API.

This module is fully-compatible with Python 2.7+ and 3.3+ versions.


Installation
======================
Use `pip`:

```bash
pip install yandex.translate
```

Usage
=======================


```python
from yandex_translate import YandexTranslate
translate = YandexTranslate('Your API key here.')
print('Languages:', translate.langs)
print('Translate directions:', translate.directions)
print('Detect language:', translate.detect('Привет, мир!'))
print('Translate:', translate.translate('Привет, мир!', 'ru-en'))  # or just 'en'
```

This will output:

```
Languages: {'en', 'el', 'ca', 'it', ..}
Translate directions: ['az-ru', 'be-bg', 'be-cs', ..]
Detect language: 'ru'
Translate: {'text': ['Hello, world!'], 'code': 200, 'lang': 'ru-en'}
```
