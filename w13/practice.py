

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
    
with MyContext() as obj:
    print(obj)
    raise ValueError

