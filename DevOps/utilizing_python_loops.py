#!C:\\Users\\Joe\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe

# Python implementation here

upper_number = int(input("How many values should we process: "))

for number in range(1, upper_number +1):
    if number % 3 == 0 and number % 5 == 0:
        print("FixxBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)