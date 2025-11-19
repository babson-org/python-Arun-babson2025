import globals
from is_mine_at import is_mine_at
from get_adjacent_cells import get_adjacent_cells

def reveal_cell(board, row, col):
    """
   
    If mine → game over
    If number → reveal that one
    If blank → reveal this cell and its direct neighbors only
    Returns 'lost' or 'ok'
    """
    if is_mine_at(board, row, col):
        board[row][col] = ('💣', '💣')
        return 'lost'

    base_value = board[row][col][1]

    # reveal the current cell
    board[row][col] = (base_value, base_value)

    # if it's a blank ('   '), reveal neighbors only once
    if base_value == '   ':
        for neighbor_row, neighbor_col in get_adjacent_cells(row, col):
            neighbor_base = board[neighbor_row][neighbor_col][1]
            if neighbor_base != '💣' and board[neighbor_row][neighbor_col][0] == ' ♦':
                board[neighbor_row][neighbor_col] = (neighbor_base, neighbor_base)

    return 'ok'
