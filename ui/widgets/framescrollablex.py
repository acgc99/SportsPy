"""
Source
https://blog.teclado.com/tkinter-scrollable-frames/
Consulted on 2023-01-08
"""


import tkinter as tk
from tkinter import ttk


class FrameScrollableX(tk.Frame):
    
    
    def __init__(self, root, *args, **kwargs):
        
        super().__init__(root, *args, **kwargs)
        
        canvas = tk.Canvas(self)
        scrollbarx = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        
        self.frame = tk.Frame(canvas)
        self.frame.bind("<Configure>", lambda x: canvas.configure(
            scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=self.frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbarx.set)
        canvas.grid(row=0, column=0, sticky="news")
        scrollbarx.grid(row=1, column=0, sticky="ew")