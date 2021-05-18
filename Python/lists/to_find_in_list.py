# finds the location of a given element inside a list:

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 5 # The target value 5 is stored in the toFind variable
found = False # boolean to find truthiness

for i in range(len(myList)):
    found = myList[i] == toFind  # the current status of the search is stored in the found variable (True/False)
    if found:
        break # when found becomes True, the for loop is exited

if found:
    print("Element found at index", i)
else:
    print("absent")

###

# Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.
# The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.
# The question is: how many numbers have you hit?
# The program will give you the answer:

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

# the drawn list stores all the drawn numbers;
# the bets list stores your bets;
# the hits variable counts your hits.

# The program output is: 4.

#