#  TO create yur own function, you have to define it first.

# •	It always starts with the keyword def (for define)
# •	next after def goes the name of the function (the rules for naming functions are exactly the same as for naming variables)
# •	after the function name, there's a place for a pair of parentheses (they contain nothing here, but that will change soon)
# •	the line has to be ended with a colon;
# •	the line directly after def begins the function body - a couple (at least one) of necessarily nested instructions, which will be executed every time the function is invoked; note: the function ends where the nesting ends, so you have to be careful.

def message():  # Message is defined as the prompting function
    print("Enter a value: ")  # nested instructions of the function

print("We start here.")
message() # this is the invocation of the function just created
print("We end here.")

###

# when you invoke a function, Python remembers the place where it happened and jumps into the invoked function;
# the body of the function is then executed;
# reaching the end of the function forces Python to return to the place directly after the point of invocation.

def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

#