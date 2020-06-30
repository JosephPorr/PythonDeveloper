import pdb #  This is a imported debugger used to tracing code.

def map(func, values):
    output_values = []
    index = 0
    while index < len(values):
        pdb.set_trace()  # settnig the trap for this trace starting from this point.
        output_values = func(values[index])
        index += 1  #  This is a broke and not intended to work to show how the debugger works
    return output_values

def add_one(val):
    return val + 1

print(map(add_one, list(range(10))))

# In the (PBD) prompt use h to show the commands, 
# and n to show the number line where the error is.  
# Can type list to see the entire source code for the error.

# REPL output below
#  $ python -i debugging.py
# >>> map(add_one, list(range(5)))
# > /home/cloud_user/learning_python/debugging.py(8)map()
# -> output_values = func(values[index])
# (Pdb)

# (Pdb) values
# [0, 1, 2, 3, 4]
# (Pdb) index
# 0
# (Pdb) output_values
# []
# (Pdb)

# q to exit the PBD prompt

# https://docs.python.org/3/library/pdb.html
# https://docs.python.org/3/library/pdb.html#pdb.set_trace
# https://docs.python.org/3/library/functions.html#breakpoint