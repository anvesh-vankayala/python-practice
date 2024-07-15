
def add(a:int,b:int):
    """This methods adds two numbers
     Args:
        a: is integer
        b: is integer
     Returns:
        bool value that returns true if func
        __doc__ is more than 50 chars.
       """
    return a+b
## Q1:
def document_checker():
    """Checks if given function __doc__ is more than
     or equal to 50 chars.
     Returns:
        closure that returns a value that returns true 
        if given func _doc__ is more than 50 chars.
       """
    doc_min_len = 50

    def checker(func):
        print(len(func.__doc__))
        if len(func.__doc__) >= doc_min_len:
            return True
        return False
    
    return checker



# dc = document_checker()
# print(dc(add))