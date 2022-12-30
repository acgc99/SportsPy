import tkinter as tk
from tkinter import ttk
import sys

from .pageselectuser import PageSelectUser


class PageStart(tk.Frame):
    
    
    def __init__(self, root):
        # Set up
        super().__init__(root, highlightbackground="black",
            highlightthickness=5, padx=50, pady=50)
        self.labelInfoText = "SportsPy"
        # Dependent pages
        self.pages = {
            "PageSelectUser": PageSelectUser(root, self)
            }
        # Title label
        labelTitle = ttk.Label(self, text="SportsPy")
        labelTitle.grid(row=0, column=0, pady=(0,10))
        # Start button
        buttonSelectUser = ttk.Button(self, text="Select User",
            command= lambda: root.change_page(self, self.pages["PageSelectUser"]))
        buttonSelectUser.grid(row=1, column=0, sticky="WE", ipadx=10)
        # Manage users button
        buttonManageUsers = ttk.Button(self, text="Manage Users")
        buttonManageUsers.grid(row=2, column=0, sticky="WE", ipadx=10)
        # Exit button
        buttonExit = ttk.Button(self, text="Exit", command=lambda:sys.exit())
        buttonExit.grid(row=3, column=0, sticky="WE", ipadx=10)