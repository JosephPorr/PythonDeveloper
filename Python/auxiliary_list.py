#  reverse the order of the elements: the first and the fifth as well as the second and fourth elements will be swapped. 
# The third one will remain untouched.

myList = [10, 1, 8, 3, 5]  # the middle element is 8 and will remain the same in reversed order.  

myList[0], myList[4] = myList[4], myList[0]  # This swaps the first element 10 with the last element 5; remember the element positions in the list are counted as 0,1,2,3,4.
myList[1], myList[3] = myList[3], myList[1]  # This swaps the second element 1 with the element 3

print(myList)

###

# A diferent way divides the list in half.

myList = [10, 1, 8, 3, 5]
length = len(myList)  # identifies the length of the list

for i in range(length // 2):  #  The integers in the range is devided in half.  So, the middle element remains the same.
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)

#