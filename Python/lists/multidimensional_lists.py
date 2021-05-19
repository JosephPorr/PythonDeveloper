# # List within lists have rows and columns like a chessboard or xcel spreadsheet.
# The location of each field is identified by letter-digit pairs. 
# Thus, we know that the bottom right corner of the board (the one with the white rook) is A1, while the opposite corner is H8.
# Access to the selected field of the board requires two indices - 
# the first selects the row; the second - the field number inside the row, 
# which is de facto a column number.

# https://edube.org/learn/programming-essentials-in-python/lists-in-advanced-applications-arrays-1


EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)