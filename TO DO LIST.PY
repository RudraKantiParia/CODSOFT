import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Calculate the position to center the window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = (screen_width - 500) // 2
        y_position = (screen_height - 400) // 2

        # Set the initial size and position of the window
        self.root.geometry(f"500x400+{x_position}+{y_position}")

        self.tasks = []

        # Create and set up the listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, bg='#E6E6FA')  # Light purple background
        self.task_listbox.pack(pady=10)

        # Create and set up entry widget
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=5)

        # Create buttons with colorful appearance
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg='#98FB98')  # Light green background
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg='#FF6347')  # Tomato color
        self.delete_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=self.root.destroy, bg='#FFD700')  # Gold color
        self.exit_button.pack(pady=5)

        # Load tasks from file
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Clear the entry widget
            self.save_tasks()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = int(selected_task_index[0])
            del self.tasks[selected_task_index]
            self.task_listbox.delete(selected_task_index)
            self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass  # If the file doesn't exist yet, it's fine.

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
