import time
import os
import colorama
import copy


def clear(s): # ez kész
    time.sleep(s)
    os.system("cls||clear")


def main_menu():
    #board méret
    #turn limit
    #játékos mód
    pass


def turn_limit():
    #50nél nagyobb, vége a játéknak
    pass


def game_mode():
    #player vs.player or player vs. ai or ai vs. ai
    pass


def get_move():
    pass


def ai_move():
    #random or intelligence
    pass


def win_condition():
    pass


def hit_or_miss():
    pass
    # hit or miss 
    # https://www.youtube.com/watch?v=_fSCkD-gWk0
    # https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
    # https://www.programiz.com/python-programming/shallow-deep-copy

def placement_phase():
    #direct (or random)
    pass


def shooting_phase():
    pass


def board_size():
    clear(0)
    board_size = input("Board size: (X * X size)\n\n- ")
    while True:
        if board_size.isnumeric():
            print("\nLoading board size...")
            return int(board_size)
        else:
            print("\nLoading default board size...")
            return 3


def init_board(board_size=3):
    board = []
    for row in range(board_size):
        row = []
        for col in range(board_size):
            row.append("O")
        board.append(row)
    return board


def main():
    size = board_size()
    board1, board2 = init_board(size) # LÁTOM, megvan
    board2 = copy.deepcopy(board1)
    board2[0][0] = "j"
    print(board1)
    print(board2)

if __name__ == "__main__":
    main()
