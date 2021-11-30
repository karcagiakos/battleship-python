import time
import os
import string
import copy


def clear(s):
    time.sleep(s)
    os.system("cls||clear")


def menu():
    print("Welcome to Battleship! You will sink!")
    clear(1)
    mode = game_mode()
    clear(1)
    player1, player2 = players(mode)
    return player1, player2


def board_size():
    while True:
        size = input("Board size: \n- ")
        if size.isnumeric() and int(size) < 11 and int(size) > 0:
            return int(size)
        clear(0)


def init_board(size=5):
    board = [["O"] * size for i in range(size)]
    return board


def print_board(board):
    alphabet = list(string.ascii_uppercase)
    line = "   "
    for letter in range(len(board[0])):
        line += str(letter+1) + "  "
    print(line+"\n")
    for row in range(len(board)):
        print(alphabet[row], end="  ")
        for col in range(len(board[0])):
            print(board[row][col], end="  ")
        print()


def game_mode():
    while True:
        print("1. Single player")
        print("2. Multiplayer")
        mode = input("- ")
        if mode.isnumeric() and int(mode) < 3 and int(mode) > 0:
            return int(mode)
        clear(0)


def players(mode):
    if mode == 1:
        player1 = input("Enter your name:\n- ")
        player2 = "AI"
    else:
        player1 = input("Enter your name:\n- ")
        player2 = input("Enter your name:\n- ")
    return player1, player2


def get_move():
    move = input("\nPlease give valid cooridantes:\n- ")
    return move


def ai_move():
    pass


def is_valid_input(board, move):
    move = move.upper()
    if len(move) == 2 and move[0].isalpha() and move[1].isnumeric():
        row = ord(move[0]) - 65
        col = int(move[1]) - 1
        if row > len(board)-1 or col > len(board)-1 or col == -1:
            print("\nOut of the board!\n")
            return False
        return True
    else:
        print("\nNot valid!\n")
        return False


def placement_phase(board):
    while True:
        print_board(board)
        move = get_move()
        is_valid = is_valid_input(board, move)
        clear(1)
        if is_valid:
            break
    row = ord(move[0]) - 97
    col = int(move[1]) - 1
    mark(board, row, col)
    clear(0)


def shooting_phase():
    pass


def mark(board, row, col):
    if board[row][col] == "O":
        board[row][col] = "X"


def win_conditions():
    pass


def main():
    clear(0)
    player1, player2 = menu()
    clear(1)
    size = board_size()
    player_1_placement_board = init_board(size)
    # player_2_placement_board = copy.deepcopy(player_1_placement_board)
    # player_1_shooting_board = copy.deepcopy(player_1_placement_board)
    # player_2_shooting_board = copy.deepcopy(player_1_placement_board)
    clear(1)
    while True:
        placement_phase(player_1_placement_board)
        shooting_phase()
        if win_conditions():
            return


if __name__ == "__main__":
    main()
