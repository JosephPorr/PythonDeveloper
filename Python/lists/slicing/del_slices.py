myList = [10, 8, 6, 4, 2]
del myList[1:3]  # del from the 1st postion and the 3rd position -1.
print(myList)
# output [10, 4, 2]

###

# Deleting all the elements at once is possible too
myList = [10, 8, 6, 4, 2]
del myList[:]
print(myList)
# output []

###
# The del instruction will delete the list itself, not its content.

myList = [10, 8, 6, 4, 2]
del myList
print(myList)
# The print() function invocation from the last line of the code will then cause a runtime error. 

#