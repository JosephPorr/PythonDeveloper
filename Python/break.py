# break - example

# break - exits the loop immediately, and unconditionally ends the loop's operation; 
# the program begins to execute the nearest instruction after the loop's body;

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


