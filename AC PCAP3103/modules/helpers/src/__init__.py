#  __init__ is a package and contents will run 1st.
# Basically, the modules can be packaged in init and be easily called from elsewhere

# can import functions from specic files

"""
Helpers is a package that provides easy to use helper functions
and variables.
"""

__all__ = ['extract_upper']

from .strings import *  # The * means import everything.