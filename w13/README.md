# Module context_manager.py module
- 1,FileContextIterator :
    - It is a iterator with, __iter__ and __next__, which take in csv file path during object creation.
    - Also it has context manager within to with __enter__ and __exit__, where 'enter' is triggered during the open of context and 'exit' is triggred during end of context.
    - It lazyly load data from csv and returns the named tuple dynamically irrespective of the csv columns number and values.