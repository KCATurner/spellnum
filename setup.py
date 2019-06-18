"""
Setup script for spellnum package
"""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='spellnum',
    version='1.0.0',
    author='Kevin Turner',
    author_email='kct0004@auburn.edu',
    description='A module for spelling numbers in conventional English short-scale',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/KCATurner/spellnum',
    packages=setuptools.find_packages(exclude=['tests*', ]),
    entry_points={
        'console_scripts': [
            'spellnum = spellnum.__main__:main'
        ]
    },
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
