#!C:\\Users\\Joe\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe

value = int(input("Enter an integer value: "))

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 ==0:
    print("Buzz")
else:
    print(value)
