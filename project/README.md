# Tic-Tac-Toe Game

## Project Title: Tic-Tac
This project implements a simple Tic-Tac-Toe game using Python and Tkinter for the GUI.

## Video Demo: <https://youtu.be/8Xog4EoCdnQ>

## Author
- **Name**: Sk Rajiuddin
- **GitHub Username**: [@Rajiuddin786](https://github.com/Rajiuddin786)
- **Edx Username**: skrajiuddin
- **City/Country**: Kolkata, India
- **Date**: 20/07/2024

## Description
This project is a comprehensive implementation of the classic Tic-Tac-Toe game, created using Python and the Tkinter library for the graphical user interface. Tic-Tac-Toe, also known as Noughts and Crosses or Xs and Os, is a straightforward yet engaging game where two players take turns marking spaces in a 3x3 grid with their respective symbols, typically "X" and "O". The objective is to align three of one's symbols in a row, column, or diagonal before the opponent. In main funtion I have make the "root" global so that other funtion can assess it. The root contains the basic to initiate the tkinter. I have also used ".title()" function to give title to the game. After the I called the "add_grid()" funtion to add button for the game. I have passed an empty 2D Matrix of 3X3 named buttons into add_grid(). This matrix keeps a real time track of the game. While creating button we have pass another funtion "on_click_button()" which keeps track of the button clicked by the player. Here, we check if a box is empty or not using the buttons matrix if the box is empty then we simply add the player's logo onto the button or box. We also check for winner , draw or switching the player in this funtion. The check_winner() funtion simply check if a condition satify or not. It has all the possible combination in a tic-tac-toe game. The check_draw() simply check if boxes are empty or not. If it is empty then the match continue or else it is a draw. After a draw or game over thr reset_game() funtion resets the whole board and player can play it again.

The technical requirements for this project are minimal. It is developed in Python 3.x and uses Tkinter, which is included with Python, so no additional installations are necessary. The project can be easily set up by cloning the repository from GitHub and running the main script.

In summary, this Tic-Tac-Toe project combines the classic gameplay of Tic-Tac-Toe with modern programming techniques to create a fun and interactive experience. Its user-friendly interface, real-time win and draw detection, and easy reset functionality make it a great way for two players to enjoy this timeless game on a computer.

## Features
- Two-player gameplay (Player X and Player O)
- Graphical User Interface (GUI) using Tkinter
- Detection of winning moves
- Detection of draw games
- Game reset functionality

## Requirements
- Python 3.x
- Tkinter (usually included with Python)


## Usage
Run the game by executing the main script:
```bash
python project.py
