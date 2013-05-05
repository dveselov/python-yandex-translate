# coding: utf-8

from distutils.core import setup
import yandex_translate

setup(name='yandex-translate',
      version=yandex_translate.__version__,
      author="Sofia Velmer",
      author_email="pyth0n3r@yandex.ru",
      description='Python library for Yandex.Translate API.',
      license = "DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE",
      keywords = "yandex yandex-translate translate",
      url = "https://github.com/valmet/python-yandex-translate",
      packages=['yandex_translate'],
      package_dir={'yandex_translate': 'yandex_translate'},
      provides=['yandex_translate'],
      classifiers=[
          'Intended Audience :: Developers',
          'Development Status :: 3 - Alpha',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
      long_description=open('README.md').read(),
      platforms=['All'],
      )
