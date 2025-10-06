
from calc_score import calc_score


def game_over(board: list[int]):
    """
        After every move (see play_game) we check to see if the game 
        is over.  The game is over if calc_score() returns 30 or -30
        or if ther are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """
    full = True
    for cell in board:
        if cell != 10 and cell != -10:
            full = False
            break

    # TODO: Use calc_score to check if someone has won
    result = calc_score(board)

    # TODO: Return True if game over, otherwise False
    if result == 30 or result == -30 or full:
        return True
    else:
        return False    
                
    
