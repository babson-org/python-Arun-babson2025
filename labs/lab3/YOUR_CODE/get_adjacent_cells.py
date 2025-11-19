import globals

def get_adjacent_cells(row, col):

    neighbors = []

    # 8 directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]
    # each cell in minesweeper has 8 neighbors, rowchange/col change are the amount we move from the 
    # current cell. we just use this to get neighbors location.
    for row_change, col_change in directions:
        new_row = row+row_change
        new_col = col+col_change

        if 0 <= new_row < globals.ROWS and 0 <= new_col < globals.COLS:
            neighbors.append((new_row, new_col))

    return neighbors