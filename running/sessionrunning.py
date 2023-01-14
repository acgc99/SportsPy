from collections import namedtuple
import datetime


SessionRunningTuple = namedtuple(typename="SessionRunningTuple", field_names=[
    "date", "distance", "time", "kcal"])


class SessionRunning(SessionRunningTuple):
    """
    Class representing a session of running exercise. The units used are:
    'distance' in km, 'time' in min, 'kcal' in kcal
    """
    
    def __new__(cls, year: int, month: int, day: int, distance : float,
        time : float, kcal : float):
        date = datetime.date(year, month, day).toordinal()
        self = super().__new__(cls, date, distance, time, kcal)
        return self
    
    
    def vel(self):
        """
        Returns the mean velocity in km/h
        """
        return round(self.distance/self.time*60, 1)
    
    
    def dens(self):
        """
        Returns the mean kcal density in kcal/km
        """
        return round(self.kcal/self.distance, 1)
    
    
    def datetime_date(self):
        """
        Returns the date as a 'datetime.date' object
        """
        return datetime.date.fromordinal(self.date)
    
    
    def date_str(self):
        """
        Returns the date in the ISO 8601 format
        """
        return self.datetime_date().isoformat()
    
    
    def date_dict(self):
        """
        Returns the date in a 'dict'
        """
        year, month, day = map(int, self.date_str().split("-"))
        return {"year": year, "month": month, "day": day}