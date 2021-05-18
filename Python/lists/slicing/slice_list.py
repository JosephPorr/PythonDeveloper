# A slice is an element of Python syntax that allows you to make a brand new copy of a list, 
# or parts of a list
# copies the list's contents, not the list's name.

list1 = [1]
list2 = list1[:]  # list2 copies content from list1
list1[0] = 2  # list1 now has the contents of list2
print(list2)

###

# myList[start:end]
# start is the index of the first element included in the slice;
# end is the index of the first element not included in the slice.

# Copying part of the list
myList = [10, 8, 6, 4, 2]
newList = myList[1:3]  # start position:end postion -1 (first position in a list is zero, not 1)
print(newList)

# Start:end Note: not to end but to end - 1. 
# An element with an index equal to end is the first element which does not take part in the slicing.
# Remeber, the first position in the list is Zero
# The start at 1 will be 8
# The end is 3rd position - 1.  The end would be the element 4 but it's not counted, 
# so it's the previous number in the list, 6

#