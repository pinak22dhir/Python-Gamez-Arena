Chess Game Application

This is a simple chess game application built using Python's Tkinter library. It provides a graphical chessboard interface where players can interact by clicking on pieces to select and move them.

Features

Graphical Chessboard: An 8x8 board with alternating black and white squares.

Piece Placement: Standard initial chess setup with pawns, rooks, knights, bishops, queens, and kings for both black and white sides.

Turn-Based Movement: Players can select and move pieces one at a time, alternating between white and black turns.

Piece Highlighting: Highlights the selected piece to indicate it's ready for a move.

Error Handling: Displays messages for invalid moves or selections.

Requirements

Python 3.x

Tkinter (included with most Python installations)

How to Run

Clone the repository or copy the code:
```
git clone https://github.com/yourusername/chess-game.git

cd chess-game
```
Run the script:

python chess_game.py

Play the game:

Click on a piece to select it.

Click on a valid square to move the selected piece.

The game enforces turn-based play and prevents invalid moves like capturing your own pieces.

How It Works

Chessboard Creation:

The chessboard is represented as an 8x8 grid of Label widgets, styled with alternating colors.

Piece Initialization:

The initialize_pieces method sets up the initial positions of all pieces.

Piece Movement:

Players click on a piece to select it, and then click on a destination square to move it.

The move_piece method handles piece movement, ensuring turns alternate and moves are valid.

Visual Updates:

The reset_board and place_pieces methods handle updating the board's appearance after each move.

Turn Management:

The turn attribute tracks whose turn it is ("white" or "black").

Limitations

The current implementation does not enforce chess rules like legal moves, check, checkmate, or stalemate.

The game is not designed for AI or network play.

Capturing is allowed but does not display captured pieces.

Future Enhancements

Add rules for legal moves for each piece type.

Implement check and checkmate detection.

Provide an undo feature to revert moves.

Integrate AI for single-player mode.

Improve the UI with piece icons instead of text labels.

File Structure
```
chess_game.py      # Main script for the Chess game
README.md          # Documentation file
```
Screenshots
![Chessgame](screenshots/image.png)