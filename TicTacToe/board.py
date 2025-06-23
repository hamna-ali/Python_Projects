import numpy as np

class Board:
    SYMBOLS = {0: " ", 1: "*", 2: "O"}  # Mapping numbers to symbols
    POSITIONS = {i: ((i - 1) // 3, (i - 1) % 3) for i in range(1, 10)}  # Mapping 1-9 to row, col

    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)  # Initialize empty 3x3 board

    def print_board(self):
        print("\nCurrent Board:")
        for i in range(3):
            print(" | ".join(Board.SYMBOLS[self.board[i][j]] for j in range(3)))
            if i < 2:
                print("-" * 9)

    def is_empty(self, row, col):
        return self.board[row][col] == 0

    def place_move(self, box_number, player):
        if box_number in Board.POSITIONS:
            row, col = Board.POSITIONS[box_number]
            if self.is_empty(row, col):
                self.board[row][col] = player
                return True
        return False

    def is_winner(self, player):
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(self.board[i][j] != 0 for i in range(3) for j in range(3))

    def available_moves(self):
        return [key for key, (i, j) in Board.POSITIONS.items() if self.board[i][j] == 0]

    def game_over(self):
        return self.is_winner(1) or self.is_winner(2) or self.is_full()

    def reset_board(self):
        self.board = np.zeros((3, 3), dtype=int)