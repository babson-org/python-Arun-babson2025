def calc_score(board: list[int]):
    """
        Determines if there's a winner on the board.
        Returns 30 if X wins, -30 if O wins, 0 otherwise.
         
        there are 8 ways to win: 3 rows, 3 columns, 2 diagnols
        if the cells in a row, column or diagnol add up to 30 return 30
        if they add upto -30 return -30
        else return 0
    """
     
    def line_sum(a, b, c):
        '''
            line_sum takes 3 numbers and if the sum is either 30
            or -30 returns that sum otherwise do not return
        '''         
         
        # TODO: Sum the values at board[a], board[b], board[c] 
        total = board[a] + board[b] + board[c]
        if total == 30:
            return 30
        elif total == -30:
            return -30
        # TODO: Return 30 if X wins, -30 if O wins otherwise do not return
        pass
     
    # TODO: For each of the 8 ways to win
    # TODO: Check the cells in each row, column, or diagonal using line_sum
    # TODO: Return 0 if line_sum() didn't return 30 or -30

    result = line_sum(0, 1, 2)
    if result is not None:
        return result
    
    result = line_sum(3, 4, 5)
    if result is not None:
        return result

    result = line_sum(6, 7, 8)
    if result is not None:
        return result

    result = line_sum(0, 3, 6)
    if result is not None:
        return result

    result = line_sum(1, 4, 7)
    if result is not None:
        return result

    result = line_sum(2, 5, 8)
    if result is not None:
        return result

    result = line_sum(0, 4, 8)
    if result is not None:
        return result

    result = line_sum(2, 4, 6)
    if result is not None:
        return result

    return 0


    pass

