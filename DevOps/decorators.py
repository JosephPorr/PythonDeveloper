# Python's decorators allow you to extend and modify the behavior of a callable 
# (functions, methods, and classes) without permanently modifying the callable itself. 
# Any sufficiently generic functionality you can “tack on” to an existing class or 
# function's behavior makes a great use case for decoration

# The distinction between referencing a function and calling a function allows us to 
# pass functions into other functions, and return functions from functions.
#A function that receives a function argument and/or returns a function is what's 
# known as a "higher-order function." 

# Inspect gets information about live objects such as modules, classes, methods, functions.

def inspect(func, *args):# * allows to pack or unpact the current function and every function onward.
    def wrapped_func(*args, **kwargs): # ** all keyword args
        print(f"Running {func.__name__}")  # function is an object.  Stored in one variable
        val = func(*args, **kwargs) # ** does the same with keyword arguments
        print(f"Result: {val}")
        return val

    return wrapped_func

@inspect
def combine(a, b):
    return a + b