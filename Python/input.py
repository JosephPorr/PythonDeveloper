# the result of the input() function is a string.
# A string containing all the characters the user enters from the keyboard. It is not an integer or a float.
# Cannot use it as an argument of any arithmetic operation, e.g., you can't use this data to square it, divide it by anything, or divide anything by it.

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

