#!/usr/bin/python


from setuptools import setup, find_packages


setup(
    name = "ari2",
    version = "0.1",
    author = "Vitold Sedyshev",
    author_email = "vit1251@gmail.com",
    description = "Asterisk RESTful Interface",
    keywords = "asterisk rest ari voip telephony",
    package_dir = {'': 'src'},
    packages = find_packages('src'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
    ],
)
