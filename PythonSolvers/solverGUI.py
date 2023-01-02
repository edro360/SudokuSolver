import pygame
from DepthFirst.depthFirst import solveDFS
from utils.debug import printBoard

# ----- Pygame Functions -----
pygame.init()

# ----- Pygame Window -----
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# ----- Pygame Solve Button -----
SOLVE_WIDTH = 100
SOLVE_HEIGHT = 50
SOLVE_X = 420
SOLVE_Y = 545

# ----- Pygame Reset Button -----
RESET_WIDTH = 100
RESET_HEIGHT = 50
RESET_X = 300
RESET_Y = 545

# ----- Pygame Colors and Font -----
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
font = pygame.font.Font(None, 36)

def drawGrid():
    # Draw the horizontal lines
    for i in range(1, 10):
        pygame.draw.line(window, GRAY, (0, i * 60), (540, i * 60), 2)
    # Draw the vertical lines
    for i in range(1, 9):
        pygame.draw.line(window, GRAY, (i * 60, 0), (i * 60, 540), 2)

def drawNums(board):
    for i in range(9):
        for j in range(9):
            # If the cell is not empty, draw the number
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                window.blit(text, (j * 60 + 25, i * 60 + 20))

def drawBigButton(buttonX, buttonY, buttonWidth, buttonHeight, msg):
    pygame.draw.rect(window, BLACK, (buttonX, buttonY, buttonWidth, buttonHeight))
    text = font.render(msg, True, WHITE)
    window.blit(text, (buttonX + 20, buttonY + 10))

def isWithin(mouseX, mouseY, buttonX, buttonY, buttonHeight, buttonWidth):
    if (buttonX <= mouseX <= buttonX+buttonWidth and buttonY <= mouseY <= buttonY+buttonHeight):
        return True
    return False

def main():
    # Initialize the board
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
    # Set the running flag to True
    running = True
    while running:
        # Fill the window with white color
        window.fill(WHITE)
        # Handle events
        for event in pygame.event.get():
            match event.type:
                # If the user closes the window, set the running flag to False
                case pygame.QUIT:
                    running = False
                # If the user clicks the mouse, get the cell coordinates and update the board
                case pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    row = mouse_y // 60
                    col = mouse_x // 60
                    if row < 9 and col < 9:
                        board[row][col] = (board[row][col] + 1) % 10
                    elif isWithin(mouse_x, mouse_y, SOLVE_X, SOLVE_Y, SOLVE_HEIGHT, SOLVE_WIDTH):
                        pygame.display.set_caption("Sudoku Solver using DFS")
                        solveDFS(board)
                    elif isWithin(mouse_x, mouse_y, RESET_X, RESET_Y, RESET_HEIGHT, RESET_WIDTH):
                        pygame.display.set_caption("Sudoku Solver")
                        board = [
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                ]
        # Draw the grid and the numbers
        drawGrid()
        drawNums(board)
        drawBigButton(SOLVE_X, SOLVE_Y, SOLVE_WIDTH, SOLVE_HEIGHT, "Solve")
        drawBigButton(RESET_X, RESET_Y, RESET_WIDTH, RESET_HEIGHT, "Reset")
        # Update the display
        pygame.display.update()
    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
