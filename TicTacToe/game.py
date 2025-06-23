import random
from board import Board
class Game:
    def __init__(self):
        self.board = Board()
        self.user_symbol, self.ai_symbol = self.choose_symbol()
        self.user_player = 1 if self.user_symbol == "*" else 2
        self.ai_player = 2 if self.user_player == 1 else 1
        self.current_player = 1  # Player 1 always starts

    def choose_symbol(self):
        while True:
            symbol = input("Choose your symbol (* or O): ").strip()
            if symbol == "*":
                return "*", "O"
            elif symbol.upper() == "O":
                return "O", "*"
            else:
                print("Invalid choice. Please choose '*' or 'O'.")

    def switch_player(self):
        self.current_player = 2 if self.current_player == 1 else 1

    def play_random_move(self):
        available_moves = self.board.available_moves()
        if available_moves:
            move = random.choice(available_moves)
            self.board.place_move(move, self.current_player)
            return move
        return None

    def play_game(self):
        while not self.board.game_over():
            self.board.print_board()
            if self.current_player == self.user_player:
                print(f"Your turn ({self.user_symbol}):")
                print("Enter a box number (1-9) from left to right, top to bottom.")
                while True:
                    try:
                        box_number = int(input("Box number: "))
                        if self.board.place_move(box_number, self.current_player):
                            break
                        else:
                            print("Invalid move. Try again.")
                    except ValueError:
                        print("Invalid input. Enter a number between 1 and 9.")
            else:
                print("AI is making a move...")
                self.play_random_move()

            self.switch_player()

        self.board.print_board()
        if self.board.is_winner(self.user_player):
            print("You win!!")
        elif self.board.is_winner(self.ai_player):
            print("AI wins!!")
        else:
            print("It's a draw!!")

        self.board.reset_board()
