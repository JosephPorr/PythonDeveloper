#  You can start a list's life by making it empty 
# (this is done with an empty pair of square brackets) 
# and then adding new elements to it as needed.

myList = [] # creating an empty list

for i in range(5):   # "i" is shorthand variable for "Integer" in the for loop"
    myList.append(i + 1)  #  It'll be a sequence of consecutive integer numbers from 1 (you then add one to all the appended values) to 5.

print(myList)

###

myList = [] # creating an empty list

for i in range(5):
    myList.insert(0, i + 1)  # the "insert" reverses the range sequence.

print(myList)

#