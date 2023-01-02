
def isValid(board, row, col, num):
    for i in range(9):
        if (board[row][i] == num):
            return False
    for i in range(9):
        if (board[i][col] == num):
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if (board[startRow + i][startCol + j] == num):
                return False
    return True

def solveDFS(board):
    for row in range(9):
        for col in range(9):
            if (board[row][col] == 0):
                for k in range(1, 10):
                    if isValid(board, row, col, k):
                        board[row][col] = k
                        if solveDFS(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    board = [
        [5, 1, 8, 0, 0, 0, 0, 0, 0],
        [9, 7, 3, 0, 0, 1, 2, 0, 0],
        [6, 2, 4, 5, 0, 0, 0, 1, 0],
        [3, 8, 2, 0, 0, 9, 0, 0, 0],
        [4, 6, 9, 7, 0, 0, 0, 0, 3],
        [1, 5, 7, 0, 0, 0, 4, 0, 0],
        [2, 0, 1, 0, 0, 5, 3, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 7],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        ]
    solveDFS(board)

if __name__ == "__main__":
    main()
