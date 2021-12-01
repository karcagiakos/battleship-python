import time
import os
import string
import copy
import random
import pygame


# pygame.init()
# pygame.font.init()
# pygame.mixer.init()
# s = "sound"
# music = pygame.mixer.music.load(os.path.join(s, "juppi.wav"))
# pygame.mixer.music.play(-1)


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


# def ai_move():
#     pass
# already_shooted = []# contain all the shots
# hit = False #False because we dont already hit a boat
# def AI_okos(move):
#     move = random.randint(0, 99)
#     if check_shot(move):
#         already_shooted.append(move)

#         if shooting_board[move] == 1:
#             change_shot(move)
#             hit = True
#             i = 1
#             nextshot = move + i

#         if shooting_board[nextshot] == 0:  #left --  1 coordinata 2 számból, 0-t board szél, 0-tól board magasság
#             i = 1
#             nextshot = shot - 1
#             if board_player_init[nextshot] == 1:
#                 change_shot(nextshot)
#                 i = i + 1
#                 nextshot = shot - i

#         elif shooting_board[nextshot] == 1:  #right
#             change_shot(nextshot)
#             i = i + 1
#             nextshot = shot + i

#         elif shooting_board[nextshot] == 0:
#             i = 1
#             nextshot = shot + 10
#             if shooting_board[nextshot] == 1:
#                 change_shot(nextshot)
#                 i = i + 10
#                 nextshot = shot + i
#         elif shooting_board[nextshot] == 0: #up
#                 i = 1
#                 nextshot = shot - 10
#                 if shooting_board[nextshot] == 1:
#                     change_shot(nextshot)
#                     i = i + 10
#                     nextshot = shot - i
#     pass

# def AI_béla(): # just a simple IA, kéne egy ciklus hogy ha nem valid a lövés akkor generáljon újat amíg nincs valid hely
#     shot = random.randint(0, 99)
#     if check_shot(shot):
#         already_shooted.append(shot)
#         pass


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


def mark(board, row, col, orient, key, value, dict):
    if board[row][col] == "🇴":
        if orient == "H":
            for i in range(value):
                board[row][col+i] = "🇽"
                coordinate = row, col+i
                dict[key] += [coordinate]
        elif orient == "V":
            for i in range(value):
                board[row+i][col] = "🇽"
                coordinate = row+i, col
                dict[key] += [coordinate]
    return dict


def win_conditions():
    pass

def placement_phase(board):
    ships = {"Big": 4, "Medium": 3, "Small": 2}
    dict = {"Big": [], "Medium": [], "Small": []}
    for key, value in ships.items():
        while True:
            print_board(board)
            move = get_move()
            is_valid, row, col, orient = is_valid_input(board, move)
            clear(1)
            if is_valid:
                break
        dict = mark(board, row, col, orient, key, value, dict)
        clear(0)
    print_board(board)
    print(dict)



def check_shot(move):#check if the shot has not already been fired
    pass
#     for i in range(len(already_shooted)):
#         if already_shooted[i] == move:
#             return False
#         return True

def shooting_phase():
    pass
#     def shooting_phase(player_1,player_1_placement_board):
#     board = player_1_placement_board 
#     player = player_1 #change_player(player)
#     move = get_move()
#     # board = [player_1_placement_board, player_2_placement_board] #change_board():
#     is_valid, row, col = is_valid_input(board, move)
#     if  board[row][col] != "🇽":
#         print("Missed!")
#         check_shot
#         change_shot(move)
#         print(board)
#     elif board[row][col] == "🇽":
#         print("Hit")
#         # if board[row+1][col] == "🇽":
#         #     return False
#         # elif board[row+1][col+1] == "🇽":
#         pass


# def change_shot(move):
#     del board_player_init[move]
#     board_player_init.insert(move, "🇽")
#     board[row][col] = "🇲"


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