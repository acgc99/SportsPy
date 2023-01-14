import sqlite3
import datetime
import sys

from .sessionrunning import SessionRunning


class DatabaseManagerRunning(sqlite3.Connection):
    """
    Used to manage 'SessionRunning's data in a database
    """
    
    def __init__(self, database: str):
        # Initialize the database connection
        super().__init__(database)
        def factory(row):
            date = datetime.date.fromordinal(row[1]).isoformat().split("-")
            year, month, day = map(int, date)
            return SessionRunning(year, month, day, *row[2:])
        self.row_factory = lambda cursor, row: factory(row)
        self.c = self.cursor()
        self.row_factory = lambda cursor, row: row[0]
        self.cl = self.cursor() # list cursor (returns list, use when only one field is requested)
        self.row_factory = None
        # Attributes
        self.database = database
        self.tablename = "record"
        self.colsdefs = ("idsession INTEGER PRIMARY KEY UNIQUE, "
            "date INTEGER DEFAULT NULL, "
            "distance REAL DEFAULT NULL, "
            "time REAL DEFAULT NULL, "
            "kcal REAL DEFAULT NULL")
        self.colsnames = ("date, "
            "distance, "
            "time, "
            "kcal")
        self.colsinsert = ", ".join(["?" for i in range(
            len(self.colsnames.split(", ")))])
        # Create the table if needed
        self._create_table()
    
    
    def disconnect(self):
        """
        Closes the current connection to the database
        """
        self.c.close()
        self.close()
    
    
    def reconnect(self):
        """
        Reconnects to the database
        """
        self.__init__(self.database)
    
    
    def _create_table(self):
        """
        Creates the table if needed
        """
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(
            self.tablename, self.colsdefs)
        self.c.execute(query)
        self.commit()
    
    
    def insert(self, sessionRunning: SessionRunning, commit: bool = True):
        """
        Insert new 'SessionRunning' into the database
        """
        query = "INSERT INTO {} ({}) VALUES ({})".format(
            self.tablename, self.colsnames, self.colsinsert)
        self.c.execute(query, sessionRunning)
        if commit: self.commit()
    
    
    def selectone(self, year: int, month: int, day: int):
        """
        Select one 'SessionRunning' from the database given its date
        """
        # Check if the 'SessionRunning' is registered on the database
        date = datetime.date(year, month, day).toordinal()
        self.check_if_in_database(date)
        # Select
        query = "SELECT * FROM {} WHERE date = {}".format(
            self.tablename,
            date
            )
        self.c.execute(query)
        sessionRunning = self.c.fetchone()
        return sessionRunning
    
    
    def selectmulti(self, year0: int, month0: int, day0: int, year1: int,
        month1: int, day1: int):
        """
        Select all the 'SessionRunning's from the database given the limits of
        the dates range
        """
        date0 = datetime.date(year0, month0, day0).toordinal()
        date1 = datetime.date(year1, month1, day1).toordinal()
        nrows = self.nrows()
        query = "SELECT * FROM {} WHERE date >= {} AND date <= {}".format(
            self.tablename, date0, date1)
        self.c.execute(query)
        for i in range(nrows):
            yield self.c.fetchone()
    
    
    def selectall(self):
        """
        Select all 'SessionRunning's from the database
        """
        nrows = self.nrows()
        query = "SELECT * FROM {}".format(self.tablename)
        self.c.execute(query)
        for i in range(nrows):
            yield self.c.fetchone()
    
    
    def update(self, col: str, value, year0: int, month0: int, day0: int, 
        commit: bool = True):
        """
        Update the data of a 'SessionRunning' given its date
        """
        # The idsession is unique, so it cannot be changed to avoid errors
        if col == "idsession":
            msg = "The idsession cannot be changed"
            raise DataBaseManagerRunningException(msg)
        # Check if the 'SessionRunning' is registered on the database
        date0 = datetime.date(year0, month0, day0).toordinal()
        self.check_if_in_database(date0)
        # If the date is requested to be updated, some changes are needed
        if col == "date":
            year1, month1, day1 = map(int, value.split("-"))
            date1 = datetime.date(year1, month1, day1).toordinal()
            value = date1
        # Update
        query = "UPDATE {} SET {} = {} WHERE date = {}".format(
            self.tablename,
            col,
            value,
            date0
            )
        self.c.execute(query)
        if commit: self.commit()
    
    
    def update_all(self, idsession, year, month, day, distance, time, kcal, commit = True):
        """
        Update all the data of a 'SessionRunning' given its idsession
        """
        # Check if the 'SessionRunning' is registered on the database
        
        
        sessionRunning = SessionRunning(year, month, day, distance, time, kcal)
        # Update
        query = ("UPDATE {} SET "
            "date = {}, "
            "distance = {}, "
            "time = {}, "
            "kcal = {} "
            "WHERE idsession = {}").format(
            self.tablename,
            sessionRunning.date, distance, time, kcal, idsession
            )
        self.c.execute(query)
        if commit: self.commit()
    
    
    def delete(self, idsession: int, commit = True):
        """
        Delete a 'SessionRunning' from the database given its idsession
        """
        # Check if the 'SessionRunning' is registered on the database
        #date = datetime.date(year, month, day).toordinal()
        #self.check_if_in_database(date)
        # Delete
        query = "DELETE FROM {} WHERE idsession = {}".format(self.tablename, idsession)
        self.c.execute(query)
        if commit: self.commit()
    
    
    def check_if_in_database(self, date: int):
        """
        Checks if there is a 'SessionRunning' with the given date in the database
        """
        query = "SELECT * FROM {} WHERE date = {}".format(self.tablename, date)
        self.c.execute(query)
        data = self.c.fetchone()
        if data is None:
            msg = "There is no record with that date"
            raise DataBaseManagerRunningException(msg)
    
    
    def nrows(self):
        """
        Returns the number of rows in the database ( = the number of
        'SessionRunning's registered)
        """
        c = self.cursor()
        c.execute("SELECT COUNT(*) FROM {}".format(self.tablename))
        nrows = c.fetchone()[0]
        return nrows


class DataBaseManagerRunningException(Exception):
    """
    Used to raise exceptions regarding 'DataBaseManagerRunning'
    """
    
    
    def __init__(self, msg):
        
        super().__init__(msg)