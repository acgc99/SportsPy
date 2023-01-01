import tkinter as tk


class Page(tk.Frame):
    
    
    def __init__(self, root, previousPage, rootLabel="", *args, **kwargs):
        # Set up
        super().__init__(root, *args, **kwargs)
        self.root = root
        self.rootLabel = rootLabel
        self.previousPage = previousPage
        # Dependent pages
        self.pages = {}
        # Frames
        self.frames = {}
        # Labels
        self.labels = {}
        # Buttons
        self.buttons = {}
        # Buttons functions
        self.fbuttons = {}
        # Entries
        self.entries = {}
    
    
    def set_button_command(self, button):
        self.buttons[button].configure(command=self.fbuttons[button])