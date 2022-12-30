import tkinter as tk
from tkinter import ttk

from running.ui import PageRunning

class PageSelectSport(tk.Frame):
    
    
    def __init__(self, root, previousPage):
        # Set up
        super().__init__(root, highlightbackground="red",
            highlightthickness=5, padx=50, pady=50)
        self.labelInfoText = "SportsPy > Select User > Select Sport"
        # Dependent pages
        self.pages = {
            "PageRunning": PageRunning(root, self)
            }
        # Title label
        labelTitle = ttk.Label(self, text="Select a sport from the list (buttons with images)")
        labelTitle.grid(row=0, column=0, pady=(0,10))
        # Running button
        buttonRunning = ttk.Button(self, text="Running",
            command=lambda:root.change_page(self, self.pages["PageRunning"]))
        buttonRunning.grid(row=1, column=0, sticky="WE")
        # Back button
        buttonBack = ttk.Button(self, text="Back",
            command=lambda:root.change_page(self, previousPage))
        buttonBack.grid(row=2, column=0, sticky="WE")