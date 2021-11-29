import time
import os
import colorama
import copy
import getpass


def clear(s): # ez kész
    time.sleep(s)
    os.system("cls||clear")


def main_menu():
    #board mérethow to make something invisible in python
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
    # https://askubuntu.com/questions/317880/is-it-possible-to-make-the-text-in-terminal-invisible

    # https://www.youtube.com/watch?v=n1OB96dqFZM

def placement_phase():
    #direct (or random)
    pass


def shooting_phase():
    pass


def board_size():
    clear(0)
    board_size = getpass("Board size: (X * X size)\n\n- ")
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


def print_board(board):
    print()
    string = "  "
    for number in range(1, len(board)+1):
        string += str(number) + "  "
    list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    msg = ""
    for i, row in enumerate(board):
        element = row[0]
        element_str = f"{list[i]}" + '{:^{width}}'.format(element, width=3)
        msg = msg + element_str
        for element in row[1:]:
            element_str = '{:^{width}}'.format(element, width=3)
            msg = msg + element_str
        msg = msg 
        if i is not len(board) - 1:
            element_str = " " + len(board) * "{:^{width}}" .format("", width=3)
            msg = msg + element_str[:-1]
            msg = msg + '\n'
    print(string + "\n" + msg)


def main():
    size = board_size()
    board1 = init_board(size) # LÁTOM, megvan
    board2 = copy.deepcopy(board1)
    board2[0][0] = "j"
    print_board(board1)

if __name__ == "__main__":
    main()
