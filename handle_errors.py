import sys # Import a system package to clean-up.

# The error is a FileExistsError and it's being raised 
# because we're opening the file for creation (using the x mode), 
# but it already exists.
# To handle this, we need to place our code that could raise an
#  error within a try statement and then except an error if it
#  happens and do something else.
try:
    my_file = open('recipes.txt', 'x')
    my_file.write('Meatballs\n')
    my_file.close()
except FileExistsError as err:
    print(f"The {file_name} file already exists")
except:
    print(f"Unable to write to the {file_name} file")
# We could make this more specific and only except a 
# very specific error, and even have multiple separate 
# except blocks catching different kinds of errors.
else:
    print(f"Wrote to {file_name}")
# If a finally clause is present, the finally clause will 
# execute as the last task before the try statement completes. 
# The finally clause runs whether or not the try statement 
# produces an exception.
finally:
    print("Execution complete")