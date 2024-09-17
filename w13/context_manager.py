
import csv
from collections import namedtuple


class FileContextIterator:

    def __init__(self,
                 file_path) -> None:
        self.file_path = file_path
        self._f = None
        self.row = None

    def __iter__(self):
        return self
    
    def __next__(self):
        row = next(self._f)
        row_striped = tuple(row.strip('\n').split(';'))
        return self.row(*row_striped)
        # return row_striped

    def __enter__(self):
        self._f = open(file=self.file_path, mode='r')
        column_names = next(self._f)
        self.row = namedtuple('Row', column_names.strip('\n').split(';'))

        return self

    def __exit__(self,exc_type,exc_value,exce_tb):
        if not self._f.closed:
            self._f.close()
        return False


with FileContextIterator('/workspaces/python-practice/w13/cars.csv') as data:
    for r in data:
        print(r)
