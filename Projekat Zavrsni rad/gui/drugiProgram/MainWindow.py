import tkinter as tk
from gui import constants as cs
from gui.windows.Sto import Sto
import db
from db import models as mdl

session=db.DBManager.session()

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Aplikacija za rad")
        width=self.winfo_screenwidth()
        height=self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))
        self.state("zoomed")
        self.mainframe=tk.Frame(self)
        self.mainframe.pack(fill="both",expand=True)

    def layout(self):
        self.sto1=tk.Button(self.mainframe,text="1", bg="green", fg="black", font=cs.MAIN_FONT,anchor="center",width=15,height=3,command=lambda: Sto(self.mainframe,"1"))
        self.sto1.place(x=50,y=100)
        self.sto2=tk.Button(self.mainframe,text="2", bg="green", fg="black", font=cs.MAIN_FONT,anchor="center",width=15,height=3,command=lambda: Sto(self.mainframe,"2"))
        self.sto2.place(x=450,y=100)
        self.sto3=tk.Button(self.mainframe,text="3", bg="green", fg="black", font=cs.MAIN_FONT,anchor="center",width=15,height=3,command=lambda: Sto(self.mainframe,"3"))
        self.sto3.place(x=850,y=100)
        self.sto4=tk.Button(self.mainframe,text="4", bg="green", fg="black", font=cs.MAIN_FONT,anchor="center",width=15,height=3,command=lambda: Sto(self.mainframe,"4"))
        self.sto4.place(x=1250,y=100)
        self.sto5=tk.Button(self.mainframe,text="5", bg="green", fg="black", font=cs.MAIN_FONT,anchor="center",width=15,height=3,command=lambda: Sto(self.mainframe,"5"))
        self.sto5.place(x=1650,y=100)
        self.sto11=tk.Button(self.mainframe,text="11", bg="green", fg="black", font=cs.MAIN_FONT,anchor="center",width=15,height=3,command=lambda: Sto(self.mainframe,"11"))
        self.sto11.place(x=50,y=600)
        self.sto12=tk.Button(self.mainframe,text="12", bg="green", fg="black", font=cs.MAIN_FONT,anchor="center",width=15,height=3,command=lambda: Sto(self.mainframe,"12"))
        self.sto12.place(x=450,y=600)
        self.sto13=tk.Button(self.mainframe,text="13", bg="green", fg="black", font=cs.MAIN_FONT,anchor="center",width=15,height=3,command=lambda: Sto(self.mainframe,"13"))
        self.sto13.place(x=850,y=600)
        self.sto14=tk.Button(self.mainframe,text="14", bg="green", fg="black", font=cs.MAIN_FONT,anchor="center",width=15,height=3,command=lambda: Sto(self.mainframe,"14"))
        self.sto14.place(x=1250,y=600)
        self.sto15=tk.Button(self.mainframe,text="15", bg="green", fg="black", font=cs.MAIN_FONT,anchor="center",width=15,height=3,command=lambda: Sto(self.mainframe,"15"))
        self.sto15.place(x=1650,y=600)

    