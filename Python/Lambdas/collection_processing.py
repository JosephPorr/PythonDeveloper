# 1) Sort rhe 'porple' list of dictionaries alphabetically based on the
# 'name' key from each dictionary using the 'sorted' function and store
# the new list as a 'sorted_by_name'

people = [
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Fred Ward", "age": 77},
    {"name": "Finn Carter", "age": 59},
    {"name": "Ariana Richards", "age": 46},
    {"name": "Victor Wong", "age": 74},
]

# use a key parameter and a labmbs d is for a dictionary 
# access the name key from the dictionary
# and make is lower case before comparison.
sorted_by_name = sorted(people, key=lambda d: d['name'].lower())  

assert sorted_by_name == [
    {"name": "Ariana Richards", "age": 46},
    {"name": "Finn Carter", "age": 59},
    {"name": "Fred Ward", "age": 77},
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Victor Wong", "age": 74},
]

