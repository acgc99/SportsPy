import tkinter as tk
from tkinter import ttk

from .pageselectsport import PageSelectSport


class PageSelectUser(tk.Frame):
    
    
    def __init__(self, root, previousPage):
        # Set up
        super().__init__(root, highlightbackground="blue",
            highlightthickness=5, padx=50, pady=50)
        self.labelInfoText = "SportsPy > Select User"
        # Dependent pages
        self.pages = {
            "PageSelectSport": PageSelectSport(root, self)
            }
        # Title label
        labelTitle = ttk.Label(self, text="Select a user from the list (drop down menu)")
        labelTitle.grid(row=0, column=0, pady=(0,10))
        # Select user button
        buttonSelectUser = ttk.Button(self, text="Select User",
            command=lambda: root.change_page(self, self.pages["PageSelectSport"]))
        buttonSelectUser.grid(row=1, column=0, sticky="WE")
        # Back button
        buttonBack = ttk.Button(self, text="Back",
            command=lambda:root.change_page(self, previousPage))
        buttonBack.grid(row=2, column=0, sticky="WE")