# Input: 'col1up col2up col3up col4up col1down col2down col3down col4down row1left row2left row3left row4left row1right row2right row3right row4right
# Output: '1 3 2 4 4 2 3 1 3 4 1 2 2 1 4 3'

# solver("col1up col2up col3up col4up col1down col2down col3down col4down row1left row2left row3left row4left row1right row2right row3right row4right")
# Import relevant libraries
import time
import datetime
import numpy as np
from itertools import product
from random import randint, shuffle
from itertools import permutations
SIZE = 4
solCount, endSolve = 0, False
class SkyscraperSolver:

    def visible(grid, x, direction):
        counter, highest = 0, 0
        match (direction):
            case 'n':
                line = grid[:, x]
            case  's':
                line = grid[:, x][::-1]
            case 'w':
                line = grid[x, :]
            case 'e':
                line = grid[x, :][::-1]
            case _:
                print('Insert a correct direction')
                return 0
        for n in line:
            if n > highest:
                highest = n
                counter += 1
        return counter


    def possible(board, y, x, n):
        grid = board[1:-1, 1:-1]
        gridTemp = np.copy(grid)
        # Check if 'n' is already in row 'y' or in column 'x'
        for i in range(SIZE):
            if grid[y][i] == n or grid[i][x] == n:
                return False
        # Check the requirements on the column
        col = False
        for line in list((permutations(np.delete(range(1, SIZE+1), n-1)))):
            idx = 0
            for i in range(SIZE):
                if grid[i, x] == 0:
                    if i == y:
                        gridTemp[y, x] = n
                    else:
                        gridTemp[i, x] = line[idx]
                        idx += 1
            if board[0, x + 1] in [0, visible(gridTemp, x, 'n')] and board[-1, x + 1] in [0, visible(gridTemp, x, 's')]:
                col = True
                break
        # Check the requirements on the row
        find_row = False
        for line in list((permutations(np.delete(range(1, SIZE+1), n-1)))):
            idx = 0
            for i in range(SIZE):
                if grid[y, i] == 0:
                    if i == x:
                        gridTemp[y, x] = n
                    else:
                        gridTemp[y, i] = line[idx]
                        idx += 1
            if board[y + 1, 0] in [0, visible(gridTemp, y, 'w')] and board[y + 1, -1] in [0, visible(gridTemp, y, 'e')]:
                find_row = True
                break
        return find_row and col


    def solver(board):
        global solCount
        global endSolve
        for y, x in product(range(SIZE), range(SIZE)):
            if board[y+1][x+1] == 0:
                for n in range(1, SIZE+1):
                    if possible(board, y, x, n):
                        board[y+1][x+1] = n
                        solver(board)
                        if not (endSolve):
                            board[y+1][x+1] = 0
                return
        solCount += 1
        if solCount == 2:
            endSolve = True
        print(board)


# Usage
startTime = time.time()
board = np.array([[0, 2, 2, 3, 1, 0],
                  [3, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 3],
                  [2, 0, 0, 0, 0, 2],
                  [2, 0, 0, 0, 0, 2],
                  [0, 3, 2, 1, 2, 0]])
print('Solution(s):\n')
solver(board)
print(
    f'\nFound {solCount} solution(s) [{round((time.time()-startTime)*1000, 3)}]')

# Calculate time to solve
# timer = 0
# for i in range(1000):
#     startTime = time.time()
#     board = np.array([[0, 2, 2, 3, 1, 0],
#                       [3, 0, 0, 0, 0, 1],
#                       [1, 0, 0, 0, 0, 3],
#                       [2, 0, 0, 0, 0, 2],
#                       [2, 0, 0, 0, 0, 2],
#                       [0, 3, 2, 1, 2, 0]])
#     solve(board)
#     print(board)
#     timer += round((time.time()-startTime)*1000, 3)
# print('Avg: ',timer/1000)