def game_won(board):
    """
    Return True when all safe cells are revealed on the DISPLAY layer.
    A cell is unrevealed if its display_value is ' ♦'.
    """
    for row in range(len(board)):
        for col in range(len(board[0])):
            display_value, base_value = board[row][col]
            if base_value != '💣' and display_value == ' ♦':
                return False
    return True