import tkinter as tk

from running import SessionRunning, DataBaseManagerRunning, DataBaseManagerRunningPlotter, ui


def main():
    
    database = "database.db"
    import os
    try: os.remove(database)
    except: pass
    os.system("cls")
    
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
    
    root = tk.Tk()
    ui.FrameStart(root)
    root.mainloop()



if __name__ == "__main__":
    
    print("Welcome to SportsPy!")
    main()