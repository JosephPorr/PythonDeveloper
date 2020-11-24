# for loop TEMP_VARIABLE in SEQUENCE

for num in range(1, 10, 2):
    if num % 3:
        print(num)

#>>> for num in range(1, 10, 2):
#...     if num % 3:
#...         print(num)
#...
#1
#5
#7

# A range is an immutable sequence type that defines a start, a stop, and a step value.
#  Start at 1, the length is ten, and the 2 means every other number for 1, 3, 5, 7, 9. 
# The modulus operation will return a non-zero value for some numbers, 
# and as a result, it will invoke the print line. Since 3 & 9 
# have no remainders when divided by % 3, the zeros aren't printed