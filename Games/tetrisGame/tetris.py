import tkinter as tk
import random

# Constants
GAME_WIDTH = 300
GAME_HEIGHT = 600
CELL_SIZE = 30
COLUMNS = GAME_WIDTH // CELL_SIZE
ROWS = GAME_HEIGHT // CELL_SIZE
SPEED = 1000

# Shapes and their rotations
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[1, 1],
     [1, 1]],

    [[1, 1, 0],
     [0, 1, 1]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 1, 1]],

    [[1, 1, 1],
     [1, 0, 0]],

    [[1, 1, 1],
     [0, 0, 1]]
]

COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "cyan"]

class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("Tetris")
        
        self.canvas = tk.Canvas(root, width=GAME_WIDTH, height=GAME_HEIGHT, bg="black")
        self.canvas.grid(row=0, column=0, rowspan=20)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.grid(row=0, column=1, padx=10, pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_game)
        self.stop_button.grid(row=1, column=1, padx=10, pady=5)

        self.resume_button = tk.Button(root, text="Resume", command=self.resume_game)
        self.resume_button.grid(row=2, column=1, padx=10, pady=5)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=3, column=1, padx=10, pady=5)

        self.score = 0
        self.running = True

        self.board = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]

        self.current_shape = None
        self.current_color = None
        self.current_x = 0
        self.current_y = 0

        self.spawn_shape()
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.rotate_shape)

        self.update_game()

    def spawn_shape(self):
        self.current_shape = random.choice(SHAPES)
        self.current_color = random.choice(COLORS)
        self.current_x = COLUMNS // 2 - len(self.current_shape[0]) // 2
        self.current_y = 0

        if not self.is_valid_position():
            self.running = False
            self.game_over()

    def is_valid_position(self, x_offset=0, y_offset=0):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_x + x + x_offset
                    new_y = self.current_y + y + y_offset

                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS:
                        return False
                    if new_y >= 0 and self.board[new_y][new_x]:
                        return False
        return True

    def move_left(self, event):
        if self.is_valid_position(x_offset=-1):
            self.current_x -= 1

    def move_right(self, event):
        if self.is_valid_position(x_offset=1):
            self.current_x += 1

    def move_down(self, event=None):
        if self.is_valid_position(y_offset=1):
            self.current_y += 1
        else:
            self.place_shape()

    def rotate_shape(self, event):
        rotated_shape = list(zip(*self.current_shape[::-1]))
        original_shape = self.current_shape
        self.current_shape = rotated_shape
        if not self.is_valid_position():
            self.current_shape = original_shape

    def place_shape(self):
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_y + y][self.current_x + x] = self.current_color
        self.clear_lines()
        self.spawn_shape()

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(row)]
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [None for _ in range(COLUMNS)])
        self.score += len(lines_to_clear)
        self.score_label.config(text=f"Score: {self.score}")

    def game_over(self):
        self.canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2 - 20, text="Game Over", fill="white", font=("Arial", 24))
        self.canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2 + 20, text=f"Final Score: {self.score}", fill="white", font=("Arial", 18))

    def restart_game(self):
        self.score = 0
        self.running = True
        self.board = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.score_label.config(text="Score: 0")
        self.spawn_shape()
        self.update_game()

    def stop_game(self):
        self.running = False
        self.canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2 - 20, text="Game Stopped", fill="white", font=("Arial", 24))
        self.canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2 + 20, text=f"Score: {self.score}", fill="white", font=("Arial", 18))

    def resume_game(self):
        if not self.running:
            self.running = True
            self.update_game()

    def draw_board(self):
        self.canvas.delete("all")
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_cell(x, y, cell)

        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_cell(self.current_x + x, self.current_y + y, self.current_color)

    def draw_cell(self, x, y, color):
        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def update_game(self):
        if self.running:
            self.move_down()
            self.draw_board()
            self.root.after(SPEED, self.update_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = Tetris(root)
    root.mainloop()
