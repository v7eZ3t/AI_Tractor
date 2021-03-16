import random
from Main.constants import *

board = []

for i in range(int(HORIZONTAL_TILES_NUMBER)):
    board.append([random.randint(0, 3)])
    for j in range(int(VERTICAL_TILES_NUMBER)):
        board[i].append(random.randint(0, 3))

# 0 - pole na medal
# 1 - do zasiania
# 2 - do podlania
# 3 - do ścięcia

print(board)