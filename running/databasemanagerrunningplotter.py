import collections

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from numpy import linspace

from .sessionrunning import SessionRunning
from .databasemanagerrunning import DatabaseManagerRunning


class DatabaseManagerRunningPlotter:
    
    
    def __init__(self, dbm: DatabaseManagerRunning):
        self.dbm = dbm
        self.fig = Figure()
        # Plotting style
        self.STYLE = "bmh"
        self.LABELVEL = "v (km/h)"
        self.LABELDENS = "d (kcal/km)"
        self.STYLEVEL = "b-"
        self.STYLEDENS = "r-"
        self.LIMVEL0, self.LIMVEL1 = 0, 20
        self.LIMDENS0, self.LIMDENS1 = 0, 100
        self.YTICKSNUM = 5
    
    
    def plotall(self, **kwargs):
        """
        Plots 'vel' and 'dens' in the same plot
        kwargs used to specify the time interval
        year0, month0, day0, year1, month1, day1
        """
        # Initialize the plot
        plt.style.use(self.STYLE)
        ax_vel = plt.subplot2grid((1, 1), (0, 0), 1, 1, self.fig)
        ax_vel.set_xlabel("Date", loc = "right")
        ax_vel.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y"))
        ax_vel.set_ylabel(self.LABELVEL, loc = "top")
        ax_vel.set_ylim(self.LIMVEL0, self.LIMVEL1)
        ax_vel.set_yticks(linspace(self.LIMVEL0, self.LIMVEL1, self.YTICKSNUM))
        ax_dens = ax_vel.twinx()
        ax_dens.set_ylabel(self.LABELDENS, loc="top")
        ax_dens.set_ylim(self.LIMDENS0, self.LIMDENS1)
        ax_dens.set_yticks(linspace(self.LIMDENS0, self.LIMDENS1, self.YTICKSNUM))
        # Format x axis labels
        for label in ax_vel.get_xticklabels(which = "major"):
            label.set(rotation=30, horizontalalignment = "right")
        # If date limits are provided, use them
        if kwargs == {}: data = self.dbm.selectall()
        else:
            year0, month0, day0 = kwargs["year0"], kwargs["month0"], kwargs["day0"]
            year1, month1, day1 = kwargs["year1"], kwargs["month1"], kwargs["day1"]
            data = self.dbm.selectmulti(year0, month0, day0, year1, month1, day1)
        # Get the data and plot
        dates = collections.deque()
        vels = collections.deque()
        dens = collections.deque()
        for i in data:
            dates.append(i.datetime_date())
            vels.append(i.vel())
            dens.append(i.dens())
        plot_vel, = ax_vel.plot(dates, vels, self.STYLEVEL)
        plot_dens, = ax_dens.plot(dates, dens, self.STYLEDENS)
        ax_vel.yaxis.label.set_color(plot_vel.get_color())
        ax_vel.tick_params(axis="y", colors=plot_vel.get_color())
        ax_dens.yaxis.label.set_color(plot_dens.get_color())
        ax_dens.tick_params(axis="y", colors=plot_dens.get_color())
    
    
    def plot(self, what, **kwargs):
        """
        Plots the given 'what' = 'vel', 'dens'
        kwargs used to specify the time interval
        year0, month0, day0, year1, month1, day1
        """
        if what == 2: what = "vel"
        elif what == 3: what = "dens"
        else: raise Exception("databasemanagerrunning.plot_over error")
        
        if what == "vel":
            xlabel = self.LABELVEL
            styleline = self.STYLEVEL
            lim0, lim1 = self.LIMVEL0, self.LIMVEL1
        elif what == "dens":
            xlabel = self.LABELDENS
            styleline = self.STYLEDENS
            lim0, lim1 = self.LIMDENS0, self.LIMDENS1
        else:
            msg = ("DataBaseManagerRunningPlotter.plot only accepts 'vel' "
                "and 'dens' to plot")
            raise Exception(msg)
        # Initialize the plot
        plt.style.use(self.STYLE)
        ax = plt.subplot2grid((1, 1), (0, 0), 1, 1, self.fig)
        ax.set_xlabel("Date", loc = "right")
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y"))
        ax.set_ylabel(xlabel, loc = "top")
        ax.set_ylim(lim0, lim1)
        ax.set_yticks(linspace(lim0, lim1, self.YTICKSNUM))
        # Format x axis labels
        for label in ax.get_xticklabels(which = "major"):
            label.set(rotation=30, horizontalalignment = "right")
        # If date limits are provided, use them
        if kwargs == {}: data = self.dbm.selectall()
        else:
            year0, month0, day0 = kwargs["year0"], kwargs["month0"], kwargs["day0"]
            year1, month1, day1 = kwargs["year1"], kwargs["month1"], kwargs["day1"]
            data = self.dbm.selectmulti(year0, month0, day0, year1, month1, day1)
        # Get the data and plot
        dates = collections.deque()
        values = collections.deque()
        for i in data:
            dates.append(i.datetime_date())
            values.append(getattr(i, what)())
        plot, = ax.plot(dates, values, styleline)
        ax.yaxis.label.set_color(plot.get_color())
        ax.tick_params(axis="y", colors=plot.get_color())
    
    
    def plotall_show(self, **kwargs):
        """
        Plots 'vel' and 'dens' in the same plot
        kwargs used to specify the time interval
        year0, month0, day0, year1, month1, day1
        """
        # Initialize the plot
        plt.style.use(self.STYLE)
        fig = plt.figure()
        ax_vel = plt.subplot2grid((1, 1), (0, 0), 1, 1, fig)
        ax_vel.set_xlabel("Date", loc = "right")
        ax_vel.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y"))
        ax_vel.set_ylabel(self.LABELVEL, loc = "top")
        ax_vel.set_ylim(self.LIMVEL0, self.LIMVEL1)
        ax_vel.set_yticks(linspace(self.LIMVEL0, self.LIMVEL1, self.YTICKSNUM))
        ax_dens = ax_vel.twinx()
        ax_dens.set_ylabel(self.LABELDENS, loc="top")
        ax_dens.set_ylim(self.LIMDENS0, self.LIMDENS1)
        ax_dens.set_yticks(linspace(self.LIMDENS0, self.LIMDENS1, self.YTICKSNUM))
        # Format x axis labels
        for label in ax_vel.get_xticklabels(which = "major"):
            label.set(rotation=30, horizontalalignment = "right")
        # If date limits are provided, use them
        if kwargs == {}: data = self.dbm.selectall()
        else:
            year0, month0, day0 = kwargs["year0"], kwargs["month0"], kwargs["day0"]
            year1, month1, day1 = kwargs["year1"], kwargs["month1"], kwargs["day1"]
            data = self.dbm.selectmulti(year0, month0, day0, year1, month1, day1)
        # Get the data and plot
        dates = collections.deque()
        vels = collections.deque()
        dens = collections.deque()
        for i in data:
            dates.append(i.datetime_date())
            vels.append(i.vel())
            dens.append(i.dens())
        plot_vel, = ax_vel.plot(dates, vels, self.STYLEVEL)
        plot_dens, = ax_dens.plot(dates, dens, self.STYLEDENS)
        ax_vel.yaxis.label.set_color(plot_vel.get_color())
        ax_vel.tick_params(axis="y", colors=plot_vel.get_color())
        ax_dens.yaxis.label.set_color(plot_dens.get_color())
        ax_dens.tick_params(axis="y", colors=plot_dens.get_color())
        
        plt.show()
    
    
    def plot_show(self, what, **kwargs):
        """
        Plots the given 'what' = 'vel', 'dens'
        kwargs used to specify the time interval
        year0, month0, day0, year1, month1, day1
        """
        if what == 2: what = "vel"
        elif what == 3: what = "dens"
        else: raise Exception("databasemanagerrunning.plot_over error")
        
        if what == "vel":
            xlabel = self.LABELVEL
            styleline = self.STYLEVEL
            lim0, lim1 = self.LIMVEL0, self.LIMVEL1
        elif what == "dens":
            xlabel = self.LABELDENS
            styleline = self.STYLEDENS
            lim0, lim1 = self.LIMDENS0, self.LIMDENS1
        else:
            msg = ("DataBaseManagerRunningPlotter.plot only accepts 'vel' "
                "and 'dens' to plot")
            raise Exception(msg)
        # Initialize the plot
        plt.style.use(self.STYLE)
        fig = plt.figure()
        ax = plt.subplot2grid((1, 1), (0, 0), 1, 1, fig)
        ax.set_xlabel("Date", loc = "right")
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y"))
        ax.set_ylabel(xlabel, loc = "top")
        ax.set_ylim(lim0, lim1)
        ax.set_yticks(linspace(lim0, lim1, self.YTICKSNUM))
        # Format x axis labels
        for label in ax.get_xticklabels(which = "major"):
            label.set(rotation=30, horizontalalignment = "right")
        # If date limits are provided, use them
        if kwargs == {}: data = self.dbm.selectall()
        else:
            year0, month0, day0 = kwargs["year0"], kwargs["month0"], kwargs["day0"]
            year1, month1, day1 = kwargs["year1"], kwargs["month1"], kwargs["day1"]
            data = self.dbm.selectmulti(year0, month0, day0, year1, month1, day1)
        # Get the data and plot
        dates = collections.deque()
        values = collections.deque()
        for i in data:
            dates.append(i.datetime_date())
            values.append(getattr(i, what)())
        plot, = ax.plot(dates, values, styleline)
        ax.yaxis.label.set_color(plot.get_color())
        ax.tick_params(axis="y", colors=plot.get_color())
        
        plt.show()