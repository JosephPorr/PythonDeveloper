# The for loop is designed to do more complicated tasks - it can "browse" large collections of data item by item. 

for i in range(2, 8):
    print("The value of i is currently", i)

#In this case, the first argument determines the initial (first) value of the control variable.

#The last argument shows the first value the control variable will not be assigned.

#Note: the range() function accepts only integers as its arguments, and generates sequences of integers.
#REPL Output
#>>> for i in range(2, 8):
#...     print("The value of i is currently", i)
#...
#The value of i is currently 2
#The value of i is currently 3
#The value of i is currently 4
#The value of i is currently 5
#The value of i is currently 6
#The value of i is currently 7