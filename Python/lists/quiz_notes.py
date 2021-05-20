i = 2
while i >= 0:
    print("*")
    i -= 2  
# Subtract AND. It subtracts right operand from the left operand
# and assign the result to left operand. c -= a is equivalent to c = c - 

###

for i in range(-1, 1):
    print("#")  # nothing changes, still two integers

###

z = 10
y = 0
x = z > y or z == y  # The value of z is greater than y

###

lst = [3, 1, -1]
lst[-1] = lst[-2]  
print(lst)

###

vals = [0, 1,2]
vals[0], vals[1] = vals[1], vals[2]

###

nums = []
vals = nums  
vals.append(1) # The append would add to both

###

nums = []
vals = nums[:] # omitting both start and end makes a copy of the whole list
vals.append(1)

###

l = [0 for i in range(1, 3)] # Zero means no additional elements will be added to te list

###

lst = [0, 1, 2, 3]
x = 1
for elem in lst:
    x *= elem  # x times the element 0, or  x = x * 0
print(x)

#

