class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        row1 = '| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2])
        row2 = '| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5])
        row3 = '| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def has_won(self, player):
        winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False

    def is_draw(self):
        return ' ' not in self.board

    def minimax(self, depth, is_maximizing):
        if self.has_won('X'):
            return -10 + depth
        elif self.has_won('O'):
            return 10 - depth
        elif self.is_draw():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    score = self.minimax(depth + 1, False)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    score = self.minimax(depth + 1, True)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def ai_move(self):
        best_score = float('-inf')
        best_move = 0
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = 'O'

    def play(self):
        while True:
            self.print_board()
            move = input("Enter your move (1-9): ")
            if self.board[int(move) - 1] != ' ':
                print("Invalid move, try again.")
                continue
            self.board[int(move) - 1] = 'X'
            if self.has_won('X'):
                self.print_board()
                print("You win!")
                break
            elif self.is_draw():
                self.print_board()
                print("It's a draw!")
                break
            self.ai_move()
            if self.has_won('O'):
                self.print_board()
                print("AI wins!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()