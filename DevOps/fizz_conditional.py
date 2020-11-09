#!C:\\Users\\Joe\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe

value = int(input("Enter an integer value: "))

if value % 5 == 0 and value % 3 == 0:  # % is not percent its divisible by 5 or 3
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 ==0:
    print("Buzz")
else:
    print(value)

'''
$ ./fizz_conditional.py
Enter an integer value: 15
FizzBuzz
'''
