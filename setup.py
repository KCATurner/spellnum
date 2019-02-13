import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='spellnum-kcaturner',
    version='0.0.1',
    author='Kevin Turner',
    author_email='kct0004@auburn.edu',
    description='A module for spelling numbers in conventional English short-scale',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/KCATurner/spellnum',
    packages=setuptools.find_packages(exclude=['docs', 'tests*']),
    install_requires=['re'],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
