import tkinter as tk
from tkinter import ttk
from gui import constants as cst
import db
from db import models as mdl
from gui.windows import UvozSirovina as us
from gui.windows import IzlazSirovina as izs
from gui.windows import DodavanjeSirovina as ds
from gui.windows import BrisanjeSirovina as bs 
from gui.windows import DodavanjeProizvoda as dp
from gui.windows import PromenaCeneProizvoda as pcp 
session=db.DBManager.session()
class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Aplikacija za sirovine")
        width=self.winfo_screenwidth()
        height=self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))

    def layout(self):
        self.levi_frame=tk.Frame(self, background="#a8f584",bd=2 )
        self.levi_frame.pack(side="left",fill="both")
        self.button1=tk.Button(self.levi_frame, text="Pregled stanja sirovina", font=cst.MAIN_FONT,border=5, fg="black",anchor="w",overrelief="groove",width=20, command=lambda: self.show_tree())
        self.button1.pack(ipady=5,ipadx=100,)
        self.button2=tk.Button(self.levi_frame, text="Ulaz sirovina",border=5, font=cst.MAIN_FONT,fg="black",anchor="w",overrelief="groove",width=20, command=lambda: us.UvozSirovina(self.desni_frame) )
        self.button2.pack(ipady=5,ipadx=100,padx=0)
        self.button3=tk.Button(self.levi_frame, text="Izlaz sirovina",border=5,font=cst.MAIN_FONT, fg="black",anchor="w",overrelief="groove",width=20,command=lambda: izs.IzlazSirovina(self.desni_frame))
        self.button3.pack(ipady=5,ipadx=100,padx=0)
        self.button4=tk.Button(self.levi_frame, text="Dodavanje sirovina",border=5, font=cst.MAIN_FONT,fg="black",anchor="w",overrelief="groove",width=20, command=lambda: ds.DodavanjeSirovina(self.desni_frame))
        self.button4.pack(ipady=5,ipadx=100,padx=0)
        self.button5=tk.Button(self.levi_frame, text="Brisanje sirovina",border=5, font=cst.MAIN_FONT,fg="black",anchor="w",overrelief="groove",width=20, command=lambda: bs.BrisanjeSirovina(self.desni_frame) )
        self.button5.pack(ipady=5,ipadx=100,padx=0)
        self.button6=tk.Button(self.levi_frame, text="Dodavanje proizvoda",border=5, font=cst.MAIN_FONT,fg="black",anchor="w",overrelief="groove",width=20, command=lambda:dp.DodavanjeProizvoda(self.desni_frame)  )
        self.button6.pack(ipady=5,ipadx=100,padx=0)
        self.button7=tk.Button(self.levi_frame, text="Promena cene proizvoda",border=5, font=cst.MAIN_FONT,fg="black",anchor="w",overrelief="groove",width=20, command=lambda: pcp.PromenaCeneProizvoda(self.desni_frame) )
        self.button7.pack(ipady=5,ipadx=100,padx=0)
        self.desni_frame=tk.Frame(self,)
        self.desni_frame.pack(fill="both",expand="yes")
        self.tree=None
       
    def show_tree(self):
        
            if self.tree is not None:
                self.tree.destroy()
                self.tree=None
            kolone=("1", "2", "3","4","5")
            self.tree=ttk.Treeview(self.desni_frame,columns=kolone,show="headings")

            self.tree.heading("1",text="Šifra artikla",anchor="w")
            self.tree.heading("2",text="Naziv artikla",anchor="w")
            self.tree.heading("3",text="Cena artikla po jedinici mere",anchor="w")
            self.tree.heading("4",text="Količina artikla",anchor="w")
            self.tree.heading("5",text="Ukupna cena artikla",anchor="w")

            
                
            podaci=[]

            sirovine=session.query(mdl.Sirovine).all()
            for sir in sirovine:
                podaci.append((sir.sifra_artikla,sir.ime_artikla,sir.cena_artikla_PJM,sir.kolicina_artikala,sir.ukupna_cena()))

            for podatak in podaci:
                self.tree.insert('',tk.END, values=podatak)

            
            self.tree.pack(fill="both",expand="yes",side="bottom")
                



