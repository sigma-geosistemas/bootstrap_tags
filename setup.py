# coding: utf-8
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
	README = readme

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bootstrap_tags',
    version='0.1',
    packages=['bootstrap_tags'],
    include_package_data=True,
    license='Proprietária',  # example license
    description='Aplicação da SIGMA Geosistemas para facilitar a integração entre o bootstrap e o Django',
    long_description=README,
    url='http://www.sigmageosistemas.com.br',
    author='George Silva',
    author_email='george@consultoriasigma.com.br',
    install_requires=['django-widget-tweaks',],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Proprietária',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)