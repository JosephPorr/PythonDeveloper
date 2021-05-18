# The assignment: list2 = list1 copies the name of the array, not its contents. 
# In effect, the two names (list1 and list2) identify the same location in the computer memory. 
# Modifying one of them affects the other, and vice versa.

list1 = [1]  # creates a one-element list named list1;
list2 = list1 # assigns it to a new list named list2;
list1[0] = 2 # changes the only element of list1;
print(list2) # prints out list2.