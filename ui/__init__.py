import tkinter as tk
from tkinter import ttk

from .pagestart import PageStart


class UI(tk.Tk):
    
    def __init__(self, start: bool = True):
        super().__init__()
        
        labelInfoFrame = tk.Frame(self, highlightbackground="red",
            highlightthickness=2)
        labelInfoFrame.grid(row=1, column=0, sticky="WE")
        self.labelInfoText = "SportsPy"
        self.labelInfo = ttk.Label(labelInfoFrame, text=self.labelInfoText)
        self.labelInfo.grid(row=0, column=0, sticky="W")
        
        pageStart = PageStart(self)
        pageStart.grid(row=0, column=0)
        
        if start: self.mainloop()
    
    def change_page(self, oldPage, newPage):
        oldPage.grid_forget()
        newPage.grid(row=0, column=0)
        self.labelInfo.config(text=newPage.labelInfoText)