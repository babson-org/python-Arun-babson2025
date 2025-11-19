
import globals

def print_board(board: list, level: int):

    line_hash = '|-----'

    # Print column headers
    print('      ', end='')
    for idx in range(globals.COLS):
        print(f'   {idx}  ', end='')
    print(f'\n      {line_hash * globals.COLS}|')

    # Print each row
    for row in range(globals.ROWS):
        print(f'  {row}   ', end='')
        for col in range(globals.COLS):
            symbol = board[row][col][level]
            if symbol == '💣':
                print(f'| {symbol:3}', end='')
            else:
                print(f'| {symbol:3} ', end='')
        print('|')

        print(f'      {line_hash * globals.COLS}|')
