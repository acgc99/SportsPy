import tkinter as tk
from tkinter import ttk

from .pagestart import PageStart


class UI(tk.Tk):
    
    def __init__(self, start: bool = True):
        super().__init__()
        
        pageStart = PageStart(self)
        pageStart.grid(row=0, column=0)
        if start: self.mainloop()
    
    def change_page(self, oldPage, newPage):
        oldPage.grid_forget()
        newPage.grid(row=0, column=0)