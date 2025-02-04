import tkinter as tk
from gui import constants as cst
import db
from db import models as mdl

active=0
class PromenaCeneProizvoda(tk.Frame):

    def __init__(self,master:tk.Tk):
        global active
        super().__init__(master,bd=10)
        if active==0:
            self.pack(anchor="n")
            active=1
        
        self.np_var=tk.StringVar()
        self.cp_var=tk.DoubleVar()
        
        self.naziv=tk.Label(self, text="PROMENA CENE PROIZVODA",font=cst.MAIN_FONT)
        self.l_sp=tk.Label(self, text="Šifra proizvoda", font=cst.MAIN_FONT)
        self.l_np=tk.Label(self, text="Naziv proizvoda", font=cst.MAIN_FONT)
        self.l_cp=tk.Label(self, text="Cena proizvoda", font=cst.MAIN_FONT)
        self.e_sp=tk.Entry(self, text="", font=cst.MAIN_FONT)
        self.e_np=tk.Entry(self, textvariable=self.np_var, state="readonly",font=cst.MAIN_FONT)
        self.e_cp=tk.Entry(self, textvariable=self.cp_var, font=cst.MAIN_FONT)
       
        self.save_button=tk.Button(self, text="Sačuvaj promene", font=cst.MAIN_FONT, command=lambda: self.save_event())
        self.cancel_button=tk.Button(self, text="Odustani", font=cst.MAIN_FONT, command=lambda: self.cancel_event())

        self.e_sp.bind('<Return>', self.enter_event)

        self.naziv.grid(row=0,column=2,columnspan=2)
        self.l_sp.grid(row=1,column=0)
        self.e_sp.grid(row=1,column=1)
        self.l_np.grid(row=1,column=2)
        self.e_np.grid(row=1,column=3)
        self.l_cp.grid(row=1,column=4)
        self.save_button.grid(row=2,column=3,columnspan=1)
        self.cancel_button.grid(row=2,column=2,columnspan=1)
        self.e_cp.grid(row=1,column=5)
        

    def enter_event(self, event):
        session=db.DBManager.session()
        sifra=self.e_sp.get()
        proizvod=session.query(mdl.Proizvodi).get(sifra)
        self.np_var.set(proizvod.naziv_proizvoda)
        self.cp_var.set(proizvod.cena_proizvoda)
        

    def save_event(self):
        session=db.DBManager.session()
        sifra=self.e_sp.get()
        cena=self.cp_var.get()
        mdl.Proizvodi.promena_cene(sifra,cena)
        self.forget()

    def cancel_event(self):
        global active
        self.forget()
        active=0