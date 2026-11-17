\# Tic-Tac-Toe — Python OOP Project



A two-player command-line Tic-Tac-Toe game built to practise

Python and object-oriented programming as part of my learning

journey toward machine learning engineering.



\## Features



\- Custom player names and unique letter symbols.

\- Input validation for player details and moves.

\- Automatic turn switching after valid moves.

\- Win detection across rows, columns, and diagonals.

\- Draw detection when the board is full and no player wins.

\- Restart option to play again.



\## Code Structure



The game is organised into four classes:



| Class | Responsibility |

|-------|----------------|

| Player | Handles player names and symbol selection. |

| Board | Stores, displays, updates, and resets the board. |

| Menu | Displays the start and end-of-game menus. |

| Game | Manages setup, turns, win and draw checks, and restarts. |



\## Requirements



\- Python 3.

\- A terminal, such as Command Prompt or PowerShell.



No third-party Python packages are required.



\## How to Run



1\. Download or clone this repository.

2\. Open a terminal in the main project folder containing this README.

3\. Run:



```bash

python Tic\_Tac\_Toc/Tic\_Tac\_Toc.py

```



On Windows, if `python` is not recognised, try:



```bash

py Tic\_Tac\_Toc/Tic\_Tac\_Toc.py

```



\## How to Play



1\. Choose Start Game.

2\. Enter each player's name and choose different letter symbols.

3\. Take turns selecting an available cell from 1 to 9.

4\. Get three matching symbols in a row, column, or diagonal to win.

5\. After the game ends, choose to restart or quit.



\## What I Practised



\- Creating classes, objects, attributes, and methods.

\- Separating responsibilities across classes.

\- Using loops and conditions to control game flow.

\- Validating input and handling errors with try/except.

\- Working with lists and checking winning combinations.



\## Project Scope



This is a learning project focused on Python fundamentals and OOP.

It runs in the terminal and supports two human players.

