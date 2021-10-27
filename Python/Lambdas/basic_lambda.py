# A lambda is a function that don’t have names. 
# Simply put, a lambda function is just like any normal python function, 
# except that it has no name when defining it, 
# and it is contained in one line of code. 
# A lambda function evaluates an expression for a given argument. 
# You give the function a value (argument) and then provide the operation (expression).

def square(num):  # defining the function, def calls the name that defines the parameters a, b
    return num * num 

square_lambda = lambda num: num * num

#both the def and lambda have the same outcome.
#assert is used to test comparisons.

assert square(4) == square_lambda(4)

# in cmd term, $python learning_lambda.py
# no results will confirm the def & lambda are the same
# there will be an error printed otherwise.