import time
import os
import string
import copy
# import random
# import pygame


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


def change_player(player, player1, player2):
    if player == player1:
        player = player2
    else:
        player = player1
    return player


def players(mode):
    if mode == 1:
        player1 = input("Enter your name:\n- ")
        player2 = "AI"
    else:
        player1 = input("Enter Player 1 name:\n- ")
        player2 = input("Enter Player 2 name:\n- ")
    return player1, player2


def get_move():
    move = input("\nPlease give valid coordinates:\n- ")
    return move


def ai_move():
    pass
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


def AI_béla():
    pass
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
            col = int(int(str(move[1]) + str(move[2]))) - 1
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
    while True:
        try:
            if board[row][col] == "🇴":
                if orient == "H":
                    for i in range(value):
                        if col+value <= len(board):
                            board[row][col+i] = "🇽"
                            coordinate = row, col+i
                            dict[key] += [coordinate]
                        else:
                            raise IndexError
                elif orient == "V":
                    for i in range(value):
                        if row+value <= len(board):
                            board[row+i][col] = "🇽"
                            coordinate = row+i, col
                            dict[key] += [coordinate]
                        else:
                            raise IndexError
        except IndexError:
            while True:
                print("Rossz!")
                move = get_move()
                is_valid, row, col, orient = is_valid_input(board, move)
                if not is_valid or not check_shot(row, col, dict, key, orient, board):
                    continue
                else:
                    break
            continue
        return dict


def win_conditions():
    pass



def check_shot(row, col, dict, key, orient, board):
    if key == "Big":
        if orient == "H":
            for i in dict.values():
                for y in range(len(i)):
                    if (row, col) == i[y] or (row, col+1) == i[y] or (row, col+2) or (row, col+3) == i[y]:
                        print("rossz")
                        return False
            print("jó")
            return True
        elif orient == "V":
            for i in dict.values():
                for y in range(len(i)):
                    if (row, col) == i[y] or (row+1, col) == i[y] or (row+2, col) or (row+3, col) == i[y]:
                        print("rossz")
                        return False
            print("jó")
            return True
    elif key == "Medium":
        if orient == "H":
            try:
                for i in dict.values():
                    for y in range(len(i)):
                        if (row, col) == i[y] or (row, col+1) == i[y] or (row, col+2) == i[y] or board[row][col+3] == "🇽" or board[row][col-1] == "🇽" or board[row+1][col] == "🇽" or board[row+1][col+1] == "🇽" or board[row+1][col+2] == "🇽" or board[row-1][col] == "🇽" or board[row-1][col+1] == "🇽" or board[row-1][col+2] == "🇽":
                            print("rossz")
                            return False
            except IndexError:
                if col+3 <= len(board):
                    return True
                print("rossz")
                return False
            print("jó")
            return True
        elif orient == "V":
            try:
                for i in dict.values():
                    for y in range(len(i)):
                        if (row, col) == i[y] or (row+1, col) == i[y] or (row+2, col) == i[y] or board[row+3][col] == "🇽" or board[row-1][col] == "🇽" or board[row][col+1] == "🇽" or board[row+1][col+1] == "🇽" or board[row+2][col+1] == "🇽" or board[row][col-1] == "🇽" or board[row+1][col-1] == "🇽" or board[row+2][col-1] == "🇽":
                            print("rossz")
                            return False
            except IndexError:
                if row+3 <= len(board):
                    return True
                print("rossz")
                return False
            print("jó")
            return True
    elif key == "Small":
        if orient == "H":
            try:
                for i in dict.values():
                    for y in range(len(i)):
                        if (row, col) == i[y] or (row, col+1) == i[y] or board[row][col+2] == "🇽" or board[row][col-1] == "🇽" or board[row+1][col] == "🇽" or board[row+1][col+1] == "🇽" or board[row-1][col] == "🇽" or board[row-1][col+1] == "🇽":
                            print("rossz")
                            return False
            except IndexError:
                if col+2 <= len(board):
                    return True
                print("rossz")
                return False
            print("jó")
            return True
        elif orient == "V":
            for i in dict.values():
                try:
                    for y in range(len(i)):
                        if (row, col) == i[y] or (row+1, col) == i[y] or board[row+2][col] == "🇽" or board[row-1][col] == "🇽" or board[row][col+1] == "🇽" or board[row+1][col+1] == "🇽" or board[row][col-1] == "🇽" or board[row+1][col-1] == "🇽":
                            print("rossz")
                            return False
                except IndexError:
                    if row+2 <= len(board):
                        return True
                    print("rossz")
                    return False
            print("jó")
            return True


def can_shoot(move, hits_list, board): # Ellenőrzi, hogy a lövés valid helyre történt-e
    move = move.upper()
    while True:
        if len(move) == 2:
            if move[0].isalpha() and move[1].isnumeric() and int(move[1]) <= len(board):
                row = ord(move[0]) - 65
                col = int(move[1]) - 1
                if (row, col) in hits_list:
                    print("rossz")
                    return False, 0, 0
                return True, row, col
        elif len(move) == 3:
            if move[0].isalpha() and move[1:].isnumeric() and int(move[1:]) <= len(board):
                row = ord(move[0]) - 65
                col = int(move[1:]) - 1
                if (row, col) in hits_list:
                    return False, 0, 0
                return True, row, col

    
def placement_phase(board1, board2, player1, player2):
    player = player1
    
    ships = {"Big": 4, "Medium": 3, "Small": 2}
    
    dict = {"Big": [], "Medium": [], "Small": []}
    dict2 = {"Big": [], "Medium": [], "Small": []}

    while player == player1:
        for key, value in ships.items():
            while True:
                print_board(board1)
                move = get_move()
                is_valid, row, col, orient = is_valid_input(board1, move)
                clear(1)
                if not is_valid or not check_shot(row, col, dict, key, orient, board1):
                    continue
                else:
                    break
            dict = mark(board1, row, col, orient, key, value, dict)
            clear(0)
        print_board(board1)
        player = change_player(player, player1, player2)
        break
    input("Next player's placement phase")
    while player == player2:
        for key, value in ships.items():
            while True:
                print_board(board2)
                move = get_move()
                is_valid, row, col, orient = is_valid_input(board2, move)
                clear(1)
                if not is_valid or not check_shot(row, col, dict2, key, orient, board2):
                    continue
                else:
                    break
            dict2 = mark(board2, row, col, orient, key, value, dict2)
            clear(0)
        print_board(board2)
        break
    print(dict)
    print(dict2)
    return dict, dict2


# already_shooted = []# contain all the shots
def shooting_phase(board1, board2, dict1, dict2, player1, player2):
    player = player1
    guesses1 = []
    guesses2 = []
    while player == player1:
        clear(1)
        print_board(board2)
        move = get_move()
        valid, row, col = can_shoot(move, guesses1, board2)
        if valid == False:
            continue
        else:
            break
    for key, value in dict2.items():
        if (row, col) in value:
            guesses1.append((row, col))
    board2 = change_shot(row, col, board2)
    clear(1)
    print_board(board2)


    # if row, col in dict2:
    #     if dict2.keys() összes elem hit = elsüllyed
    #     return hit
    # else:
    #     return miss
    #     board2[row][col] = "M"
    #     print_board(board2)



    # board = board1
    # player = player_1 #change_player(player)
    # move = get_move()
    # # board = [player_1_placement_board, player_2_placement_board] #change_board():
    # is_valid, row, col = is_valid_input(board, move)
    # if  board[row][col] != "🇽":
    #     print("Missed!")
    #     check_shot
    #     change_shot(move)
    #     print(board)
    # elif board[row][col] == "🇽":
    #     print("Hit")
    #     # if board[row+1][col] == "🇽":
    #     #     return False
    #     # elif board[row+1][col+1] == "🇽":
    #     pass


def change_shot(row, col, board):
    if board[row][col] == "🇴":
        board[row][col] == "🇲"
    elif board[row][col] == "🇽":
        board[row][col] == "🇭"
    return board


    #     del board_player_init[move]
    #     board_player_init.insert(move, "🇽")
    #     board[row][col] = "🇲"


def main():
    clear(0)
    player1, player2 = menu()
    clear(1)
    size = board_size()
    player_1_placement_board = init_board(size)
    player_2_placement_board = copy.deepcopy(player_1_placement_board)
    player_1_shooting_board = copy.deepcopy(player_1_placement_board)
    player_2_shooting_board = copy.deepcopy(player_1_placement_board)
    clear(1)
    dict1, dict2 = placement_phase(player_1_placement_board, player_2_placement_board, player1, player2)
    shooting_phase(player_1_shooting_board, player_2_shooting_board, dict1, dict2, player1, player2)
    if win_conditions():
        return


if __name__ == "__main__":
    main()