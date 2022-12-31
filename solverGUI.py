import pygame
from DepthFirst.depthFirst import solveDFS
from utils.debug import printBoard

# ----- Pygame Functions -----
pygame.init()

# ----- Pygame Window -----
WINDOW_WIDTH = 540
WINDOW_HEIGHT = 590
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

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
    for i in range(1, 9):
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
                window.blit(text, (j * 60 + 20, i * 60 + 20))

def drawSolve():
    pygame.draw.rect(window, BLACK, (SOLVE_X, SOLVE_Y, SOLVE_WIDTH, SOLVE_HEIGHT))
    text = font.render("Solve", True, WHITE)
    window.blit(text, (SOLVE_X + 20, SOLVE_Y + 10))

def drawReset():
    pygame.draw.rect(window, BLACK, (RESET_X, RESET_Y, RESET_WIDTH, RESET_HEIGHT))
    text = font.render("Reset", True, WHITE)
    window.blit(text, (RESET_X + 20, RESET_Y + 10))

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
            # If the user closes the window, set the running flag to False
            if event.type == pygame.QUIT:
                running = False
            # If the user clicks the mouse, get the cell coordinates and update the board
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                row = mouse_y // 60
                col = mouse_x // 60
                if row < 9 and col < 9:
                    board[row][col] = (board[row][col] + 1) % 10
                elif SOLVE_X <= mouse_x <= SOLVE_X + SOLVE_WIDTH and SOLVE_Y <= mouse_y <= SOLVE_Y + SOLVE_HEIGHT:
                    solveDFS(board)
                elif RESET_X <= mouse_x <= RESET_X + RESET_WIDTH and RESET_Y <= mouse_y <= RESET_Y + RESET_HEIGHT:
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
        drawSolve()
        drawReset()
        # Update the display
        pygame.display.update()
    # Quit pygame
    pygame.quit()


if __name__ == "__main__":
    main()
