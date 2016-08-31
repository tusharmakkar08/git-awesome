__author__ = 'tusharmakkar08'

from setuptools import setup

setup(
    # Application name:
    name="git-awesome",

    # Version number:
    version="1.0.0",

    # Application author details:
    author="Tushar Makkar",
    author_email="tusharmakkar08@gmail.com",

    # Packages
    py_modules=['git_awesome'],

    package_data={'': ['*.md']},

    license='MIT',
    platforms=['any'],
    # Details
    url="https://github.com/tusharmakkar08/git-awesome",

    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    description="Git delete merged branches",

    long_description=open("README.rst").read(),

    entry_points={
        'console_scripts': [
            'git-awesome=git_awesome:git_awesome',
        ]
    },

)
