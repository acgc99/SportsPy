import tkinter as tk
from tkinter import ttk


class PageAddRecord(tk.Frame):
    
    
    def __init__(self, root, previousPage):
        # Set up
        super().__init__(root, highlightbackground="pink",
            highlightthickness=5, padx=50, pady=50)
        self.labelInfoText = "SportsPy > Select User > Running > Add Record"
        # Dependent pages
        self.pages = {}
        # Title label
        labelTitle = ttk.Label(self, text="Add Record")
        labelTitle.grid(row=0, column=0, pady=(0,10))
        
        # Insert values frame
        frameInsert = tk.Frame(self, highlightbackground="black", highlightthickness=1)
        frameInsert.grid(row=1, column=0)
        # Date frame
        frameDate = tk.Frame(frameInsert, highlightbackground="black", highlightthickness=1)
        frameDate.grid(row=0, column=0)
        # Date labels
        labelDate = ttk.Label(frameDate, text="Date")
        labelDate.grid(row=0, column=1)
        labelYear = ttk.Label(frameDate, text="Year")
        labelYear.grid(row=1, column=0)
        labelMonth = ttk.Label(frameDate, text="Month")
        labelMonth.grid(row=1, column=1)
        labelDay = ttk.Label(frameDate, text="Day")
        labelDay.grid(row=1, column=2)
        # Date entries
        entryYear = ttk.Entry(frameDate)
        entryYear.grid(row=2, column=0)
        entryMonth = ttk.Entry(frameDate)
        entryMonth.grid(row=2, column=1)
        entryDay = ttk.Entry(frameDate)
        entryDay.grid(row=2, column=2)
        # Date buttons
        buttonYear = ttk.Button(frameDate, text="This Year")
        buttonYear.grid(row=3, column=0, sticky="WE")
        buttonMonth = ttk.Button(frameDate, text="This Month")
        buttonMonth.grid(row=3, column=1, sticky="WE")
        buttonDay = ttk.Button(frameDate, text="This Day")
        buttonDay.grid(row=3, column=2, sticky="WE")
        buttonToday = ttk.Button(frameDate, text="Today")
        buttonToday.grid(row=4, column=0, columnspan=3, sticky="WE")
        # Distance frame
        frameDistance = tk.Frame(frameInsert, highlightbackground="black", highlightthickness=1)
        frameDistance.grid(row=0, column=1)
        # Distance label
        labelDistance = ttk.Label(frameDistance, text="Distance (km)")
        labelDistance.grid(row=0, column=0)
        # Distance entry
        entryDistance = ttk.Entry(frameDistance)
        entryDistance.grid(row=1, column=0)
        # Time frame
        frameTime = tk.Frame(frameInsert, highlightbackground="black", highlightthickness=1)
        frameTime.grid(row=0, column=2)
        # Time label
        labelTime = ttk.Label(frameTime, text="Time (min)")
        labelTime.grid(row=0, column=0)
        # Time entry
        entryTime = ttk.Entry(frameTime)
        entryTime.grid(row=1, column=0)
        # Kcal frame
        frameKcal = tk.Frame(frameInsert, highlightbackground="black", highlightthickness=1)
        frameKcal.grid(row=0, column=3)
        # Kcal label
        labelKcal = ttk.Label(frameKcal, text="Energy (kcal)")
        labelKcal.grid(row=0, column=0)
        # Kcal entry
        entryKcal = ttk.Entry(frameKcal)
        entryKcal.grid(row=1, column=0)
        
        # Control frame
        frameControl = tk.Frame(self, highlightbackground="black", highlightthickness=1)
        frameControl.grid(row=2, column=0, sticky="WE")
        # Save button
        buttonSave = ttk.Button(frameControl, text="Save")
        buttonSave.grid(row=0, column=2)
        # Clear button
        buttonClear = ttk.Button(frameControl, text="Clear")
        buttonClear.grid(row=0, column=1)
        # Back button
        buttonBack = ttk.Button(frameControl, text="Back",
            command=lambda:root.change_page(self, previousPage))
        buttonBack.grid(row=0, column=0)