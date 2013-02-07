# coding: utf-8

from distutils.core import setup
import yandex_translate

setup(name='yandex_translate',
      version=yandex_translate.__version__,
      description='Python library for Yandex Translate API.',
      packages=['yandex_translate'],
      package_dir={'yandex_translate': 'yandex_translate'},
      provides=['yandex_translate'],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
      long_description=open('README.md').read(),
      platforms=['All'],
      )
