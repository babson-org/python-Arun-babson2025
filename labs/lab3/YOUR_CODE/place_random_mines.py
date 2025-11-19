import random
import globals

def place_random_mines(board, seed=None):
    
    #Randomly sets exactly globals.MINES mines in the board's *base* layer.
    #Board cells are tuples: (display_value, base_value).
    
    if seed is not None:
        random.seed(seed)

    total_rows = globals.ROWS
    total_cols = globals.COLS
    mines_to_place = globals.MINES
    total_cells = total_rows * total_cols

    if not (1 <= mines_to_place < total_cells):
        raise ValueError(f"MINES must be in [1, {total_cells - 1}]")

    # choose unique cell indices without replacement
    chosen_positions = random.sample(range(total_cells), mines_to_place)

    for position in chosen_positions:
        row_index = position // total_cols
        col_index = position % total_cols

        # keep current display value, replace base with a mine
        current_display, _current_base = board[row_index][col_index]
        board[row_index][col_index] = (current_display, '💣')