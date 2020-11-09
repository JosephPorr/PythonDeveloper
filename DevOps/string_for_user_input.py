#!C:\\Users\\Joe\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe

message = input("Enter a message: ")  # prompt the user to enter a message.

print("First character:", message[0])  # Zero is the first index
print("Last character:", message[-1])  # -1 is last character of the index
print("Middle character:", message[int(len(message) / 2)])  # Divided by 2 (half) prints the middle int of the index.
# If its a even number of ints in a index, it will print +1 of the middle. example, abcd will print c.
print("Even index characters:", message[0::2])  # prints all the even numbers.
print("Odd index characters:", message[1::2])
print("Reversed message:", message[::-1]) # Use slicing to do the index in reverse.

#Joe@Joe-PC MINGW64 ~/Documents/GitHub/PythonDeveloper (master)
#$ ./string_for_user_input.py
#Enter a message: abcde
#First character: a
#Last character: e
#Middle character: c
#Even index characters: ace
#Odd index characters: bd
#Reversed message: edcba