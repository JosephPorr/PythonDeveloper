# Append new element may be glued to the end of the existing list
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###
# method named append(). It takes its argument's value 
# and puts it at the end of the list which owns the method.
numbers.append(4)

print(len(numbers))
print(numbers)

###
# The insert() method is a bit smarter
# it can add a new element at any place in the list
numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#  the first shows the required location of the element to be inserted; 
# note: all the existing elements that occupy locations to the right of the new element
#  (including the one at the indicated position) are shifted to the right, 
# in order to make space for the new element;
# the second is the element to be inserted.



