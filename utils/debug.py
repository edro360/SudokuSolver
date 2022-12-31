def printBoard(board):
    """
    Creates a board in the command line of the current board.
    """
    for i in range(9):
        for j in range(9):
            print("{:2}".format(board[i][j]), end=" ")
            if ((j + 1) % 3 == 0):
                print("", end=" ")
        print()
        if ((i + 1) % 3 == 0):
            print("" * 32)
            