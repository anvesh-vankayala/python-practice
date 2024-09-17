
import csv
from collections import namedtuple


class FileContextIterator:
    """
    FileContextIterator :
    - It is a iterator with, __iter__ and __next__, 
      which take in csv file path during object creation.
    - Also it has context manager within to with __enter__ and __exit__, 
      where 'enter' is triggered during the open of context and 'exit' is triggred during end of context.
    - It lazyly load data from csv and returns the named tuple dynamically irrespective 
      of the csv columns number and values.
    """

    def __init__(self,
                 file_path) -> None:
        self.file_path = file_path
        self._f = None
        self.row = None

    def __iter__(self):
        return self
    
    def __next__(self):
        row = next(self._f)
        row_striped = tuple(row.strip('\n').split(self.delimiter))
        return self.row(*row_striped)
        # return row_striped

    def __enter__(self):
        self._f = open(file=self.file_path, mode='r')
        column_names = next(self._f)
        self.delimiter = ';' if ';' in column_names.strip('\n') else ','
        self.row = namedtuple('Row', column_names.strip('\n').split(self.delimiter))

        return self

    def __exit__(self,exc_type,exc_value,exce_tb):
        if not self._f.closed:
            self._f.close()
        return False


with FileContextIterator('/workspaces/python-practice/w13/cars.csv') as data:
    for r in data:
        print(r)

print('################################################################################################################################################')

with FileContextIterator('/workspaces/python-practice/w13/personal_info.csv') as data:
    for r in data:
        print(r)