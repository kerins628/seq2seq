# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='seq2seq-lstm',
    version='6.2.0a0',
    packages=['seq2seq_lstm'],
    description='Grapheme to phoneme module based on Seq2Seq',
    long_description=long_description,
    url='https://github.com/bond005/seq2seq',
    author='Ivan Bondarenko',
    author_email='bond005@yandex.ru',
    license='Apache License Version 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache License Version 2.0',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='seq2seq lstm keras scikit-learn',
    install_requires=['keras', 'numpy', 'scikit-learn'],
    test_suite = 'tests'
)
