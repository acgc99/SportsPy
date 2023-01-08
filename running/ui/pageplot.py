import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from ui.widgets import Page
from running import DatabaseManagerRunning, DatabaseManagerRunningPlotter


class PagePlot(Page):
    """
    matplotlib on tkinter
    https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html
    personalize toolbar
    https://stackoverflow.com/questions/59606641/how-do-i-configure-a-matplotlib-toolbar-so-that-the-buttons-in-the-toolbars-are
    """
    
    def __init__(self, root, previousPage, rootLabel="SportsPy > Select User > Running > Plot"):
        # Set up
        super().__init__(root, previousPage, rootLabel, highlightbackground="pink", highlightthickness=5, padx=50, pady=50)
        # Title label
        self.labels["title"] = ttk.Label(self, text="Plot Data")
        self.labels["title"].grid(row=0, column=0, pady=(0,10), columnspan=3)
        
        self.frames["select"] = tk.Frame(self, highlightbackground="gray", highlightthickness=1)
        self.frames["select"].grid(row=1, column=0, rowspan=2)
        
        self.labels["select_select"] = ttk.Label(self.frames["select"], text="Select")
        self.labels["select_select"].grid(row=0, column=0)
        
        self.what = tk.IntVar()
        self.radiobuttons["select_plotAll"] = tk.Radiobutton(self.frames["select"], text="All", variable=self.what, value=1)
        self.radiobuttons["select_plotAll"].grid(row=1, column=0)
        self.fradiobuttons["select_plotAll"] = lambda: self._command_plot()
        self.set_radiobutton_command("select_plotAll")
        self.radiobuttons["select_plotVel"] = tk.Radiobutton(self.frames["select"], text="Vel", variable=self.what, value=2)
        self.radiobuttons["select_plotVel"].grid(row=1, column=1)
        self.fradiobuttons["select_plotVel"] = lambda: self._command_plot()
        self.set_radiobutton_command("select_plotVel")
        self.radiobuttons["select_plotDens"] = tk.Radiobutton(self.frames["select"], text="Dens", variable=self.what, value=3)
        self.radiobuttons["select_plotDens"].grid(row=1, column=2)
        self.fradiobuttons["select_plotDens"] = lambda: self._command_plot()
        self.set_radiobutton_command("select_plotDens")
        
        self.separators["select"] = ttk.Separator(self, orient="vertical")
        self.separators["select"].grid(row=1, column=1, sticky="NS", rowspan=2, padx=(10, 10))
        
        # Figure
        self.dbmp = DatabaseManagerRunningPlotter(DatabaseManagerRunning("database.db"))
        self.canvas = FigureCanvasTkAgg(self.dbmp.fig, master=self)
        self.canvas.draw()
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()
        self.canvas.get_tk_widget().grid(row=1, column=2)
        self.toolbar.grid(row=2, column=2)
        
        # Back button
        self.buttons["back"] = ttk.Button(self, text="Back")
        self.buttons["back"].grid(row=3, column=0, sticky="WE", columnspan=4, pady=(10,0))
        self.fbuttons["back"] = lambda: self._command_back()
        self.set_button_command("back")
    
    
    def _command_plot(self):
        
        self.dbmp.fig.clear()
        if self.what.get() == 1:
            self.dbmp.plotall()
        else:
            self.dbmp.plot(self.what.get())
        self.canvas.draw()
    
    
    def _command_back(self):
        
        self.dbmp.fig.clear()
        self.canvas.draw()
        self.what.set(0)
        self.root.change_page(self, self.previousPage)