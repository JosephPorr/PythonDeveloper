#  A hotel building is a good example of 3 dimensional lists.

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# The first index (0 through 2) selects one of the buildings; 
# the second (0 through 14) selects the floor, 
# the third (0 through 19) selects the room number.

###

# Can book a room for two newlyweds: in the second building, on the tenth floor, room 14:
rooms[1][9][13] = True

# and release the second room on the fifth floor located in the first building:
rooms[0][4][1] = False

# Check if there are any vacancies on the 15th floor of the third building:

vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1

# The vacancy variable contains 0 if all the rooms are occupied, or the number of available rooms otherwise.

#