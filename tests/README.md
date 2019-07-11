# Unit Test Organization
It is currently my understanding that submodules in a unit test package generally follow a test_submodule.py convention like so...  
```
project\
├── package\
│   ├── __init__.py
│   ├── submodule1.py
│   └── submodule2.py
└── tests\
    ├── __init__.py
    ├── test_submodule1.py
    └── test_submodule2.py
```
That is to say that entire test modules are not _usually_ dedicated to singular functions.  

However, that will be the case here. The `number2text` and `text2number` functions were written to encapsulate behavior that is very loosely predicated on the format of their inputs, which in turn explodes the number of potential test cases and clutters up a module otherwise indented to test a more diverse set of functionality. There is a great case to be made for refactoring these functions into a more specific API. Said API would probably be extensive enough to warrant its own submodule, which would then have it's own testing submodule. This would have been the design from the start if I had more foresight. Maybe I'll get to it one day, but it's not like this is the first time someone's ignored the [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle) (looking at you [`pandas.read_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)).  
