from get_adjacent_cells import get_adjacent_cells
from is_mine_at import is_mine_at

def count_adjacent_mines(board, row, col):
    
   # Counts the number of mines surrounding (row, col).
    

    total_mines = 0

    for neighbor_row, neighbor_col in get_adjacent_cells(row, col):
        if is_mine_at(board, neighbor_row, neighbor_col):
            total_mines += 1

    return total_mines