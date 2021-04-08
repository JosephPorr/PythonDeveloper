# A for loop and a break statement. This should iterate over characters in an email address, 
# exit the loop when it reaches the @ symbol, 
# and print the part before @ on one line. 

for ch in "email@email.com":  # ch = characters
    if ch == "@":   # need to define the ch
        break
    print(ch, end="")
    

# When a comma is used at the end of a PRINT statement, 
# the data in the next PRINT statement is continued on the same line 
# beginning in the next print zone. When " " (quote, blank, quote) is used 
# as a print field the computer will skip to the next print field. 
# You are actually telling the computer to print a blank field.