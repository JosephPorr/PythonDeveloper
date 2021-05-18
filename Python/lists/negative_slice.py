# myList[start:end]
# start is the index of the first element included in the slice;
# end is the index of the first element not included in the slice.

# The 1st postion starts at 8, and zero is the first position is 10.  
# The -1 in the list start from the end and works backwards.
# 2 is the first element not to be included.

myList = [10, 8, 6, 4, 2]
newList = myList[1:-1]  # start position:end position
print(newList)
# output is [8, 6, 4]

###

# If the start specifies an element lying further than the one described by the end 
# (from the list's beginning point of view), the slice will be empty:
myList = [10, 8, 6, 4, 2]
newList = myList[-1:4]
print(newList)
# output is []

###

myList = [10, 8, 6, 4, 2]
newList = myList[:3]  # compact equivalent of mylist[0:3]
print(newList)
# output [10, 8, 6]

###

myList = [10, 8, 6, 4, 2]
newList = myList[3:] # compact equivalent of mylist[3:0]. starts at 4th position, or 4. no end defined
print(newList)
# output [4, 2]

#