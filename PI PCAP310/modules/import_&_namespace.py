#  The imported symbols supersede their previous definitions within the namespace.
#  Also works when the import is beofre the namespace.
#  Will print both outcomes.

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))


