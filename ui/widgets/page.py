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
        # Radio buttons
        self.radiobuttons = {}
        # Radio buttons functions
        self.fradiobuttons = {}
        # Entries
        self.entries = {}
        # Separators
        self.separators = {}
    
    
    def set_button_command(self, button):
        self.buttons[button].configure(command=self.fbuttons[button])
    
    
    def set_radiobutton_command(self, button):
        self.radiobuttons[button].configure(command=self.fradiobuttons[button])
    
    
    def on_shown(self, *args, **kwargs):
        """
        This will be executed when the page is gridded/packed from the UI
        """
        pass