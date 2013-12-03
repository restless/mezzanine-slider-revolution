# -*- coding: utf-8 -*-
import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mezzanine-slider-revolution',
    version='0.1',
    packages=['slider_revolution', 'slider_revolution.templatetags', 'slider_revolution.migrations'],
    include_package_data=True,
    license='MIT License',  
    description='Mezzanine plugin that adds support for Slider Revolution.',
    long_description=README,
    url='http://github.com/restless/mezzanine-slider-revolution/',
    author='Jakub Wiśniowski',
    author_email='jakub.wisniowski@natcam.pl',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
	'Framework :: Django',
    ],
)
