import tkinter as tk
from tkinter import ttk

from .pageaddrecord import PageAddRecord


class PageRunning(tk.Frame):
    
    
    def __init__(self, root, previousPage):
        # Set up
        super().__init__(root, highlightbackground="pink",
            highlightthickness=5, padx=50, pady=50)
        self.labelInfoText = "SportsPy > Select User > Running"
        # Dependent pages
        self.pages = {
            "PageAddRecord": PageAddRecord(root, self)
            }
        # Title label
        labelTitle = ttk.Label(self, text="Running")
        labelTitle.grid(row=0, column=0, pady=(0,10))
        # Add record button
        buttonAddRecord = ttk.Button(self, text="Add Record",
            command = lambda: root.change_page(self, self.pages["PageAddRecord"])
            )
        buttonAddRecord.grid(row=1, column=0, sticky="WE")
        # Add database button
        buttonEditDatabase = ttk.Button(self, text="Edit Database")
        buttonEditDatabase.grid(row=2, column=0, sticky="WE")
        # Visualize button
        buttonVisualize = ttk.Button(self, text="Visualize Data")
        buttonVisualize.grid(row=3, column=0, sticky="WE")
        # Back button
        buttonBack = ttk.Button(self, text="Back",
            command=lambda:root.change_page(self, previousPage))
        buttonBack.grid(row=4, column=0, sticky="WE")