import pygame
import sys
import random

pygame.init()

WINDOW_WIDTH = 300  
WINDOW_HEIGHT = 600  
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tetris')

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

SHAPES = {
    'S': [[0, 1, 1],
          [1, 1, 0],
          [0, 0, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1],
          [0, 0, 0]],
    'I': [[0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
    'O': [[1, 1],
          [1, 1]],
    'J': [[1, 0, 0],
          [1, 1, 1],
          [0, 0, 0]],
    'L': [[0, 0, 1],
          [1, 1, 1],
          [0, 0, 0]],
    'T': [[0, 1, 0],
          [1, 1, 1],
          [0, 0, 0]]
}

SHAPE_COLORS = {
    'S': GREEN,
    'Z': RED,
    'I': CYAN,
    'O': YELLOW,
    'J': BLUE,
    'L': ORANGE,
    'T': PURPLE
}

GRID_SIZE = 30  
GRID_WIDTH = 10  
GRID_HEIGHT = 20  
GAP = 1  

class Tetromino:
    def __init__(self, shape):
        self.shape = SHAPES[shape]
        self.color = SHAPE_COLORS[shape]
        self.rotation = 0
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        self.rotation = (self.rotation + 1) % 4

    def get_cells(self):
        cells = []
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    cells.append((self.x + j, self.y + i))
        return cells

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for (x, y), color in locked_positions.items():
        if y < GRID_HEIGHT:
            grid[y][x] = color
    return grid

def draw_grid(surface, grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(surface, grid[y][x],
                             (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - GAP, GRID_SIZE - GAP))

    # Draw grid lines
    for x in range(GRID_WIDTH):
        pygame.draw.line(surface, GRAY, (x * GRID_SIZE, 0), (x * GRID_SIZE, WINDOW_HEIGHT))
    for y in range(GRID_HEIGHT):
        pygame.draw.line(surface, GRAY, (0, y * GRID_SIZE), (WINDOW_WIDTH, y * GRID_SIZE))

def valid_space(tetromino, grid):
    accepted_positions = [[(x, y) for x in range(GRID_WIDTH) if grid[y][x] == BLACK] for y in range(GRID_HEIGHT)]
    accepted_positions = [x for sub in accepted_positions for x in sub]

    formatted = tetromino.get_cells()

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def get_shape():
    return Tetromino(random.choice(list(SHAPES.keys())))

def lock_position(tetromino, grid, locked_positions):
    for pos in tetromino.get_cells():
        x, y = pos
        if y >= 0:
            locked_positions[(x, y)] = tetromino.color
    return locked_positions

def clear_rows(grid, locked_positions, score):
    increment = 0
    for y in range(GRID_HEIGHT -1, -1, -1):
        row = grid[y]
        if BLACK not in row:
            increment +=1
            for x in range(GRID_WIDTH):
                try:
                    del locked_positions[(x, y)]
                except:
                    continue
    if increment > 0:
        for key in sorted(list(locked_positions), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < GRID_HEIGHT:
                if y < GRID_HEIGHT - increment:
                    newKey = (x, y + increment)
                    locked_positions[newKey] = locked_positions.pop(key)
        score += increment * 10
    return score, locked_positions

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, True, color)

    surface.blit(label, (WINDOW_WIDTH/2 - (label.get_width()/2),
                         WINDOW_HEIGHT/2 - label.get_height()/2))

def draw_score(surface, score):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render(f"Score: {score}", True, WHITE)

    surface.blit(label, (WINDOW_WIDTH - 120, 10))

def draw_window(surface, grid, score=0):
    surface.fill(BLACK)

    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', True, WHITE)
    surface.blit(label, (WINDOW_WIDTH/2 - (label.get_width()/2), 30))

    draw_grid(surface, grid)
    draw_score(surface, score)

def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y +=1
            if not (valid_space(current_piece, grid)) and current_piece.y >0:
                current_piece.y -=1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -=1
                    if not valid_space(current_piece, grid):
                        current_piece.x +=1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x +=1
                    if not valid_space(current_piece, grid):
                        current_piece.x -=1
                elif event.key == pygame.K_DOWN:
                    current_piece.y +=1
                    if not valid_space(current_piece, grid):
                        current_piece.y -=1
                elif event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not valid_space(current_piece, grid):
                        current_piece.rotate()
                        current_piece.rotate()
                        current_piece.rotate()

        shape_pos = current_piece.get_cells()

        for pos in shape_pos:
            x, y = pos
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                x, y = pos
                if y > -1:
                    locked_positions[(x, y)] = current_piece.color
            current_piece = get_shape()
            change_piece = False
            score, locked_positions = clear_rows(grid, locked_positions, score)

        draw_window(window, grid, score)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_text_middle(window, "YOU LOST", 40, WHITE)
            pygame.display.update()
            pygame.time.delay(2000)
            run = False

    pygame.display.quit()

def main_menu():
    run = True
    while run:
        window.fill(BLACK)
        draw_text_middle(window, 'Press Any Key To Play', 30, WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()

if __name__ == "__main__":
    main_menu()