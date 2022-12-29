"""
27/12/2022 1h40min
> Project started with the running sessions
> SessionRunning and DataBaseManagerRunning classes
> Basic database managing (insert, delete, update, selectone)
> DataBaseManagerRunningException created
28/12/2022 2h40min + 1h40min
> Now the cursor returns SessionRunning, not raw data
> Multiselection (dates range)
> Method for selecting all entries in the db
> Date can be updated now
> DataBaseManagerRunningPlotter for plotting mean velocity and kcal density, methods: plot, plotall
"""

"""
Objectives
README and those files
review code style
user interface
"""

from running import SessionRunning, DataBaseManagerRunning, DataBaseManagerRunningPlotter


def main():
    
    database = "database.db"
    import os
    try: os.remove(database)
    except: pass
    os.system("cls")
    
    years = [
        2022,
        2022,
        2022,
        2022
        ]
    
    months = [
        12,
        12,
        12,
        12
        ]
    
    days = [
        22,
        23,
        28,
        29
        ]
    
    times = [
        45,
        45,
        45,
        45
        ]
    
    distances = [
        5.1,
        5.2,
        5.1,
        5.0
        ]
    
    kcals = [
        310,
        327,
        280,
        312
        ]
    
    sessions = []
    for i in range(len(days)):
        sessionRunning = SessionRunning(
            years[i], months[i], days[i],
            distances[i],
            times[i],
            kcals[i]
            )
        sessions.append(sessionRunning)
        #print(sessionRunning)
    
    global dbm
    dbm = DataBaseManagerRunning(database)
    for session in sessions:
        dbm.insert(session)
    
    global dbmp
    dbmp = DataBaseManagerRunningPlotter(dbm)
    dbmp.plotall()
    


if __name__ == "__main__":
    
    print("Welcome to SportsPy!")
    main()