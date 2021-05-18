# If you have a list l1, then the following assignment: l2 = l1 does not make a copy of the l1 list, but makes the variables l1 and l2 point to one and the same list in memory. For example:

vehiclesOne = ['car', 'bicycle', 'motor']
print(vehiclesOne) # outputs: ['car', 'bicycle', 'motor']

vehiclesTwo = vehiclesOne
del vehiclesOne[0] # deletes 'car'
print(vehiclesTwo) # outputs: ['bicycle', 'motor']

###

# If you want to copy a list or part of the list, you can do it by performing slicing:

colors = ['red', 'green', 'orange']

copyWholeColors = colors[:] # copy the whole list
copyPartColors = colors[0:2] # copy part of the list

###

# You can use negative indices to perform slices, too. For example:

sampleList = ["A", "B", "C", "D", "E"]
newList = sampleList[2:-1]
print(newList) # outputs: ['C', 'D']

###

# The start and end parameters are optional when performing a slice: list[start:end], e.g.:

myList = [1, 2, 3, 4, 5]
sliceOne = myList[2: ]
sliceTwo = myList[ :2]
sliceThree = myList[-2: ]

print(sliceOne) # outputs: [3, 4, 5]
print(sliceTwo) # outputs: [1, 2]
print(sliceThree) # outputs: [4, 5]

###

# You can delete slices using the del instruction:

myList = [1, 2, 3, 4, 5]
del myList[0:2]
print(myList) # outputs: [3, 4, 5]

del myList[:]
print(myList) # deletes the list content, outputs: []

###

# You can test if some items exist in a list or not using the keywords in and not in, e.g.:

myList = ["A", "B", 1, 2]

print("A" in myList) # outputs: True
print("C" not in myList) # outputs: True
print(2 not in myList) # outputs: False

#

