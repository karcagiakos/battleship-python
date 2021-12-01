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
        print("Invalid input! Try again!")
        clear(1)


def init_board(size=5):
    board = [["🇴"] * size for i in range(size)]
    return board


def print_board(board):
    alphabet = list(string.ascii_uppercase)
    line = "    "
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
        print("Invalid input! Try again!")
        clear(1)


def players(mode):
    if mode == 1:
        player1 = input("Enter your name:\n- ")
        player2 = "AI"
    else:
        player1 = input("Enter Player 1 name:\n- ")
        player2 = input("Enter Player 2 name:\n- ")
    return player1, player2


def get_move():
    move = input("\nPlease give valid cooridanates:\n- ")
    return move


def ai_move():
    pass


def is_valid_input(board, move):
    move = move.upper()
    if len(move) == 3:
        if move[0].isalpha() and move[1].isnumeric() and move[2].isalpha():
            row = ord(move[0]) - 65
            col = int(move[1]) - 1
            orient = move[2]
            if row > len(board)-1 or col > len(board)-1 or col == -1 or orient != "H" and orient != "V":
                print("Invalid input! Try again!")
                return False, 0, 0, 0
            return True, row, col, orient
        else:
            print("Invalid input! Try again!")
            return False, 0, 0, 0

    elif len(move) == 4:
        if move[0].isalpha() and move[1].isnumeric() and move[2].isnumeric() and move[3].isalpha():
            row = ord(move[0]) - 65
            col = int(int(str(move[1]) + str(move[2])) ) - 1
            orient = move[3]
            if row > len(board)-1 or col > len(board)-1 or col == -1 or orient != "H" and orient != "V":
                print("Invalid input! Try again!")
                return False, 0, 0, 0
            return True, row, col, orient
        else:
            print("Invalid input! Try again!")
            return False, 0, 0, 0
    else:
        print("Invalid input! Try again!")
        return False, 0, 0, 0


def mark(board, row, col, orient, value):
    if board[row][col] == "🇴":
        if orient == "H":
            for i in range(value):
                board[row][col+i] = "🇭"
        elif orient == "V":
            for i in range(value):
                board[row+i][col] = "🇭"


def win_conditions():
    pass


def placement_phase(board):
    ships = {"Big": 4, "Medium": 3, "Small": 2}
    for value in ships.values():
        while True:
            print_board(board)
            move = get_move()
            is_valid, row, col, orient = is_valid_input(board, move)
            clear(1)
            if is_valid:
                break
        mark(board, row, col, orient, value)
        clear(0)
    print_board(board)


def check_shot(shot):#check if the shot has not already been fired
    for i in range(len(previous_shots)):
        if previous_shots[i] == shot:
            return False
    return True


def shooting_phase():
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
    placement_phase(player_1_placement_board)
    shooting_phase()
    if win_conditions():
        return


if __name__ == "__main__":
    main()
