import helpers

# The import module was the fucntion created in the helpers file.
# It's recommended to run the main.py file with only the mod
# This would show if there are errors.  
# If there are no results, then its working properly.

name = "Joseph Porr"
print(f"Lowercase Letters: {helpers.extract_lower(name)}")
print(f"Uppercase Letters: {helpers.extract_upper(name)}")

###

# Note:  Helpers can be shorten to just an "h".
import helpers as h

name = "Joseph Porr"
print(f"Lowercase Letters: {h.extract_lower(name)}")
print(f"Uppercase Letters: {h.extract_upper(name)}")

###

# Can call functions directly form the module.

from helpers import extract_upper, extract_lower

name = "Joseph Porr"
print(f"Lowercase Letters: {extract_lower(name)}")
print(f"Uppercase Letters: {extract_upper(name)}")

#
