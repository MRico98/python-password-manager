import tkinter as tk
from tkinter import ttk

class AddPasswordWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Save New Password")
        self.geometry("400x300")

        
        self._setup_ui()

    def _setup_ui(self) -> None:
        save_password_frame = ttk.Frame(self, padding="30")
        save_password_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        save_password_frame.columnconfigure(0, weight=1)

        self.username_entry = ttk.Entry(save_password_frame)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)