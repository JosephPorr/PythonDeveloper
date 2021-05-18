#  If you want Python to sort your list, you can do it like this:

myList = [8, 10, 6, 2, 4]
myList.sort()
print(myList)

###

myList = []  #  The list is empty and will require input from the user
swapped = True
num = int(input("How many elements do you want to sort: "))  # Requires an integer from the user

for i in range(num):  
    val = float(input("Enter a list element: "))  # The float turns the integer into a decimal
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):  # Counts the integer from the back in the lis
        if myList[i] > myList[i + 1]: # The If counts the integers from back to fron and if it is greater than the previous
            swapped = True # swap occured
            myList[i], myList[i + 1] = myList[i + 1], myList[i] #  This moves the interger with the great number to the rear.  The actual swap

print("\nSorted:")
print(myList)

#