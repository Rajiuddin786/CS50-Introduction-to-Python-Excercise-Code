"""
Project Title: Tic-Tac
Name: Sk Rajiuddin
Git-Hub UserName: @Rajiuddin786
Edx UserName: skrajiuddin
City/Country: Kolkata/India
Date: 20/07/2024
"""
import tkinter as tk
from tkinter import messagebox



current_player = "X"
def main():
    global root
    root=tk.Tk()
    root.title("TIK_TAC Game")
    buttons = [[None for _ in range(3)] for _ in range(3)]
    add_grid(buttons)
    root.mainloop()


def add_grid(buttons):
    for row in range(3):
        for col in range(3):
            button = tk.Button(root,text="",font='normal 30 bold',height=3,width=6,command=lambda r=row ,c=col:on_button_click(r,c,buttons))
            button.grid(row=row,column=col)
            buttons[row][col]=button


def on_button_click(row,col,buttons):
    global current_player
    button = buttons[row][col]
    if button['text'] == "":
        button['text'] = current_player
        if check_winner(buttons):
            messagebox.showinfo("Tik_Tac Winner!", f"{current_player}")
            reset_game(buttons)
        elif check_draw(buttons):
            messagebox.showinfo("Draw!")
            reset_game(buttons)
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
def check_winner(buttons):
    if buttons:
        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] ==buttons[row][2]['text'] != '':
                return True
        for col in range(3):
            if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != '':
                return True
        if buttons[0][0]['text'] == buttons[1][1]['text'] ==buttons[2][2]['text'] !='':
            return True
        if buttons[0][2]['text'] == buttons[1][1]['text'] ==buttons[2][0]['text'] !='':
            return True
    return False

def check_draw(buttons):
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == '':
                return False
    return True

def reset_game(buttons):
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''
    current_player = "X"


if __name__ == "__main__":
    main()

