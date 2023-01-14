import os

from running import SessionRunning, DatabaseManagerRunning, DatabaseManagerRunningPlotter
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
    dbm = DatabaseManagerRunning(database)
    for session in sessions: dbm.insert(session)
    
    global dbmp
    dbmp = DatabaseManagerRunningPlotter(dbm)
    #dbmp.plotall_show()
    
    
    root = UI()


if __name__ == "__main__":
    
    # windows
    if os.name == "nt": os.system("cls")
    # linux
    elif os.name == "posix": os.system("clear")
    
    print("Welcome to SportsPy!")
    main()