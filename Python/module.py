# Modules are addon fuctions. imported like books in a library.
# These entities can be functions, variables, constants, classes, and objects
# https://edube.org/learn/pe-2/using-modules-9
# Inside a certain namespace, each name must remain unique. 
# If the module of a specified name exists and is accessible 
# (a module is in fact a Python source file), Python imports its contents, 
# i.e., all the names defined in the module become known, but they don't enter your code's namespace.
# first, the name of the module (e.g., math)
# then, a dot (i.e., .)
# lastely, the name of the entity (e.g., pi)

import math
print(math.sin(math.pi/2))   

# The math. keeps the pi on the math namespace unique to math.  
# it won't conflict with exisiting namespaces.