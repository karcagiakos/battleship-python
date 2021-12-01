import time
import os
import string
import copy


def clear(s):
    time.sleep(s)
    os.system("cls||clear")


def menu():
    print("Welcome to Battleship!")


def board_size():
    clear(0)
    size = input("Board size: (X * X size)\n\n- ")
    while True:
        if size.isnumeric():
            print("\nLoading board size...")
            return int(size)
        else:
            print("\nLoading default board size...")
            return 5


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
    possible_modes = [ "HUMAN-HUMAN", "HUMAN-AI", "AI-HUMAN", "AI-AI" ]
    while True:
        mode = int(input("Please choose game mode:\n 1: HUMAN-HUMAN\n 2: HUMAN-AI\n 3: AI-HUMAN\n 4: AI-AI\nType the number of your choice.\n"))
        if mode not in range(1, len(possible_modes)+1):
            print("Invalid input")
            continue
        else:
            print(possible_modes[int(mode)-1])
            return possible_modes[int(mode)-1]
            


def get_players():
    # game mode alapján, ha van ai, random nevet adni neki
    player1 = input("Enter your name:\n- ")
    player2 = input("Enter your name:\n- ")
    return player1, player2


def change_player(player):
    if player == player1:
        pass
    # minden körben más lép


def get_move(board):
    # bekérni az inputot a felhasználótól
    # is_valid_input függvényt használni szabályos-e a lépés
    # átalakítani a betűket számmá, a visszaadott értékek 0-val kezdődjenek
    # ha lehetséges, ez a függvény legyen felhasználható placement és shooting phase alatt is
    while True:
        move = input("\nPlease give valid coordinates:\n- ")
        move = move.upper()
        if move == "QUIT" or move == "EXIT":
            print("Exit the game!")
            sys.exit()
        else:
            if len(move) == 2 and move[0].isalpha() and move[1].isnumeric():
                row = ord(move[0]) - 65
                col = int(move[1]) - 1
                if row > len(board)-1 or col > len(board)-1 or col == -1:
                    print("\nOut of the board!\n")
                    continue
                return row, col
            else:
                print("\nNot valid!\n")
    # kiszervezni a validálást az is_valid függvénybe!


def ai_move():
    # random lépések szabályoknak megfelelően
    # később lépések az alapján, hogy hova érdemes inkább lépni
    # ha lehetséges, ez a függvény legyen felhasználható placement és shooting phase alatt is
    pass


def is_valid_input():
    # ellenőrzi, phase-nek megfelelően, hogy az adott lépés, amit a felhasználó megad a get_move-ban, szabályos-e
    # szabályoknak megfelel
    # nincs kint a tábla határain
    # először egy betű, majd egy szám
    # nem foglalt-e már placement phase alatt az a hely
    # stb
    pass


def placement_phase(board):
    # player 1 kezd, leteszi a szabályoknak megfelelően az összes hajóját
    # player 2 következik
    # a hajók a placement boardokon tárolódnak
    print_board(board)
    row, col = get_move(board)
    mark(board, row, col)
    clear(0.5)



def shooting_phase(board, row, col, player):
    player = change_player(player)
    board = [player_1_placement_board, player_2_placement_board]
    row, col = get_move(board[i])
    if 
    # player 1 kezd,
    # tippel, a szabályoknak megfelelően történik valami a shooting boardon
    # a shooting board kerül kiprintelésre, és a hajók felfedésére a mark függvénnyel
    # körök vannak, player 2 második kör, és így tovább
    # win conditions ellenőrzi, hogy nyer-e valaki
    pass


def mark(board, row, col):
    # a játékos vagy az ai lépését felviszi a megfelelő játékos shooting boardjára
    # gyakorlatilag a visszakapott row, col értéket behelyetesíti a szabályoknak megfelelő betüvel
    # ellenőrzi, akár itt, akár egy külön függvényben, hogy egy hajó összes elemét megtalálták-e, ilyenkor elsüllyed
    if board[row][col] == "O":
        board[row][col] = "X"


def win_conditions():
    # turn limit, 50 kör után döntetlen
    # ha elsüllyed valaki összes hajója, nyer az ellenfél
    # stb, szabályoknak megfelelően
    pass


def main():
    clear(0)
    menu()
    clear(1)
    game_mode()
    player1, player2 = get_players()
    clear(1)
    size = board_size()
    player_1_placement_board = init_board(size)
    player_2_placement_board = copy.deepcopy(player_1_placement_board)
    player_1_shooting_board = copy.deepcopy(player_1_placement_board)
    player_2_shooting_board = copy.deepcopy(player_1_placement_board)
    clear(1)
    while True:
        placement_phase(player_1_placement_board)
        shooting_phase()
        if win_conditions():  # ekkor van vége a játéknak
            return


if __name__ == "__main__":
    main()

