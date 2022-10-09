# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

import codecs
import os
import platform

_dir = os.path.dirname(__file__)
py_version = platform.python_version()


def finedescription():
    line = ''
    with open(os.path.join(_dir, 'README.rst')) as f:
        line = f.read()
    return line


def find_version():
    f = codecs.open('version', 'r', 'utf-8-sig')
    line = f.readline()
    f.close()
    return line


def install_requires():
    list = []
    with open(os.path.join(_dir, 'requirements.txt')) as f:
        for line in f:
            list.append(line)
    return list


PACKAGE_VERSION = str(find_version())
PACKAGE_LONG_DESCRIPTION = str(finedescription())

setup(
    name="footballex",
    version=PACKAGE_VERSION,
    packages=find_packages(),
    long_description=PACKAGE_LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    zip_safe=False,

    description="egg football.",
    author="pickyman",
    author_email="mkiceman@163.com",
    install_requires=install_requires(),
    license='MIT License',
    keywords=("test", "egg"),

    platforms="Independant",
    url="",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
