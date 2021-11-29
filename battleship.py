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


def players_choice():
    if mode == 1:
        player_1 = input("Enter name of Player 1: ")
        player_2 = input("Enter name of Player 2: ")
    elif mode == 2:
        player_1 = input("Enter your name: ")
        player_2 = names.get_first_name()
    elif mode == 3:
        player_1 = names.get_first_name()
        player_2 = input("Enter your name: ")
    elif mode == 4:
        player_1 = names.get_first_name()
        player_2 = names.get_first_name()


def game_mode():
    possible_modes = ["HUMAN-HUMAN", "HUMAN-AI", "AI-HUMAN", "AI-AI"]
    
    while True:
        mode = input("Please choose between:\n HUMAN-HUMAN\n HUMAN-AI\n AI-HUMAN\n AI-AI\nGame modes!\nType the name of your choice.\n")
        if mode.upper() in possible_modes:
            game(mode.upper(), size)
            break
        elif mode.upper() == 'QUIT':
            exit()


def get_move(board):
    while True:
        move = input("Please give valid coordinates:\n- ")
        move = move.upper()
        if move == "QUIT" or move == "EXIT":
            print("\nQuit.")
            sys.exit()
        else:
            if len(move) == 2 or len(move) == 3 and move[0].isalpha() and move[1:].isnumeric():
                row = ord(move[0]) - 65
                col = int(move[1:]) - 1
                if row > len(board)-1 or col > len(board)-1 or col == -1:
                    print("\nOut of the board!\n")
                    clear(1)
                    continue
                return row, col
            else:
                print("\nNot valid!\n")
                clear(1)
                # continue


def ai_move():
    #random or intelligence
    pass


def win_condition():
    pass


def hit_or_miss():
    pass


def placement_phase():
    #direct (or random)
    pass


def shooting_phase():
    pass


def board_size():
    clear(0)
    board_size = getpass.getpass("Board size: (X * X size)\n\n- ")
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
    board = init_board(size) # LÁTOM, megvan
    board_copy = copy.deepcopy(board)
    board_copy[0][0] = "j"
    print_board(board)
    print_board(board_copy)
    row, col = get_move(board)



if __name__ == "__main__":
    main()
