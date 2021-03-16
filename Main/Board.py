import random
from Main.constants import *

board = []


def generate():
    for i in range(int(HORIZONTAL_TILES_NUMBER)):
        board.append([random.randint(0, 3)])
        for j in range(int(VERTICAL_TILES_NUMBER)):
            board[i].append(random.randint(0, 3))
    return board
