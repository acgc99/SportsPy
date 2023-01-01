import tkinter as tk
from tkinter import ttk

from .page import Page
from .pagestart import PageStart


class UI(tk.Tk):
    
    def __init__(self, start: bool = True):
        # Set up
        super().__init__()
        # Pages
        self.pages = {}
        # Frames
        self.frames = {}
        # Labels
        self.labels = {}
        # Start page
        self.pages["Start"] = PageStart(self)
        self.pages["Start"].grid(row=0, column=0)
        # Info label
        self.frames["label"] = tk.Frame(self, highlightbackground="red", highlightthickness=2)
        self.frames["label"].grid(row=1, column=0, sticky="WE")
        self.labels["label_info"] = ttk.Label(self.frames["label"], text=self.pages["Start"].rootLabel)
        self.labels["label_info"].grid(row=0, column=0, sticky="W")
        
        if start: self.mainloop()
    
    def change_page(self, oldPage, newPage):
        """
        Change the shown page
        """
        oldPage.grid_forget()
        newPage.grid(row=0, column=0)
        self.labels["label_info"].config(text=newPage.rootLabel)