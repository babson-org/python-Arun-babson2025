import globals

def get_validated_input(board):
    rows = globals.ROWS
    cols = globals.COLS

    while True:
            try:
                row = int(input("Enter a row number: "))
                col = int(input("Enter a column number: "))

                if not (0 <= row < rows and 0 <= col < cols):
                    print(f"Outside the board! Rows 0–{rows-1}, Cols 0–{cols-1}.")
                    continue

                display_value, _ = board[row][col]
                if display_value != ' ♦':
                    print("That cell is already revealed. Pick another.")
                    continue

                return row, col
            except ValueError:
                print("Please enter numbers only.")