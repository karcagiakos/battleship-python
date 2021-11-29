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
    # human vs. human, ai vs. human, ai vs. ai
    pass


def get_players():
    # game mode alapján, ha van ai, random nevet adni neki
    player1 = input("Enter your name:\n- ")
    player2 = input("Enter your name:\n- ")
    return player1, player2


def get_move():
    # bekérni az inputot a felhasználótól
    # is_valid_input függvényt használni szabályos-e a lépés
    # átalakítani a betűket számmá, a visszaadott értékek 0-val kezdődjenek
    # ha lehetséges, ez a függvény legyen felhasználható placement és shooting phase alatt is
    pass


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


def placement_phase():
    # player 1 kezd, leteszi a szabályoknak megfelelően az összes hajóját
    # player 2 következik
    # a hajók a placement boardokon tárolódnak
    pass


def shooting_phase():
    # player 1 kezd,
    # tippel, a szabályoknak megfelelően történik valami a shooting boardon
    # a shooting board kerül kiprintelésre, és a hajók felfedésére a mark függvénnyel
    # körök vannak, player 2 második kör, és így tovább
    # win conditions ellenőrzi, hogy nyer-e valaki
    pass


def mark():
    # a játékos vagy az ai lépését felviszi a megfelelő játékos shooting boardjára
    # gyakorlatilag a visszakapott row, col értéket behelyetesíti a szabályoknak megfelelő betüvel
    # ellenőrzi, akár itt, akár egy külön függvényben, hogy egy hajó összes elemét megtalálták-e, ilyenkor elsüllyed
    pass


def win_conditions():
    # turn limit, 50 kör után döntetlen
    # ha elsüllyed valaki összes hajója, nyer az ellenfél
    # stb, szabályoknak megfelelően
    pass


def main():
    clear(0)
    menu()
    clear(1)
    player1, player2 = get_players()
    clear(1)
    size = board_size()
    player_1_placement_board = init_board(size)
    player_2_placement_board = copy.deepcopy(player_1_placement_board)
    player_1_shooting_board = copy.deepcopy(player_1_placement_board)
    player_2_shooting_board = copy.deepcopy(player_1_placement_board)
    clear(1)
    print_board(player_1_placement_board)
    while True:
        placement_phase()
        shooting_phase()
        if win_conditions():  # ekkor van vége a játéknak
            return


if __name__ == "__main__":
    main()
