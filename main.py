from Graphics.Board import *
from time import sleep


board = Board(500, 500, 10, 10)

while True:
    sleep(100)
    board.update_board()