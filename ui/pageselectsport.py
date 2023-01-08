import tkinter as tk
from tkinter import ttk

from .widgets import Page
from running.ui import PageRunning


class PageSelectSport(Page):
    
    
    def __init__(self, root, previousPage, rootLabel="SportsPy > Select User > Select Sport"):
        # Set up
        super().__init__(root, previousPage, rootLabel, highlightbackground="red", highlightthickness=5, padx=50, pady=50)
        # Dependent pages
        self.pages["PageRunning"] = PageRunning(self.root, self)
        # Title label
        self.labels["title"] = ttk.Label(self, text="Select a sport from the list (buttons with images)")
        self.labels["title"].grid(row=0, column=0, pady=(0,10))
        # Running button
        self.buttons["running"] =  ttk.Button(self, text="Running")
        self.buttons["running"].grid(row=1, column=0, sticky="WE")
        self.fbuttons["running"] = lambda: self.root.change_page(self, self.pages["PageRunning"])
        self.set_button_command("running")
        # Back button
        self.buttons["back"] = ttk.Button(self, text="Back")
        self.buttons["back"].grid(row=2, column=0, sticky="WE")
        self.fbuttons["back"] = lambda: root.change_page(self, self.previousPage)
        self.set_button_command("back")