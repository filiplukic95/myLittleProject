import tkinter as tk
from gui import constants as cst
import db
from db import models as mdl

active=0
class BrisanjeSirovina(tk.Frame):

    def __init__(self,master:tk.Tk):
        global active
        super().__init__(master,bd=10)
        if active==0:
            self.pack(anchor="n")
            active=1
        self.na_var=tk.StringVar()
        
        self.naziv=tk.Label(self, text="BRISANJE SIROVINA",font=cst.MAIN_FONT)
        self.l_sa=tk.Label(self, text="Šifra artikla", font=cst.MAIN_FONT)
        self.l_na=tk.Label(self, text="Naziv artikla", font=cst.MAIN_FONT)
        self.e_sa=tk.Entry(self, text="", font=cst.MAIN_FONT)
        self.e_na=tk.Entry(self, textvariable=self.na_var, state="readonly",font=cst.MAIN_FONT)


        self.save_button=tk.Button(self, text="Sačuvaj promene", font=cst.MAIN_FONT, command=lambda: self.save_event())
        self.cancel_button=tk.Button(self, text="Odustani", font=cst.MAIN_FONT, command=lambda: self.cancel_event())

        self.e_sa.bind('<Return>', self.enter_event)

        self.naziv.grid(row=0, column=1,columnspan=3)
        self.l_sa.grid(row=1,column=0)
        self.e_sa.grid(row=1,column=1)
        self.l_na.grid(row=1,column=2)
        self.e_na.grid(row=1,column=3)
        self.save_button.grid(row=2,column=2,columnspan=2)
        self.cancel_button.grid(row=2,column=1,columnspan=1)
    
    def enter_event(self, event):
        session=db.DBManager.session()
        sifra=self.e_sa.get()
        sirovine=session.query(mdl.Sirovine).get(sifra)
        self.na_var.set(sirovine.ime_artikla)

    def save_event(self):
        session=db.DBManager.session()
        sifra=self.e_sa.get()
        mdl.Sirovine.brisanje_sirovine(sifra)
        self.forget()

    def cancel_event(self):
        global active
        self.forget()
        active=0