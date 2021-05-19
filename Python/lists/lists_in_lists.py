# List within lists have rows and columns like a chessboard or xcel spreadsheet.
# The location of each field is identified by letter-digit pairs. 
# Thus, we know that the bottom right corner of the board (the one with the white rook) is A1, while the opposite corner is H8.
# This line of code in defined, but an idea of have the
"""
row = []  # A row is counted downward, the left side of the chessboard

for i in range(8):  # this is a range of 8 rows.
    row.append(WHITE_PAWN)

row = [WHITE_PAWN for i in range(8)]

squares = [x ** 2 for x in range(10)]
# The snippet produces a ten-element list filled with squares of ten integer numbers 
# starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
# This multiple squares like a square root.  
# Looking a chessboard, A1 would be 1 square in the top left corner.
# H8  is the bottom left corner with a total of 64 squares, 8 rows and 8 columns is a total of 64 squares

odds = [x for x in squares if x % 2 != 0 ]
The snippet makes a list with only the odd elements of the squares list.

"""