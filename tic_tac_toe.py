import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("15x15 Tic-Tac-Toe")
        
        # Initial game state
        self.board = [[None for _ in range(15)] for _ in range(15)]
        self.current_player = "X"
        self.game_over = False

        # Create buttons for the 15x15 grid
        self.buttons = [
            [tk.Button(self.root, text="", width=4, height=2, font=("Arial", 14), 
                       command=lambda row=row, col=col: self.make_move(row, col)) 
             for col in range(15)] for row in range(15)
        ]

        # Place buttons in the window grid
        for row in range(15):
            for col in range(15):
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.game_over or self.board[row][col] is not None:
            return  # If cell is already filled or game is over, do nothing

        # Mark the button with the current player's symbol
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)

        # Check if someone has won
        if self.check_winner(row, col):
            self.game_over = True
            tk.messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")

        # Switch players
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        # Check horizontal, vertical, and both diagonals for 5 in a row
        return (self.check_line(row, col, 0, 1) or  # Horizontal
                self.check_line(row, col, 1, 0) or  # Vertical
                self.check_line(row, col, 1, 1) or  # Diagonal (top-left to bottom-right)
                self.check_line(row, col, 1, -1))   # Diagonal (top-right to bottom-left)

    def check_line(self, row, col, drow, dcol):
        # Check a line in the direction (drow, dcol) starting from (row, col)
        count = 0
        for i in range(-4, 5):  # Check 5 cells in both directions
            r, c = row + i * drow, col + i * dcol
            if 0 <= r < 15 and 0 <= c < 15 and self.board[r][c] == self.current_player:
                count += 1
            else:
                count = 0
            if count == 5:  # If we have 5 in a row, we have a winner
                return True
        return False

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
