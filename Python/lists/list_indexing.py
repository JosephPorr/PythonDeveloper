# Python has adopted a convention stating that the elements in a list are always numbered starting from zero. 
# This means that the item stored at the beginning of the list will have the number zero. 
# Since there are five elements in our list, the last of them is assigned the number four. 
# Don't forget this.

numbers = [10, 5, 7, 2, 1]
print("Orignal list content:", numbers) # printing original list content

numbers[0] = 111
print("\nPrevious list of content: ", numbers) # print previous list content

numbers[1] = numbers[4] # compying value of the fifth element to the second
print("New list content: ", numbers) # print current list content