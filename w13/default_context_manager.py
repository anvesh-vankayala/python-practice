from contextlib import contextmanager
import csv
from collections import namedtuple


def just_iterator(Row,reader,delimiter):
    """
    Just generator
    """
    for ro in reader:
        row_striped = tuple(ro[0].split(delimiter)) if delimiter==';' else tuple(ro)
        nt = Row(*row_striped)
        yield nt


@contextmanager
def custom_cntx_generator(file_path):
    """
    - context manager is used from context lib.
    - finally is used to handle file closing etc.
    - for lazy loading just_iterator is created to yeild value in the form of named tuples.
    """
    try:
        f = open(file=file_path, mode='r')
        column_names = next(f)
        reader = csv.reader(f)
        delimiter = ';' if ';' in column_names.strip('\n') else ','
        Row = namedtuple('Row', column_names.strip('\n').split(delimiter))
        yield just_iterator(Row,reader,delimiter)
    finally:
        if not f.closed:
            f.close()
        print('Exiting the context and cleaning')


with custom_cntx_generator('/workspaces/python-practice/w13/cars.csv') as data:
    for r in data:
        print(r)

print('################################################################################################################################################')


with custom_cntx_generator('/workspaces/python-practice/w13/personal_info.csv') as data:
    for r in data:
        print(r)



