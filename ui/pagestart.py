import tkinter as tk
from tkinter import ttk
import sys

from .page import Page
from .pageselectuser import PageSelectUser


class PageStart(Page):
    
    """
    self.root, self.previousPage, self.rootLabel defined by inherit from Page
    """
    def __init__(self, root, previousPage=None, rootLabel="SportsPy"):
        # Set up
        super().__init__(root, previousPage, rootLabel, highlightbackground="black", highlightthickness=5, padx=50, pady=50)
        # Dependent pages
        self.pages["PageSelectUser"] = PageSelectUser(self.root, self)
        # Title label
        self.labels["title"] = ttk.Label(self, text="SportsPy")
        self.labels["title"].grid(row=0, column=0, pady=(0,10))
        # Start button
        self.buttons["select"] = ttk.Button(self, text="Select User")
        self.buttons["select"].grid(row=1, column=0, sticky="WE", ipadx=10)
        self.fbuttons["select"] = lambda: self.root.change_page(self, self.pages["PageSelectUser"])
        self.set_button_command("select")
        # Manage users button
        self.buttons["manage"] = ttk.Button(self, text="Manage Users")
        self.buttons["manage"].grid(row=2, column=0, sticky="WE", ipadx=10)
        # Exit button
        self.buttons["exit"] = ttk.Button(self, text="Exit")
        self.buttons["exit"].grid(row=3, column=0, sticky="WE", ipadx=10)
        self.fbuttons["exit"] = lambda: sys.exit()
        self.set_button_command("exit")