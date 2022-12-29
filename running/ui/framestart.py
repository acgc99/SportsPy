import tkinter as tk
from tkinter import ttk
import sys


class FrameStart(tk.Frame):
    
    
    def __init__(self, root):
        # Set up
        super().__init__(root, highlightbackground="black",
            highlightthickness=5, padx=50, pady=50)
        self.grid(row=0, column=0)
        # Title label
        labelTitle = ttk.Label(self, text="SportsPy")
        labelTitle.grid(row=0, column=0)
        # Start button
        buttonStart = ttk.Button(self, text="Start",
            command= lambda: print("Start button pressed"))
        buttonStart.grid(row=1, column=0, pady=(10,0))
        # Exit button
        buttonExit = ttk.Button(self, text="Exit", command=lambda:sys.exit())
        buttonExit.grid(row=2, column=0, pady=(10,0))