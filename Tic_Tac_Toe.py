import tkinter as tk
from tkinter import messagebox
import copy

board = [""] * 9

win_combos = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  
    (0, 4, 8), (2, 4, 6)              
]

def check_winner(b):
    for x, y, z in win_combos:
        if b[x] == b[y] == b[z] and b[x] != "":
            return b[x]
    if "" not in b:
        return "Tie"
    return None

def minimax(b, is_maximizing):
    winner = check_winner(b)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif winner == "Tie":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if b[i] == "":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if b[i] == "":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = ""
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = "O"
        buttons[move].config(text="O", state="disabled")
        check_game()

def player_move(i):
    if board[i] == "":
        board[i] = "X"
        buttons[i].config(text="X", state="disabled")
        check_game()
        ai_move()

def check_game():
    winner = check_winner(board)
    if winner:
        messagebox.showinfo("Game Over", f"{winner} wins!" if winner != "Tie" else "It's a tie!")
        reset_game()

def reset_game():
    global board
    board = [""] * 9
    for btn in buttons:
        btn.config(text="", state="normal")

root = tk.Tk()
root.title("Tic-Tac-Toe AI")

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: player_move(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
