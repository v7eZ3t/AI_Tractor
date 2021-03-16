import random

board = []

for i in range(5):
    board.append([random.randint(0, 3)])
    for j in range(5):
        board[i].append(random.randint(0, 3))

print(board)