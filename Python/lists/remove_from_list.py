#  Any of the list's elements may be removed at any time - this is done with an instruction named del (delete). 
# Note: it's an instruction, not a function.
# You have to point to the element to be removed - it'll vanish from the list, 
# and the list's length will be reduced by one.

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers) # printing original list content

numbers[0] = 111
print("\nPrevious list content:", numbers) # printing previous list content

numbers[1] = numbers[4] # copying value of the fifth element to the second
print("Previous list content:", numbers) # printing previous list content

###

del numbers[1] # Removing the seconf element from the list
print("New list's length:", len(numbers))  # prints the new list
print("\nNew list content:", numbers) # Printing current list content

###


