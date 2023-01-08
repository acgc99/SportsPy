import tkinter as tk
from tkinter import ttk

from .widgets import Page
from .pageselectsport import PageSelectSport


class PageSelectUser(Page):
    
    
    def __init__(self, root, previousPage, rootLabel="SportsPy > Select User"):
        # Set up
        super().__init__(root, previousPage, rootLabel, highlightbackground="blue", highlightthickness=5, padx=50, pady=50)
        # Dependent pages
        self.pages["PageSelectSport"] = PageSelectSport(self.root, self)
        # Title label
        self.labels["title"] = ttk.Label(self, text="Select a user from the list (drop down menu)")
        self.labels["title"].grid(row=0, column=0, pady=(0,10))
        # Select user button
        self.buttons["select"] = ttk.Button(self, text="Select User")
        self.buttons["select"].grid(row=1, column=0, sticky="WE")
        self.fbuttons["select"] = lambda: root.change_page(self, self.pages["PageSelectSport"])
        self.set_button_command("select")
        # Back button
        self.buttons["back"] = ttk.Button(self, text="Back")
        self.buttons["back"].grid(row=2, column=0, sticky="WE")
        self.fbuttons["back"] = command=lambda:root.change_page(self, self.previousPage)
        self.set_button_command("back")