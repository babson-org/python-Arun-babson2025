import globals
from initialize_board import initialize_board      
from print_board import print_board
from get_validated_input import get_validated_input
from update_board import reveal_cell
from game_won import game_won


def play_minesweeper():
    print("=== Minesweeper ===")

    # Ask user for board setup
    globals.ROWS = int(input("How many rows? "))
    globals.COLS = int(input("How many columns? "))
    globals.MINES = int(input("How many mines? "))

    # Create the board
    board = initialize_board()

    # Game loop
    while True:
        print_board(board, level=0)  # what the player sees

        # Get player move
        row, col = get_validated_input(board)

        # Reveal that cell
        status = reveal_cell(board, row, col)

        # Check lose condition
        if status == 'lost':
            print("You hit a mine. Game over.")
            # Reveal all mines for the final board
            for r in range(globals.ROWS):
                for c in range(globals.COLS):
                    display_value, base_value = board[r][c]
                    if base_value == '💣':
                        board[r][c] = ('💣', '💣')
            print_board(board, level=0)
            break

        # Check win condition
        if game_won(board):
            print_board(board, level=0)
            print("You Win! All safe cells revealed.")
            break



play_minesweeper()

