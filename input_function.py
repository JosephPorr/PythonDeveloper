name = input("What is your name? ")  # its good practive to use a colon and/or space.
color = input("What is your favorite color? ")
age = input("How old are you? ")
# Works from the inside out, 
# and whatever value is returned from input is going to be
# the arguement passed into the int function
# NAME is AGE years old and loves the COLOR.

# print(name, end=" ")  # end will equal a space instead of a new line in REPL
# print("is " + str(age) + " years old", end=" ")
# print("and loves the color " + color + ".", end=" ")

print(name, 'is', age, 'years old and loves the color', color + '.', sep=" ") 

# A sep will print each argument separated by the sep character which is '' by default.