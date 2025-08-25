import tkinter as tk
from tkinter import ttk
from typing import Optional, Callable

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Contraseñas")
        self.geometry("400x300")

        self.on_add_password: Optional[Callable] = None
        self.on_view_password: Optional[Callable] = None

        self._setup_ui()

    def _setup_ui(self) -> None:
        main_frame = ttk.Frame(self, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Button(
            main_frame,
            text="Close",
            command=self.quit
        ).grid(row=3, column=0, pady=(30,0))