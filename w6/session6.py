## Q1:


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

## Doc string len tester
def document_checker():
    """Checks if given function __doc__ is more than
     or equal to 50 chars.
     Returns:
        closure that returns a value that returns true 
        if given func _doc__ is more than 50 chars.
       """
    doc_min_len = 50

    def checker(func):
        if func.__doc__ is not None:
            print(len(func.__doc__))
            if len(func.__doc__) >= doc_min_len:
                return True
        return False
    
    return checker

# dc = document_checker()
# print(dc(add))


## Q2:
def fibonacci_numbers():
    """
    This closure generates fibonocci series
    for each call of next it gets next number.

    Returns:
        Returns next fibonacci number.

    """
    prev = 0
    current = 1

    def next():
        nonlocal prev, current
        temp = prev
        prev = current
        current =  temp + current
        return current
    
    return next

# fib_num = fibonacci_numbers()
# [print(fib_num()) for i in range(0,10)]

## Q3: function tracker

func_count_tracker = {}

def function_tracker(fn):
    """
    It is a decorator that counts how many times the function
    is called. At global level this decorator keeps track of this.

    Returns:
        Returns the closure, that tracks the function call count
    """
    def track(*args,**kwargs):
        global func_count_tracker
        print(f'Closure triggred by {fn.__name__}')
        if fn.__name__ in func_count_tracker:
            func_count_tracker[fn.__name__] += 1
        else:
            func_count_tracker[fn.__name__] = 1
        return fn(*args,**kwargs)
    # print(func_count_tracker)
    return track

# @function_tracker
# def add(a,b):
#     return a+b

# @function_tracker
# def mul(a,b):
#     return a*b
# @function_tracker
# def div(a,b):
#     return a/b

# print(add(3,4))
# print(mul(3,4))
# print(div(3,4))
# print(mul(3,4))
# print(div(3,4))
# print(func_count_tracker)

## Q4: function tracker modified

func_count_tracker_modified_dist = {}

def func_count_tracker_modified(dist={}):
    """
        It is a decorator that counts how many times the function 
        is called with custom dist. At global level this decorator keeps track of this.

        Returns:
            Returns the decorator,which has closure in it, that tracks the function call count
    """
    def function_tracker_inner(fn):
        """
        It is a decorator that counts how many times the function
        is called. At global level this decorator keeps track of this.

        Returns:
            Returns the closure, that tracks the function call count
        """
        def track(*args,**kwargs):
            global func_count_tracker_modified_dist
            if dist[fn.__name__]: ## If the func exists in dist it will be tracked else not
                print(f'Closure triggred by {fn.__name__}')
                if fn.__name__ in func_count_tracker_modified_dist:
                    func_count_tracker_modified_dist[fn.__name__] += 1
                else:
                    func_count_tracker_modified_dist[fn.__name__] = 1
            return fn(*args,**kwargs)
        # print(func_count_tracker_modified_dist)
        return track
    return function_tracker_inner


# control_dist = {'add':True,
#                 'sub':True,
#                 'mul':False}

# @func_count_tracker_modified(control_dist)
# def add(a,b):
#     return a+b

# @func_count_tracker_modified(control_dist)
# def mul(a,b):
#     return a*b

# @func_count_tracker_modified(control_dist)
# def div(a,b):
#     return a/b

# print(add(3,4))
# print(mul(3,4))
# print(div(3,4))
# print(mul(3,4))
# print(div(3,4))
# print(func_count_tracker_modified_dist)