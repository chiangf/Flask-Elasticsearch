"""
Flask-Elasticsearch
-------------

Flask extension for Elasticsearch integration.
"""
from setuptools import setup


setup(
    name='Flask-Elasticsearch',
    version='0.1',
    url='https://github.com/chiangf/Flask-Elasticsearch',
    license='MIT',
    author='Frank Chiang',
    author_email='ch14ngf@gmail.com',
    description='Flask extension for Elasticsearch integration',
    long_description=__doc__,
    py_modules=['flask_elasticsearch'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)