import time
import os
import string
import copy
import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()
s = "sound"
music = pygame.mixer.music.load(os.path.join(s, "bg.flac"))
pygame.mixer.music.play(-1)


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
        player1 = input("Enter your name:\n- ")
        player2 = input("Enter your name:\n- ")
    return player1, player2


def get_move():
    move = input("\nPlease give valid cooridanates:\n- ")
    return move



already_shooted = []# contain all the shots
hit = False #False because we dont already hit a boat
def AI_okos(move):
    move = random.randint(0, 99)
    if check_shot(move):
        already_shooted.append(move)

        if shooting_board[move] == 1:
            change_shot(move)
            hit = True
            i = 1
            nextshot = move + i

        if shooting_board[nextshot] == 0:  #left
            i = 1
            nextshot = shot - 1
            if board_player_init[nextshot] == 1:
                change_shot(nextshot)
                i = i + 1
                nextshot = shot - i

        elif shooting_board[nextshot] == 1:  #right
            change_shot(nextshot)
            i = i + 1
            nextshot = shot + i

        elif shooting_board[nextshot] == 0:
            i = 1
            nextshot = shot + 10
            if shooting_board[nextshot] == 1:
                change_shot(nextshot)
                i = i + 10
                nextshot = shot + i
        elif shooting_board[nextshot] == 0: #up
                i = 1
                nextshot = shot - 10
                if shooting_board[nextshot] == 1:
                    change_shot(nextshot)
                    i = i + 10
                    nextshot = shot - i
    pass

def AI_béla(): # just a simple IA
    shot = random.randint(0, 99)
    if check_shot(shot):
        already_shooted.append(shot)
        pass

def check_shot(move):#check if the shot has not already been fired
    for i in range(len(already_shooted)):
        if already_shooted[i] == move:
            return False
        return True


def is_valid_input(board, move):
    move = move.upper()
    if len(move) == 2:
        if move[0].isalpha() and move[1].isnumeric():
            row = ord(move[0]) - 65
            col = int(move[1]) - 1
            if row > len(board)-1 or col > len(board)-1 or col == -1:
                print("Invalid input! Try again!")
                return False, 0, 0
            return True, row, col
        else:
            print("Invalid input! Try again!")
            return False, 0, 0
    elif len(move) == 3:
        if move[0].isalpha() and move[1].isnumeric() and move[2].isnumeric():
            row = ord(move[0]) - 65
            col = int(int(str(move[1]) + str(move[2])) ) - 1
            if row > len(board)-1 or col > len(board)-1 or col == -1:
                print("Invalid input! Try again!")
                return False, 0, 0
            return True, row, col
        else:
            print("Invalid input! Try again!")
            return False, 0, 0


# def mark(board, row, col):
#     if board[row][col] == "🇴":
#         board[row][col] = "🇭"


def win_conditions():
    pass


def placement_phase(board):
    while True:
        print_board(board)
        move = get_move()
        is_valid, row, col = is_valid_input(board, move)
        clear(1)
        if is_valid:
            break
    mark(board, row, col)
    clear(0)


def check_shot(shot):#check if the shot has not already been fired
    for i in range(len(already_shooted)):
        if already_shooted[i] == shot:
            return False
        return True

def shooting_phase(player_1,player_1_placement_board):
    board = player_1_placement_board 
    player = player_1 #change_player(player)
    move = get_move()
    # board = [player_1_placement_board, player_2_placement_board] #change_board():
    is_valid, row, col = is_valid_input(board, move)
    if  board[row][col] != "🇽":
        print("Missed!")
        change_shot(move)
        print(board)
    elif board[row][col] == "🇽":
        pass


def change_shot(move):
    del board_player_init[move]
    board_player_init.insert(move, "🇽")
    board[row][col] = "🇲"

def main():
    clear(0)
    player1, player2 = menu()
    clear(1)
    size = board_size()
    player_1_placement_board = init_board(size)
    #player_1_placement_board[1][1] = '🇽'
    # player_2_placement_board = copy.deepcopy(player_1_placement_board)
    # player_1_shooting_board = copy.deepcopy(player_1_placement_board)
    # player_2_shooting_board = copy.deepcopy(player_1_placement_board)
    clear(1)
    while True:
        placement_phase(player_1_placement_board)
        shooting_phase(player1,player_1_placement_board)
        if win_conditions():
            return


if __name__ == "__main__":
    main()
