# The order matters, if the first condition that is true, and ignores all thereafter.

name = input("What is your name? ")
if len(name) >= 6:
   print("Your name is long.")
elif len(name) == 5:
   print("Your name is 5 characters.")
elif len(name) >= 4:
   print("Your name is 4 or more characters.")
else:
   print("Your name is short.")
