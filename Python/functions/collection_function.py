
from functools import reduce

#Mapping a function over a range
#Algebra, think of it as a graph paper.

domain = [1, 2, 3, 4, 5]  # the domain is the list of intigers.

# example f(x) = x * 2
# will be the same length the argument provides
# The range is always the same length as the domain.
our_range = map(lambda num: num * 2, domain)
print(list(our_range))  

#filter needs a callable and interable
evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))

# adding the reducer and accumulator
# need to call the reducer
# accumulates the numbers in the domain
the_sum = reduce(lambda acc, num: acc + num, domain, 0)