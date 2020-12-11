# Python precisely defines the priorities of all operators, and assumes that operators of a larger (higher) priority 
# perform their operations before the operators of a lower priority.

2 + 3 * 5  # multiplications precede additions.

# Most of Python's operators have left-sided binding, 
# which means that the calculation of the expression is conducted from left to righ

print(9 % 6 % 2)

# from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1;
# from right to left: first 6 % 2 gives 0, and then 9 % 0 causes a fatal error.

#  The result should be 1. This operator has left-sided binding. But there's one interesting exception.