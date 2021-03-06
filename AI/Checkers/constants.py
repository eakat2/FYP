import json
import pickle
import pygame

WIDTH, HEIGHT = 320, 320
HOR_MARG, VERT_MARG = 352, 140
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (244, 244, 240)
BLACK = (115, 62, 25)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
GOLD = (255, 223, 0)
LIGHT = (221, 211, 204)
DARK = (147, 102, 49)
BORDER = (48, 33, 23)


# Difficulty Levels
Novice = 1
Beginner = 2
Intermediate = 3
Hard = 4

# Settings
FORCE_TAKE = False
KING_MOVE = False
KING_TAKE = False
FIRST = LIGHT
DIFFICULTY = Intermediate
COMPUTER = False

# def main():
#     #int_load()
#     load_const()

# # Used to save constants to file
# def int_save():
#     data = str(FORCE_TAKE) + ";" + str(KING_MOVE) + ";" + str(KING_TAKE) + ";" + str(FIRST) + ";" + str(DIFFICULTY)
#     print("data")
#     with open(r'Gameplay Engine\UI\constants.json', 'w') as file:
#         json.dump(data, file)

# # Used to load constants from file
# def load_const():
#     global FORCE_TAKE, KING_MOVE, KING_TAKE, FIRST, DIFFICULTY

#     with open(r'Gameplay Engine\UI\constants.json', 'r') as file:
#         data = json.load(file)

#     data = data.split(';')  
#     FORCE_TAKE = bool(data[0])
#     KING_MOVE = bool(data[1])
#     KING_TAKE = bool(data[2])
#     FIRST = tuple(map(int, data[3][1:-1].split(', ')))
#     DIFFICULTY = int(data[4])

# main()