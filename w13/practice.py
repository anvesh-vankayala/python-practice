
## Custom context.
##################################################################################################
class MyContext:
    def __init__(self) -> None:
        self.obj = None

    def __enter__(self):
        print('Entered my context')
        self.obj = 'The return object'
        return self.obj
    
    def __exit__(self,exc_type,exc_val,exc_traceback):
        print('exiting context..')
        if exc_type:
            print(f'*** Error occured :{exc_type}, {exc_traceback}')
        return False  ## If True will supress the exceptions, for False it do not.
    
# with MyContext() as obj:
#     print(obj)
#     raise ValueError

## Named tuple.
##################################################################################################
from collections import namedtuple

Row = namedtuple('Row',['column1','column2','column3'])
r1 = Row('1','2','3')
r2 = Row('4','5','6')
print(r1)
print(r2)
