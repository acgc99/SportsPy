import collections

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from .sessionrunning import SessionRunning
from .databasemanagerrunning import DataBaseManagerRunning


class DataBaseManagerRunningPlotter:
    
    
    def __init__(self, dbm: DataBaseManagerRunning):
        
        self.dbm = dbm
        
        self.STYLE = "bmh"
        
        self.LABELVEL = "v (km/h)"
        self.LABELDENS = "d (kcal/km)"
        
        self.STYLEVEL = "b-"
        self.STYLEDENS = "r-"
        
        self.LIMVEL0, self.LIMVEL1 = 0, 20
        self.LIMDENS0, self.LIMDENS1 = 0, 100
    
    
    def plot(self, what, show=True, **kwargs):
        """
        kwargs used to specify the time interval
        year0, month0, day0, year1, month1, day1
        """
        
        if what == "vel":
            xlabel = self.LABELVEL
            style = self.STYLEVEL
            lim0, lim1 = self.LIMVEL0, self.LIMVEL1
        elif what == "dens":
            xlabel = self.LABELDENS
            style = self.STYLEDENS
            lim0, lim1 = self.LIMDENS0, self.LIMDENS1
        else:
            raise Exception(repr(what))
        
        plt.style.use(self.STYLE)
        
        fig = plt.figure()
        
        ax = plt.subplot2grid((1, 1), (0, 0), 1, 1, fig)
        ax.set_xlabel("Date", loc = "right")
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y"))
        ax.set_ylabel(xlabel, loc = "top")
        ax.set_ylim(lim0, lim1)
        
        for label in ax.get_xticklabels(which = "major"):
            label.set(rotation=30, horizontalalignment = "right")
        
        if kwargs == {}: data = self.dbm.selectall()
        else:
            year0, month0, day0 = kwargs["year0"], kwargs["month0"], kwargs["day0"]
            year1, month1, day1 = kwargs["year1"], kwargs["month1"], kwargs["day1"]
            data = self.dbm.selectmulti(year0, month0, day0, year1, month1, day1)
        
        dates = collections.deque()
        values = collections.deque()
        for i in data:
            dates.append(i.datetime_date())
            values.append(getattr(i, what)())
        plot, = ax.plot(dates, values, style)
        
        ax.yaxis.label.set_color(plot.get_color())
        ax.tick_params(axis="y", colors=plot.get_color())
        
        if show: plt.show()
    
    
    def plotall(self, show=True, **kwargs):
        """
        kwargs used to specify the time interval
        year0, month0, day0, year1, month1, day1
        """
        
        plt.style.use(self.STYLE)
        
        fig = plt.figure()
        
        ax_vel = plt.subplot2grid((1, 1), (0, 0), 1, 1, fig)
        ax_vel.set_xlabel("Date", loc = "right")
        ax_vel.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y"))
        ax_vel.set_ylabel(self.LABELVEL, loc = "top")
        ax_vel.set_ylim(self.LIMVEL0, self.LIMVEL1)
        
        ax_dens = ax_vel.twinx()
        ax_dens.set_ylabel(self.LABELDENS, loc="top")
        ax_dens.set_ylim(self.LIMDENS0, self.LIMDENS1)
        
        for label in ax_vel.get_xticklabels(which = "major"):
            label.set(rotation=30, horizontalalignment = "right")
        
        if kwargs == {}: data = self.dbm.selectall()
        else:
            year0, month0, day0 = kwargs["year0"], kwargs["month0"], kwargs["day0"]
            year1, month1, day1 = kwargs["year1"], kwargs["month1"], kwargs["day1"]
            data = self.dbm.selectmulti(year0, month0, day0, year1, month1, day1)
        
        """
        # If this is less efficient will be determined when the amount of data is big enough
        for i in data:
            date = i.datetime_date()
            ax_vel.scatter(date, i.vel(), c="b")
            ax_dens.scatter(date, i.dens(), c="r")
        
        dates = [ax_dens.collections[i].get_offsets()[0][0] for i in range(len(ax_dens.collections))]
        dens = [ax_dens.collections[i].get_offsets()[0][1] for i in range(len(ax_dens.collections))]
        vels = [ax_vel.collections[i].get_offsets()[0][1] for i in range(len(ax_vel.collections))]
        
        ax_dens.plot(dates, dens)
        ax_vel.plot(dates, vels)
        """
        
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
        
        if show: plt.show()