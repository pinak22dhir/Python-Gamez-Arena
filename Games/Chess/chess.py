import tkinter as tk
from tkinter import messagebox

# Initialize the main application
class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")

        # Set up the board
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.squares = []
        self.create_board()

        # Initialize game state
        self.selected_piece = None
        self.turn = "white"
        self.pieces = self.initialize_pieces()
        self.place_pieces()

    def create_board(self):
        for row in range(8):
            row_squares = []
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                square = tk.Label(self.board_frame, bg=color, width=8, height=4)
                square.grid(row=row, column=col)
                square.bind("<Button-1>", lambda e, r=row, c=col: self.on_square_click(r, c))
                row_squares.append(square)
            self.squares.append(row_squares)

    def initialize_pieces(self):
        pieces = {}
        
        # Define pawns
        for i in range(8):
            pieces[(1, i)] = ("Pawn", "black")
            pieces[(6, i)] = ("Pawn", "white")

        # Define other pieces
        piece_order = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
        for i, piece in enumerate(piece_order):
            pieces[(0, i)] = (piece, "black")
            pieces[(7, i)] = (piece, "white")

        return pieces

    def place_pieces(self):
        for position, (piece, color) in self.pieces.items():
            row, col = position
            text_color = "blue" if color == "white" else "green"
            self.squares[row][col].config(text=piece, fg=text_color)

    def on_square_click(self, row, col):
        if self.selected_piece:
            self.move_piece(row, col)
        else:
            self.select_piece(row, col)

    def select_piece(self, row, col):
        piece = self.pieces.get((row, col))
        if piece and piece[1] == self.turn:
            self.selected_piece = (row, col)
            self.squares[row][col].config(bg="yellow")
        else:
            messagebox.showinfo("Invalid Move", "Select a valid piece to move.")

    def move_piece(self, row, col):
        old_row, old_col = self.selected_piece

        if (row, col) in self.pieces and self.pieces[(row, col)][1] == self.turn:
            messagebox.showinfo("Invalid Move", "Cannot capture your own piece.")
            self.reset_selection()
            return

        # Update pieces
        self.pieces[(row, col)] = self.pieces.pop((old_row, old_col))
        
        # Update board visuals
        self.reset_board()
        self.place_pieces()

        # Update turn
        self.turn = "black" if self.turn == "white" else "white"
        self.reset_selection()

    def reset_selection(self):
        old_row, old_col = self.selected_piece
        color = "white" if (old_row + old_col) % 2 == 0 else "black"
        self.squares[old_row][old_col].config(bg=color)
        self.selected_piece = None

    def reset_board(self):
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                self.squares[row][col].config(text="", bg=color)

# Main driver code
if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()
