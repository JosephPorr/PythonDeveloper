# defines a function that closes a function.

def greeter(prefix):  # Will define a function internally.
    def greet(name):  # this will call out a name.
        print(f"{prefix} {name}")
    return greet # Returns the greet fucntion.

hello = greeter("Hello,")
goodbye = greeter("Goodbye,")

hello("Joe")
goodbye("Joe")