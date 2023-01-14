import tkinter as tk
from tkinter import ttk, messagebox

from ui.widgets import Page, FrameScrollableXY
from running import DatabaseManagerRunning
from .pageeditrecord import PageEditRecord


class PageManage(Page):
    
    
    def __init__(self, root, previousPage, rootLabel="SportsPy > Select User > Running > Manage"):
        # Set up
        super().__init__(root, previousPage, rootLabel, highlightbackground="pink", highlightthickness=5, padx=50, pady=50)
        # Dependent pages
        self.pages["PageEditRecord"] = PageEditRecord(root, self)
        # Back button
        self.buttons["back"] = ttk.Button(self, text="Back")
        self.buttons["back"].grid(row=8, column=0, columnspan=10, sticky="WE")
        self.fbuttons["back"] = lambda: self._command_back()
        self.set_button_command("back")
    
    
    def on_shown(self):
        self._initialize()
    
    
    def _initialize(self):
            
            self.frames["data"] = FrameScrollableXY(self, highlightbackground="black", highlightthickness=1)#tk.Frame(self, highlightbackground="black", highlightthickness=1)
            self.frames["data"].grid(row=0, column=0)
            
            self.labels["data_year"] = ttk.Label(self.frames["data"].frame, text="Year")
            self.labels["data_year"].grid(row=0, column=0)
            
            self.labels["data_month"] = ttk.Label(self.frames["data"].frame, text="Month")
            self.labels["data_month"].grid(row=0, column=1)
            
            self.labels["data_day"] = ttk.Label(self.frames["data"].frame, text="Day")
            self.labels["data_day"].grid(row=0, column=2)
            
            self.labels["data_distance"] = ttk.Label(self.frames["data"].frame, text="Distance")
            self.labels["data_distance"].grid(row=0, column=3)
            
            self.labels["data_time"] = ttk.Label(self.frames["data"].frame, text="Time")
            self.labels["data_time"].grid(row=0, column=4)
            
            self.labels["data_kcal"] = ttk.Label(self.frames["data"].frame, text="Kcal")
            self.labels["data_kcal"].grid(row=0, column=5)
            
            self.labels["data_idsession"] = ttk.Label(self.frames["data"].frame, text="Session id")
            self.labels["data_idsession"].grid(row=0, column=6)
            
            self.labels["data_actions"] = ttk.Label(self.frames["data"].frame, text="Actions")
            self.labels["data_actions"].grid(row=0, column=7, columnspan=2)
            
            self.dbm = DatabaseManagerRunning("database.db")
            nrows = self.dbm.nrows()
            self.dbm.c.execute("SELECT * FROM record ORDER BY date ASC")
            for i in range(nrows):
                idsession, runningSession = self.dbm.c.fetchone()
                self._initialize_dataframe(i+1, runningSession, idsession)
            self.dbm.disconnect()
    
    
    def _initialize_dataframe(self, i, runningSession, idsession):
        
        date = runningSession.date_dict()
        
        self.entries["data_year"] = ttk.Entry(self.frames["data"].frame)
        self.entries["data_year"].grid(row=i, column=0)
        self.entries["data_year"].insert(0, date["year"])
        self.entries["data_year"].config(state="disabled")
        
        self.entries["data_month"] = ttk.Entry(self.frames["data"].frame)
        self.entries["data_month"].grid(row=i, column=1)
        self.entries["data_month"].insert(0, date["month"])
        self.entries["data_month"].config(state="disabled")
        
        self.entries["data_day"] = ttk.Entry(self.frames["data"].frame)
        self.entries["data_day"].grid(row=i, column=2)
        self.entries["data_day"].insert(0, date["day"])
        self.entries["data_day"].config(state="disabled")
        
        self.entries["data_distance"] = ttk.Entry(self.frames["data"].frame)
        self.entries["data_distance"].grid(row=i, column=3)
        self.entries["data_distance"].insert(0, runningSession.distance)
        self.entries["data_distance"].config(state="disabled")
        
        self.entries["data_time".format(idsession)] = ttk.Entry(self.frames["data"].frame)
        self.entries["data_time"].grid(row=i, column=4)
        self.entries["data_time"].insert(0, runningSession.time)
        self.entries["data_time"].config(state="disabled")
        
        self.entries["data_kcal"] = ttk.Entry(self.frames["data"].frame)
        self.entries["data_kcal"].grid(row=i, column=5)
        self.entries["data_kcal"].insert(0, runningSession.kcal)
        self.entries["data_kcal"].config(state="disabled")
        
        self.entries["data_idsession"] = ttk.Entry(self.frames["data"].frame)
        self.entries["data_idsession"].grid(row=i, column=6)
        self.entries["data_idsession"].insert(0, idsession)
        self.entries["data_idsession"].config(state="disabled")
        
        self.buttons["data_edit"] = ttk.Button(self.frames["data"].frame, text="Edit")
        self.buttons["data_edit"].grid(row=i, column=7)
        self.fbuttons["data_edit"] = lambda: self._command_edit(runningSession, idsession)
        self.set_button_command("data_edit")
        
        self.buttons["data_delete"] = ttk.Button(self.frames["data"].frame, text="Delete")
        self.buttons["data_delete"].grid(row=i, column=8)
        self.fbuttons["data_delete"] = lambda: self._command_delete(idsession)
        self.set_button_command("data_delete")
    
    
    def _command_edit(self, runningSession, idsession):
        
        self.root.change_page(self, self.pages["PageEditRecord"])
        self.pages["PageEditRecord"].setall(idsession, runningSession)
    
    
    def _command_delete(self, idsession):
        
        msg = "The entry with 'idsession = {}' will be deleted".format(idsession)
        ok = messagebox.askyesno(message=msg, title="Warning")
        if not ok: return
        
        dbm = DatabaseManagerRunning("database.db")
        dbm.delete(idsession)
        dbm.disconnect()
        self.frames["data"].destroy()
        self._initialize()
    
    
    def _command_back(self):
        self.frames["data"].destroy()
        self.root.change_page(self, self.previousPage)