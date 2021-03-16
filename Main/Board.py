import random
from Main.constants import *

board = []

for i in range(HORIZONTAL_TILES_NUMBER):
    board.append([random.randint(0, 3)])
    for j in range(VERTICAL_TILES_NUMBER):
        board[i].append(random.randint(0, 3))

print(board)