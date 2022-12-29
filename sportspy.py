import tkinter as tk
import os

from running import SessionRunning, DataBaseManagerRunning, DataBaseManagerRunningPlotter
from ui import UI


def main():
    
    database = "database.db"
    try: os.remove(database)
    except: pass
    
    from testdata import years, months, days, distances, times, kcals
    sessions = []
    for i in range(len(days)):
        sessionRunning = SessionRunning(years[i], months[i], days[i],
            distances[i], times[i], kcals[i])
        sessions.append(sessionRunning)
    
    global dbm
    dbm = DataBaseManagerRunning(database)
    for session in sessions: dbm.insert(session)
    
    global dbmp
    dbmp = DataBaseManagerRunningPlotter(dbm)
    #dbmp.plotall()
    
    root = UI()


if __name__ == "__main__":
    
    os.system("cls")
    print("Welcome to SportsPy!")
    main()