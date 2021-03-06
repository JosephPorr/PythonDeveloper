# 1) Set the users variable to be an empty list. From the terminal, use $python using_lists.py to see the debug from asserts.
users = []  #  first need to create a users list, [] are for lists

assert users == [], f"Expected `users` to be [] but got: {repr(users)}"
# Assert is used to debug and test if a condition in your code is true.

# 2) Add 'Joe', 'bob', and 'alice' to the users list in that order without reassigning the variable.
users.append('Joe')
users.append('bob')
users.append('alice')

assert users == ['Joe', 'bob', 'alice'], f"Expected `users` to be ['Joe', 'bob', 'alice'] but got: {repr(users)}"

# 3) Remove 'bob' from the `users` list without reassigning the variable.
del users[1]

assert users == ['Joe', 'alice'], f"Expected `users` to be ['Joe', 'alice'] but got: {repr(users)}"

# 4) Reverse the users list and assign the result to `rev_users`
rev_users = list(reversed(users))

assert rev_users == ['alice', 'Joe'], f"Expected `rev_users` to be ['alice', 'Joe'] but got: {repr(rev_users)}"

# 5) Add the user 'melody' to users where 'bob' used to be.
users.insert(1, 'melody')

assert users == ['Joe', 'melody', 'alice'], f"Expected `users` to be ['Joe', 'melody', 'alice'] but got: {repr(users)}"

# 6) Add the users 'andy', 'wanda', and 'jim' to the users list using a single command
users += ['andy', 'wanda', 'jim']

assert users == ['Joe', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected `users` to be ['Joe', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"

# 7) Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`
center_users = users[2:4]

assert center_users == ['alice', 'andy'], f"Expected `users` to be ['alice', 'andy'] but got: {repr(center_users)}"