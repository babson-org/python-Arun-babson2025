
import globals
from place_random_mines import place_random_mines
from count_adjacent_mines import count_adjacent_mines
from is_mine_at import is_mine_at

def initialize_board():
    rows = globals.ROWS
    cols = globals.COLS

    # start with hidden display and empty base
    board = [[(' ♦', '   ') for _ in range(cols)] for _ in range(rows)]

    # place mines 
    place_random_mines(board)

    # fill numbers / blanks for non-mine cells
    for row in range(rows):
        for col in range(cols):
            if is_mine_at(board, row, col):
                continue
            count = count_adjacent_mines(board, row, col)
            if count == 0:
                # keep base as blank
                board[row][col] = (board[row][col][0], '   ')
            else:
                board[row][col] = (board[row][col][0], count)

    return board
