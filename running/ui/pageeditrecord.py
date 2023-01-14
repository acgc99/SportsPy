import tkinter as tk
from tkinter import ttk, messagebox
import datetime

from running import SessionRunning, DatabaseManagerRunning
from .pageaddrecord import PageAddRecord


class PageEditRecord(PageAddRecord):
    
    
    def __init__(self, root, previousPage, rootLabel="SportsPy > Select User > Running > Manage >  Edit Record"):
        # Set up
        super().__init__(root, previousPage, rootLabel)
        
        self.fbuttons["save"] = lambda: self._command_save()
        self.set_button_command("save")
        self.idsession = None
    
    
    def setall(self, idsession, runningSession):
        
        date = runningSession.date_dict()
        
        self.year.set(date["year"])
        self.month.set(date["month"])
        self.day.set(date["day"])
        self.distance.set(runningSession.distance)
        self.time.set(runningSession.time)
        self.kcal.set(runningSession.kcal)
        self.idsession = idsession
    
    
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
        dbm.update(self.idsession, self.year.get(), self.month.get(),
            self.day.get(), self.distance.get(), self.time.get(),
            self.kcal.get())
        dbm.disconnect()
        self._command_clear()
        self.previousPage.frames["data"].destroy()
        self.previousPage._initialize()
        self.root.change_page(self, self.previousPage)
    
    
    def _command_back(self):
        
        aux = 0
        for entry in self.entries.values():
            aux += len(entry.get())
        if aux == 0:
            msg = "No changes will be applied"
            ok = messagebox.askyesno(message=msg, title="Warning")
        else: ok = True
        if not ok: return
        # self._command_clear()
        self.root.change_page(self, self.previousPage)