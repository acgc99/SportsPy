import tkinter as tk
from tkinter import ttk, messagebox
import datetime

from running import SessionRunning, DatabaseManagerRunning
from ui.widgets import Page


class PageAddRecord(Page):
    
    
    def __init__(self, root, previousPage, rootLabel="SportsPy > Select User > Running > Add Record"):
        # Set up
        super().__init__(root, previousPage, rootLabel, highlightbackground="pink", highlightthickness=5, padx=50, pady=50)
        # Title label
        self.labels["title"] = ttk.Label(self, text="Add Record")
        self.labels["title"].grid(row=0, column=0, columnspan=6)
        # Date label
        self.labels["date"] = ttk.Label(self, text="Date")
        self.labels["date"].grid(row=1, column=0, columnspan=3)
        # Year label
        self.labels["year"] = ttk.Label(self, text="Year")
        self.labels["year"].grid(row=2, column=0)
        # Month label
        self.labels["month"] = ttk.Label(self, text="Month")
        self.labels["month"].grid(row=2, column=1)
        # Day label
        self.labels["day"] = ttk.Label(self, text="Day")
        self.labels["day"].grid(row=2, column=2)
        # Year entry
        self.year = tk.IntVar()
        self.entries["year"] = ttk.Entry(self, textvariable=self.year)
        self.entries["year"].delete(0, "end")
        self.entries["year"].grid(row=3, column=0)
        # Year button
        self.buttons["year"] = ttk.Button(self, text="This Year")
        self.buttons["year"].grid(row=4, column=0, sticky="WE")
        self.fbuttons["year"] = lambda: self._command_year()
        self.set_button_command("year")
        # Month entry
        self.month = tk.IntVar()
        self.entries["month"] = ttk.Entry(self, textvariable=self.month)
        self.entries["month"].delete(0, "end")
        self.entries["month"].grid(row=3, column=1)
        # Month button
        self.buttons["month"] = ttk.Button(self, text="This Month")
        self.buttons["month"].grid(row=4, column=1, sticky="WE")
        self.fbuttons["month"] = lambda: self._command_month()
        self.set_button_command("month")
        # Day entry
        self.day = tk.IntVar()
        self.entries["day"] = ttk.Entry(self, textvariable=self.day)
        self.entries["day"].delete(0, "end")
        self.entries["day"].grid(row=3, column=2)
        # Day button
        self.buttons["day"] = ttk.Button(self, text="This Day")
        self.buttons["day"].grid(row=4, column=2, sticky="WE")
        self.fbuttons["day"] = lambda: self._command_day()
        self.set_button_command("day")
        # Today button
        self.buttons["today"] = ttk.Button(self, text="Today")
        self.buttons["today"].grid(row=5, column=0, columnspan=3, sticky="WE")
        self.fbuttons["today"] = lambda: self._command_today()
        self.set_button_command("today")
        # Distance label
        self.labels["distance"] = ttk.Label(self, text="Distance (km)")
        self.labels["distance"].grid(row=2, column=3)
        # Distance entry
        self.distance = tk.IntVar()
        self.entries["distance"] = ttk.Entry(self, textvariable=self.distance)
        self.entries["distance"].delete(0, "end")
        self.entries["distance"].grid(row=3, column=3)
        # Time label
        self.labels["time"] = ttk.Label(self, text="Time (min)")
        self.labels["time"].grid(row=2, column=4)
        # Time entry
        self.time = tk.IntVar()
        self.entries["time"] = ttk.Entry(self, textvariable=self.time)
        self.entries["time"].delete(0, "end")
        self.entries["time"].grid(row=3, column=4)
        # Kcal label
        self.labels["kcal"] = ttk.Label(self, text="Energy (kcal)")
        self.labels["kcal"].grid(row=2, column=5)
        # Kcal entry
        self.kcal = tk.IntVar()
        self.entries["kcal"] = ttk.Entry(self, textvariable=self.kcal)
        self.entries["kcal"].delete(0, "end")
        self.entries["kcal"].grid(row=3, column=5)
        # Save button
        self.buttons["save"] = ttk.Button(self, text="Save")
        self.buttons["save"].grid(row=5, column=5, sticky="WE")
        self.fbuttons["save"] = lambda: self._command_save()
        self.set_button_command("save")
        # Clear button
        self.buttons["clear"] = ttk.Button(self, text="Clear")
        self.buttons["clear"].grid(row=5, column=4, sticky="WE")
        self.fbuttons["clear"] = lambda: self._command_clear()
        self.set_button_command("clear")
        # Back button
        self.buttons["back"] = ttk.Button(self, text="Back")
        self.buttons["back"].grid(row=6, column=5, sticky="WE")
        self.fbuttons["back"] = lambda: self._command_back()
        self.set_button_command("back")
    
    
    def _command_year(self):
        
        year, month, day = map(int, datetime.date.today().isoformat().split("-"))
        self.year.set(year)
    
    
    def _command_month(self):
        
        year, month, day = map(int, datetime.date.today().isoformat().split("-"))
        self.month.set(month)
    
    
    def _command_day(self):
        
        year, month, day = map(int, datetime.date.today().isoformat().split("-"))
        self.day.set(day)
    
    
    def _command_today(self):
        
        year, month, day = map(int, datetime.date.today().isoformat().split("-"))
        self.year.set(year)
        self.month.set(month)
        self.day.set(day)
    
    
    def _command_clear(self):
        self.entries["year"].delete(0, "end")
        self.entries["month"].delete(0, "end")
        self.entries["day"].delete(0, "end")
        self.entries["distance"].delete(0, "end")
        self.entries["time"].delete(0, "end")
        self.entries["kcal"].delete(0, "end")
    
    
    def _command_save(self):
        # Check if data is valid
        try:
            year = int(self.year.get())
            if year <= 0: raise tk.TclError()
        except tk.TclError:
            msg = "The field 'year' must be a positive integer number"
            messagebox.showerror(message=msg, title="Error")
            return
        try:
            month = int(self.month.get())
            if month <= 0: raise tk.TclError()
        except tk.TclError:
            msg = "The field 'month' must be a positive integer number"
            messagebox.showerror(message=msg, title="Error")
            return
        try:
            day = int(self.day.get())
            if day <= 0: raise tk.TclError()
        except tk.TclError:
            msg = "The field 'day' must be a positive integer number"
            messagebox.showerror(message=msg, title="Error")
            return
        try:
            year = int(self.year.get())
            month = int(self.month.get())
            day = int(self.day.get())
            date = datetime.date(year, month, day)
        except ValueError:
            msg = "The date is not valid"
            messagebox.showerror(message=msg, title="Error")
            return
        try:
            distance = int(self.distance.get())
            if distance <= 0: raise tk.TclError()
        except tk.TclError:
            msg = "The field 'distance' must be a positive number"
            messagebox.showerror(message=msg, title="Error")
            return
        try:
            time = int(self.time.get())
            if time <= 0: raise tk.TclError()
        except tk.TclError:
            msg = "The field 'time' must be a positive number"
            messagebox.showerror(message=msg, title="Error")
            return
        try:
            kcal = int(self.kcal.get())
            if time <= 0: raise tk.TclError()
        except tk.TclError:
            msg = "The field 'kcal' must be a positive number"
            messagebox.showerror(message=msg, title="Error")
            return
        sessionRunning = SessionRunning(self.year.get(), self.month.get(),
            self.day.get(), self.distance.get(), self.time.get(),
            self.kcal.get())
        # Save
        dbm = DatabaseManagerRunning("database.db")
        dbm.insert(sessionRunning)
        dbm.disconnect()
        self._command_clear()
    
    
    def _command_back(self):
        
        aux = 0
        for entry in self.entries.values():
            aux += len(entry.get())
        if aux != 0:
            msg = "Unsaved data will be lost if you go back"
            ok = messagebox.askyesno(message=msg, title="Warning")
        else: ok = True
        if not ok: return
        self._command_clear()
        self.root.change_page(self, self.previousPage)