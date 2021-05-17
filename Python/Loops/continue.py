# continue - example

# continue - behaves as if the program has suddenly reached the end of the body; 
# the next turn is started and the condition expression is tested immediately.e

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

