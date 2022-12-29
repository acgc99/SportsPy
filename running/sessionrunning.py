from collections import namedtuple
import datetime

SessionRunningTuple = namedtuple(
    typename="SessionRunningTuple",
    field_names=[
        "date",
        "distance",
        "time",
        "kcal"
    ]
)


class SessionRunning(SessionRunningTuple):
    
    
    def __new__(cls,
        year, # int
        month, # int
        day, # int
        distance : float, # km
        time : float, # min
        kcal : float # kcal
        ):
        date = datetime.date(year, month, day).toordinal()
        self = super().__new__(
            cls,
            date,
            distance,
            time,
            kcal
        )
        return self
    
    
    def vel(self):
        return round(self.distance/self.time*60, 1) # km/h
    
    
    def dens(self):
        return round(self.kcal/self.distance, 1) # kcal/km
    
    
    def datetime_date(self):
        return datetime.date.fromordinal(self.date)
    
    
    def date_str(self):
        return self.datetime_date().isoformat()
    
    
    def date_dict(self):
        year, month, day = map(int, self.date_str().split("-"))
        return {"year": year, "month": month, "day": day}