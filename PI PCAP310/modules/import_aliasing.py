# Aliasing causes the module to be identified under a different name than the original. 
# This may shorten the qualified names, too.

import math as m

print(m.sin(m.pi/2))

from math import pi as PI, sin as sine

print(sine(PI/2))