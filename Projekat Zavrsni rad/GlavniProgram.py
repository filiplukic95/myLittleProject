import tkinter as tk
import db
import os
from db import models as mdl
from gui.drugiProgram.MainWindow import MainWindow
db.DBEngine.SETTINGS_FILE=os.getcwd() + "/settings.ini"
window=MainWindow()
window.layout()
if __name__ == "__main__":
    window.mainloop()
