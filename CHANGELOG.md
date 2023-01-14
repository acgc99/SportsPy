# Changelog
+ 27/12/2022
  - Project started with the running sessions
  - SessionRunning and DataBaseManagerRunning classes
  - Basic database managing (insert, delete, update, selectone)
  - DataBaseManagerRunningException created
+ 28/12/2022
  - Now the cursor returns SessionRunning, not raw data
  - Multiselection (dates range)
  - Method for selecting all entries in the db
  - Date can be updated now
  - DataBaseManagerRunningPlotter for plotting mean velocity and kcal density, methods: plot, plotall
+ 29/12/2022
  - Project exported to GitHub
  - Added README.md, LICENSE.md, CHANGELOG.md, TODO.md
  - Started to work with the UI, with the capability to switch between frames
+ 30/12/2022
  - Work on running.ui.PageAddRecord, almost finished, users profiles not implemente yet
+ 01/01/2023
  - ui.Page created and applied to all pages
  - UI flowdiagram
  - running.ui.PagePlot works, although style issues are not addressed
+ 04/01/2023
  - Previosly, the running.ui.PagePlot figure was destroyed and created again, now the figure is cleared and filled again, more efficiente
  - Bug solved, for embedding matplotlib in tkinter use matplotlib.figure.Figure instead of matplotlib.pyplot.figure
+ 06/01/2023
  - running.ui.PageManage visually finished, although unfunctional
+ 08/01/2023
  - running.ui.PageManage functionality finished
  - ui.widgets created
  - ui.widgets.FrameScrollableX, ui.widgets.FrameScrollableY, ui.widgets.FrameScrollableXY
  - ui.Page moved to ui.widgets.Page
+ 14/01/2023
  - running.DatabaseManagerRunning cursor now returns (idsession, running.SessionRunning)
  - running.DataBaseManagerRunning.cl cursor deprecated
  - running.DatabaseManagerRunning now has methods select_one and select_date to select by idsession or date
  - running.DatabaseManagerRunning.update and running.DatabaseManagerRunning.update_all merged into running.DatabaseManagerRunning.update, now update is made by idsession
  - running.DataBaseManagerRunningPlotter.plot, plot_all, plotall_show update, only this function has been updated
  - running.ui adapted to the new changes