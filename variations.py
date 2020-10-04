#!C:\\Users\\Joe\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe
#To keep from being completely tied to the path of our python3 binary.

# This script will take a user-provided message and perform various actions on it before printing

# Makes this exicutatable through the terminal.
#Joe@Joe-PC MINGW64 ~/Documents/GitHub/PythonDeveloper (master)
#$ chmod u+x ~/Documents/GitHub/PythonDeveloper/variations.py

message = input("Enter a message: ")

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

words = message.split()  # Will store words in new variable, words.
print("Words:", words)

sorted_words = sorted(words) # Sorting the stored words in words.
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])

"""
$ ./variations.py
Enter a message: This is Test Message!
Lowercase: this is test message!
Uppercase: THIS IS TEST MESSAGE!
Capitalized: This is test message!
Title Case: This Is Test Message!
Words: ['This', 'is', 'Test', 'Message!']
"""

