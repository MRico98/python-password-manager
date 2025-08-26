import tkinter as tk
from tkinter import ttk
from typing import Optional, Callable

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Management")
        self.geometry("400x300")

        self.on_add_password: Optional[Callable] = None
        self.on_view_password: Optional[Callable] = None

        self._setup_ui()

    def _setup_ui(self) -> None:
        main_frame = ttk.Frame(self, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)

        tk.Label(
              main_frame,
              text="Password Manager",
              font=('Arial', 16, 'bold')
          ).grid(row=0, column=0, pady=(0, 30))

        ttk.Button(
              main_frame,
              text="Add new password",
              command=self._handle_add_password
          ).grid(row=1, column=0, pady=10, sticky="ew")

        ttk.Button(
              main_frame,
              text="Watch all passwords",
              command=self._handle_view_passwords
          ).grid(row=2, column=0, pady=10, sticky="ew")

        ttk.Button(
              main_frame,
              text="Close",
              command=self.quit
          ).grid(row=3, column=0, pady=(30, 0))
        
    def _handle_add_password(self) -> None:
        if self.on_add_password:
            self.on_add_password()

    def _handle_view_passwords(self) -> None:
        if self.on_view_passwords:
            self.on_view_passwords()
    
    def set_add_password_handler(self, handler: Callable) -> None:
        self.on_add_password = handler

    def set_view_passwords_handler(self, handler: Callable) -> None:
        self.on_view_password = handler

    def set_view_passwords_handler(self, handler: Callable) -> None:
        self.on_view_passwords = handler

    def run(self) -> None:
        self.mainloop()
