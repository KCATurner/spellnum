"""
Setup script for ConWech package.
"""

import setuptools
import datetime
import os

long_description = None
if os.path.exists('README.md'):
    with open('README.md', 'r') as readme:
        long_description = readme.read()

version = None
if os.path.exists('VERSION'):
    with open('VERSION', 'r') as version:
        version = str(version.read()).strip()

d = datetime.date.today()
setuptools.setup(
    name='conwech',
    version=version or datetime.datetime.now().strftime('%Y.%m'),
    author='Kevin Turner',
    author_email='kct0004@auburn.edu',
    description='A module for reading & writing numbers using the Conway-Wechsler naming system',
    long_description=long_description or 'Unable to access README.md during setup!',
    long_description_content_type='text/markdown',
    url='https://github.com/KCATurner/conwech.git',
    packages=setuptools.find_packages(exclude=['tests*', ]),
    install_requires=[
        'colorama',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'conwech = conwech.__main__:main'
        ]
    },
    python_requires='>=3.4',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
