import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        # Calculate the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set the window size and position it in the center
        window_width = 500
        window_height = 400
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Set a colorful background
        self.root.configure(bg="#40E0D0")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self.root, text="Choose rock, paper, or scissors:")
        self.instruction_label.pack(pady=10, padx=20)

        self.choices = ["rock", "paper", "scissors"]

        for choice in self.choices:
            button = tk.Button(self.root, text=choice.capitalize(), command=lambda c=choice: self.play(c))
            button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Your Score: 0 | Computer's Score: 0", bg="#E0FFFF")
        self.score_label.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"Result: {result}")
        self.update_scores()
        self.display_result(user_choice, computer_choice)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def update_scores(self):
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer's Score: {self.computer_score}")

    def display_result(self, user_choice, computer_choice):
        messagebox.showinfo("Game Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {self.result_label['text']}")
        self.reset_game()

    def reset_game(self):
        self.result_label.config(text="")
        if not messagebox.askyesno("Play Again", " Ok Let's play again?"):
            self.root.destroy()
        else:
            self.update_scores()

def main():
    root = tk.Tk()
    app = RockPaperScissorsGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
