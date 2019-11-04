"""
Setup script for conwech package.
"""

import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()
    
    
setuptools.setup(
    name='conwech',
    version='1.0.0',
    author='Kevin Turner',
    author_email='kct0004@auburn.edu',
    description='A module for reading & writing numbers using the Conway-Wechsler naming system',
    long_description=long_description or 'Unable to access README.md during setup!',
    long_description_content_type='text/markdown',
    url='https://github.com/KCATurner/spellnum',
    packages=setuptools.find_packages(exclude=['tests*', ]),
    install_requires=[
        'colorama',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'conwech = conwech.__main__:cli'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
