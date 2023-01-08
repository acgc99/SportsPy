import tkinter as tk
from tkinter import ttk

from ui import Page
from .pageaddrecord import PageAddRecord
from .pageplot import PagePlot
from .pagemanage import PageManage


class PageRunning(Page):
    
    
    def __init__(self, root, previousPage, rootLabel="SportsPy > Select User > Running"):
        # Set up
        super().__init__(root, previousPage, rootLabel, highlightbackground="pink", highlightthickness=5, padx=50, pady=50)
        # Dependent pages
        self.pages["PageAddRecord"] = PageAddRecord(root, self)
        self.pages["PageManage"] = PageManage(root, self)
        self.pages["PagePlot"] = PagePlot(root, self)
        # Title label
        self.labels["title"] = ttk.Label(self, text="Running")
        self.labels["title"].grid(row=0, column=0, pady=(0,10))
        # Add record button
        self.buttons["add"] = ttk.Button(self, text="Add Record")
        self.buttons["add"].grid(row=1, column=0, sticky="WE")
        self.fbuttons["add"] = lambda: self.root.change_page(self, self.pages["PageAddRecord"])
        self.set_button_command("add")
        # Add database button
        self.buttons["manage"] = ttk.Button(self, text="Manage Database")
        self.buttons["manage"].grid(row=2, column=0, sticky="WE")
        self.fbuttons["manage"] = lambda: self.root.change_page(self, self.pages["PageManage"])
        self.set_button_command("manage")
        # Visualize button
        self.buttons["plot"] = ttk.Button(self, text="Plot Data")
        self.buttons["plot"].grid(row=3, column=0, sticky="WE")
        self.fbuttons["plot"] = lambda: self.root.change_page(self, self.pages["PagePlot"])
        self.set_button_command("plot")
        # Back button
        self.buttons["back"] = ttk.Button(self, text="Back")
        self.buttons["back"].grid(row=4, column=0, sticky="WE")
        self.fbuttons["back"] = lambda: root.change_page(self, self.previousPage)
        self.set_button_command("back")