#!/usr/bin/python
#-*-coding: utf8-*-

from setuptools import setup, find_packages

setup(
    name="sendcloud",
    version="0.0.1",
    author="fatelei",
    author_email="fatelei@gmail.com",
    description="sendcloud webapi sdk",
    install_requires=["requests"],
    packages=["sendcloud"]
)
