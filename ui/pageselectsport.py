import tkinter as tk
from tkinter import ttk


class PageSelectSport(tk.Frame):
    
    
    def __init__(self, root, previousPage):
        # Set up
        super().__init__(root, highlightbackground="red",
            highlightthickness=5, padx=50, pady=50)
        # Label
        labelTitle = ttk.Label(self, text="Select a sport from the list (buttons with images)")
        labelTitle.grid(row=0, column=0, pady=(0,10))
        # Running button
        buttonRunning = ttk.Button(self, text="Running")
        buttonRunning.grid(row=1, column=0)
        # Back button
        buttonPageStart = ttk.Button(self, text="Back",
            command=lambda:root.change_page(self, previousPage))
        buttonPageStart.grid(row=2, column=0)