import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    player_choice = user_choice.get()
    computer_choice = get_computer_choice()

    result = check_winner(player_choice, computer_choice)

    messagebox.showinfo("Result", f"Player: {player_choice}\nComputer: {computer_choice}\n\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create a label
label = tk.Label(window, text="Choose Rock, Paper, or Scissors:")
label.pack()

# Create a dropdown menu
choices = ["Rock", "Paper", "Scissors"]
user_choice = tk.StringVar(window)
user_choice.set(choices[0])
dropdown = tk.OptionMenu(window, user_choice, *choices)
dropdown.pack()

# Create a button to play
play_button = tk.Button(window, text="Play", command=play)
play_button.pack()

# Run the Tkinter event loop
window.mainloop()
