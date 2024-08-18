from functools import wraps
from datetime import datetime
from time import perf_counter

# Decorator that allows to run a function only at odd seconds, else prints out "We're even!"
def odd_it(fn: "Function"):
	# MISSING CODE
	kind = datetime.now().second % 2
	def inner(*args, **kwargs):
		if kind != 0:
			result = fn(*args,**kwargs)
			return result
		else:
			return None
	return inner

@odd_it
def add():
	return 3+4

# The same logger that we coded in the class
# it will be tested against a function that will be sent 2 parameters, and 
# it would return some random string. 
def logger(fn: "Function"):
	@wraps(fn)
	def inner(*args,**kwargs):
		start = perf_counter()
		result = fn(*args,**kwargs)
		print(f"{fn.__name__} Execution time : { perf_counter() - start }")
		print(f'function_name : {fn.__name__}, called at {start}')
		print(f'Function description : {help(fn)}')
		print(f"This is a function's writeup : {fn.__doc__}")
		print(f"Function annotation : {fn.__annotations__}")
		return result
	return inner

	


# start with a decorator_factory that takes an argument one of these strings, 
# high, mid, low or no
# then write the decorator that has 4 free variables
# based on the argument set by the factory call, give access to 4, 3, 2 or 1 arguments
# to the function being decorated from var1, var2, var3, var4
# YOU CAN ONLY REPLACE "#potentially missing code" LINES WITH MULTIPLE LINES BELOW
# KEEP THE REST OF THE CODE SAME
def decorator_factory(access:str):
	def accessor(fn): ## decorator
		access_maper = {
			'high' : 4,
			'mid' : 3,
			'low' : 2,
			'no' :1
		}
		@wraps(fn)
		def inner(*args,**kwargs):
			fn(*args,**kwargs)
			return range(0,access_maper[access]) if access in access_maper else 'Improper access keyword set'
		return inner
	return accessor


# The authenticate function. Start with a dec_factory that sets the password. It's inner
# will not be called with "password", *args, **kwargs on the fn
def authenticate(set_password):
	# MISSING CODE
	pass


# The timing function
def timed(reps):
    # MISSING CODE
	pass


