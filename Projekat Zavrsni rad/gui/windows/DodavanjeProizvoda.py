import tkinter as tk
from gui import constants as cst
import db
from db import models as mdl

active=0
class DodavanjeProizvoda(tk.Frame):

    def __init__(self,master:tk.Tk):
        global active
        super().__init__(master,bd=10)
        if active==0:
            self.pack(anchor="n")
            active=1
        
        self.na_var=tk.StringVar()
        
        self.naziv=tk.Label(self, text="DODAVANJE PROIZVODA",font=cst.MAIN_FONT)
        self.l_sp=tk.Label(self, text="Šifra proizvoda", font=cst.MAIN_FONT)
        self.l_np=tk.Label(self, text="Naziv proizvoda", font=cst.MAIN_FONT)
        self.l_cp=tk.Label(self, text="Cena proizvoda", font=cst.MAIN_FONT)
        self.e_sp=tk.Entry(self, text="", font=cst.MAIN_FONT)
        self.e_np=tk.Entry(self, textvariable=self.na_var,font=cst.MAIN_FONT)
        self.e_cp=tk.Entry(self, text="", font=cst.MAIN_FONT)


        self.save_button=tk.Button(self, text="Sačuvaj promene", font=cst.MAIN_FONT, command=lambda: self.save_event())
        self.cancel_button=tk.Button(self, text="Odustani", font=cst.MAIN_FONT, command=lambda: self.cancel_event())

        self.naziv.grid(row=0,column=2,columnspan=2)
        self.l_sp.grid(row=1,column=0)
        self.e_sp.grid(row=1,column=1)
        self.l_np.grid(row=1,column=2)
        self.e_np.grid(row=1,column=3)
        self.l_cp.grid(row=1,column=4)
        self.e_cp.grid(row=1,column=5)
        self.save_button.grid(row=2,column=3,columnspan=1)
        self.cancel_button.grid(row=2,column=2,columnspan=1)
       

    def save_event(self):
        session=db.DBManager.session()
        sifra=self.e_sp.get()
        ime=self.na_var.get()
        cena=self.e_cp.get()
        mdl.Proizvodi.dodavnje_proizvoda(sifra,ime,cena)
        self.forget()

    def cancel_event(self):
        global active
        self.forget()
        active=0