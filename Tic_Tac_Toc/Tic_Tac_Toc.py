import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[3J\033[2J\033[H", end="", flush=True)


class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")

            if name.replace(" ", "").isalpha():
                self.name = name
                break

            print("Please enter letters only")

    def choose_symbol(self):
        while True:
            symbol = input(
                f"{self.name}, choose your symbol (a single letter): [X/O]\n"
            )

            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break

            print("Invalid symbol")


class Menu:
    def display(self):
        print("Welcome to my X-O game!")
        print("1. Start Game")
        print("2. Quit Game")

        choice = input("Enter your choice (1 or 2): ")
        return choice

    def display_end_game_menu(self):
        menu_text = """Game over!
1. Restart Game
2. Quit Game
Enter your choice (1 or 2):
"""
        choice = input(menu_text)
        return choice


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))

            if i < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True

        return False

    def is_valid_move(self, choice):
        return 1 <= choice <= 9 and self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        clear_screen()
        choice = self.menu.display()

        if choice == "1":
            self.setup_players()
            clear_screen()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details: ")
            player.choose_name()
            player.choose_symbol()

            if number == 2:
                while player.symbol == self.players[0].symbol:
                    print("This symbol is already taken.")
                    player.choose_symbol()

            print("-" * 20)

    def play_game(self):
        while True:
            self.play_turn()

            won = self.check_win()
            draw = self.check_draw()

            if won or draw:
                self.board.display_board()

                if won:
                    player = self.players[self.current_player_index]
                    print(f"{player.name} wins!")
                else:
                    print("It's a draw!")

                choice = self.menu.display_end_game_menu()

                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            else:
                self.switch_player()

    def quit_game(self):
        print("Thank you for playing!")

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")

        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                clear_screen()

                if self.board.update_board(cell_choice, player.symbol):
                    break

                self.board.display_board()
                print(f"{player.name}'s turn ({player.symbol})")
                print("Invalid move, try again.")

            except ValueError:
                print("Please enter a number between 1 and 9.")

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        clear_screen()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_combinations:
            if (
                self.board.board[combo[0]]
                == self.board.board[combo[1]]
                == self.board.board[combo[2]]
            ):
                return True

        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)


game = Game()
game.start_game()