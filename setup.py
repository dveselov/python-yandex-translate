# coding: utf-8

from setuptools import setup

setup(name='yandex.translate',
      version='0.3.5',
      author="yandex.translate contributors",
      author_email="me@require.pm",
      description='Python library for Yandex.Translate API.',
      license="DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE",
      keywords="yandex yandex-translate translate",
      url="https://github.com/dieselpoweredkitten/python-yandex-translate",
      packages=['yandex_translate'],
      package_dir={'yandex_translate': 'yandex_translate'},
      provides=['yandex_translate'],
      classifiers=[
          'Intended Audience :: Developers',
          'Development Status :: 3 - Alpha',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
      ],
      platforms=['All'],
      install_requires=['requests>=1.2.3'],
      )
