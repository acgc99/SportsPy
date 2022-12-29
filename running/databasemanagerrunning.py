import sqlite3
import datetime
import sys

from .sessionrunning import SessionRunning


class DataBaseManagerRunning(sqlite3.Connection):
    
    
    def __init__(self, database: str):
        
        super().__init__(database)
        self.database = database
        
        def cursor_to_session(row):
            date = datetime.date.fromordinal(row[1]).isoformat().split("-")
            year, month, day = map(int, date)
            return SessionRunning(year, month, day, *row[2:])
        self.row_factory = lambda cursor, row: cursor_to_session(row)
        self.c = self.cursor()
        self.row_factory = None
        
        
        
        self.tablename = "record"
        self.colsdefs = (
            "idsession INTEGER PRIMARY KEY UNIQUE, "
            "date INTEGER DEFAULT NULL, "
            "distance REAL DEFAULT NULL, "
            "time REAL DEFAULT NULL, "
            "kcal REAL DEFAULT NULL"
            )
        self.colsnames = (
            "date, "
            "distance, "
            "time, "
            "kcal"
            )
        self.colsinsert = ", ".join([
            "?" for i in range(len(self.colsnames.split(", ")))
            ])
        self._create_table()
    
    
    def disconnect(self):
        self.c.close()
        self.close()
    
    
    def reconnect(self):
        self.__init__(self.database)
    
    
    def _create_table(self):
        
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(
            self.tablename,
            self.colsdefs
            )
        self.c.execute(query)
        self.commit()
    
    
    def insert(self, sessionRunning: SessionRunning, commit: bool = True):
        
        query = "INSERT INTO {} ({}) VALUES ({})".format(
            self.tablename,
            self.colsnames,
            self.colsinsert
            )
        self.c.execute(query, sessionRunning)
        if commit: self.commit()
    
    
    def selectone(self, year: int, month: int, day: int):
        
        date = datetime.date(year, month, day).toordinal()
        self.check_if_in_database(date)
        query = "SELECT * FROM {} WHERE date = {}".format(
            self.tablename,
            date
            )
        self.c.execute(query)
        sessionRunning = self.c.fetchone()
        return sessionRunning
    
    
    def selectmulti(self, year0: int, month0: int, day0, year1: int, month1: int, day1: int):
        
        date0 = datetime.date(year0, month0, day0).toordinal()
        date1 = datetime.date(year1, month1, day1).toordinal()
        nrows = self.nrows()
        query = "SELECT * FROM {} WHERE date >= {} AND date <= {}".format(
            self.tablename,
            date0,
            date1
            )
        self.c.execute(query)
        for i in range(nrows):
            yield self.c.fetchone()
    
    
    def selectall(self):
        
        nrows = self.nrows()
        query = "SELECT * FROM {}".format(self.tablename)
        self.c.execute(query)
        for i in range(nrows):
            yield self.c.fetchone()
    
    
    def update(self, col: str, value, year0: int, month0: int, day0: int, commit: bool = True):
        
        if col == "idsession":
            raise DataBaseManagerRunningException("The idsession cannot be changed")
        date0 = datetime.date(year0, month0, day0).toordinal()
        self.check_if_in_database(date0)
        if col == "date":
            year1, month1, day1 = map(int, value.split("-"))
            date1 = datetime.date(year1, month1, day1).toordinal()
            value = date1
        query = "UPDATE {} SET {} = {} WHERE date = {}".format(
            self.tablename,
            col,
            value,
            date0
            )
        self.c.execute(query)
        if commit: self.commit()
    
    
    def delete(self, year, month, day, commit = True):
        
        date = datetime.date(year, month, day).toordinal()
        self.check_if_in_database(date)
        query = (
            "DELETE FROM {} WHERE date = {}".format(self.tablename, date)
            )
        self.c.execute(query)
        if commit: self.commit()
    
    
    def check_if_in_database(self, date):
        
        query = "SELECT * FROM {} WHERE date = {}".format(
            self.tablename,
            date
            )
        self.c.execute(query)
        data = self.c.fetchone()
        if data is None:
            raise DataBaseManagerRunningException("There is no record with that date")
    
    
    def nrows(self):
        
        c = self.cursor()
        c.execute("SELECT COUNT(*) FROM {}".format(self.tablename))
        nrows = c.fetchone()[0]
        return nrows


class DataBaseManagerRunningException(Exception):
    
    
    def __init__(self, message):
        
        super().__init__(message)