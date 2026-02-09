Tic-Tac-Toe (Human vs AI)

Overview

This project is a GUI-based Tic-Tac-Toe game built using Python Tkinter
where a human player competes against an AI opponent. The AI uses the
Minimax algorithm, which ensures optimal gameplay.

Features

-   Interactive graphical user interface\
-   Human vs AI gameplay\
-   Player can choose X or O\
-   AI uses Minimax algorithm (optimal decision making)\
-   Automatic win/draw detection\
-   Game reset after completion\
-   Smooth AI move delay for better gameplay experience

Technologies Used

-   Python\
-   Tkinter\
-   Minimax Algorithm

Game Logic

Player Selection

-   User selects either X or O\
-   If user chooses O, AI makes the first move

AI Behavior

-   AI evaluates all possible game states\
-   Maximizes AI winning chances\
-   Minimizes player winning chances\
-   Forces draw if player plays perfectly

Win Conditions

A player wins if they get three matching symbols in: - Any row\
- Any column\
- Either diagonal

User Interface

-   3 × 3 game grid\
-   Symbol selection dialog\
-   Game result popup messages\
-   Automatic board reset

How to Run the Game

### 1. Install Python

Make sure Python is installed on your system.

### 2. Run the Program

    python tictactoe.py

### 3. Choose Player Symbol

Select X or O and the game starts automatically.

Gameplay Instructions

1.  Click any empty cell to place your symbol\
2.  AI automatically makes its move\
3.  Continue until:
    -   You win\
    -   AI wins\
    -   Game ends in draw\
4.  Board resets automatically after each match

Algorithm Used: Minimax

The Minimax algorithm explores all possible moves and selects the best
possible outcome for the AI, guaranteeing optimal gameplay.

Limitations

-   AI difficulty cannot be adjusted\
-   Only supports single-player mode\
-   No score tracking system

Future Improvements

-   Add difficulty levels\
-   Add scoreboard system\
-   Add multiplayer mode\
-   Improve UI design and animations\
-   Add sound effects\
-   Add game history tracking
------------------------------------------------------------------------

## 👤 Author

Add your name here
