import pygame
from Checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from Checkers.game import Game
from Minimax.algorithm import minimax
import time

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, float('-inf'), float('inf'), WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            game.update()
            print(str(game.winner()))
            time.sleep(5)
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()