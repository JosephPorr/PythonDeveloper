myList = [10, 1, 8, 3, 5]
total = 0  # You need a variable whose sum will be stored and initially assigned a value of 0. 
# Note: we're not going to name it sum as Python uses the same name for one of its built-in functions - sum()

for i in range(len(myList)):  # "i" is shorthand variable for "Integer" in the for loop.
    total += myList[i]  # Total is the sum of all the integers in mylist added.

print(total)

###

myList = [10, 1, 8, 3, 5]
total = 0

for i in myList:
    total += i

print(total)

# the for instruction specifies the variable used to browse the list (i here) followed by the in keyword and the name of the list being processed (myList here)
# the i variable is assigned the values of all the subsequent list's elements, and the process occurs as many times as there are elements in the list;
# this means that you use the i variable as a copy of the elements' values, and you don't need to use indices;
# the len() function is not needed here, either.

#