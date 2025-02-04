import db 
import os
import sqlalchemy as sql
import sqlalchemy.orm as orm
from tkinter import messagebox
db.DBEngine.SETTINGS_FILE=os.getcwd() + "/settings.ini"
session=db.DBManager.session()

class Sirovine(db.DBManager.get_base()):
    __tablename__ = "sirovine"
    sifra_artikla = sql.Column("sifra_artikla", sql.Integer,primary_key=True)
    ime_artikla= sql.Column("ime_artikla", sql.String, nullable=False)
    cena_artikla_PJM = sql.Column("cena_artikla_po_jedinici_mere", sql.Float, nullable=True)
    kolicina_artikala= sql.Column("kolicina_artikala", sql.Float, nullable=True)
    

    def __init__(self, **data):
        if len(data.keys()) == 0:
            return

        if "sifra_artikla" in data: 
            self.sifra_artikla = data["sifra_artikla"]
        self.ime_artikla = data["ime_artikla"]
        if "cena_artikla_po_jedinici_mere" in data:
            self.cena_artikla_PJM = data["cena_artikla_po_jedinici_mere"]
        if "kolicina_artikala" in data:
            self.kolicina_artikala = data["kolicina_artikala"]

    def ukupna_cena(self):
        if self.cena_artikla_PJM is None or self.cena_artikla_PJM is None:
            return 
        return round((self.cena_artikla_PJM*self.kolicina_artikala),2)
    
    def __str__(self):
        return f"sifra: {self.sifra_artikla}, ime: {self.ime_artikla}, cena artikla po jedinici mere: {self.cena_artikla_PJM}, kolicina: {self.kolicina_artikala}, ukupna cena: {self.ukupna_cena()}"
    

    @staticmethod
    def unosenje_kolicine(sifra: int,cena: float,kolicina:float):
        sir=session.query(Sirovine).get(sifra)
        if sir == None:
            messagebox.showwarning("Pogrešna šifra","Šifra ne postoji ili je niste uneli!")
            return 
        else:
            try:
                sir.cena_artikla_PJM=cena
            except ValueError:
                messagebox.showwarning("Greška vrednosti","Vrednost mora da se unese i mora da bude broj")
                sir.cena_artikla_PJM=None
            try:
                if sir.kolicina_artikala is None:
                    sir.kolicina_artikala=0
                sir.kolicina_artikala=sir.kolicina_artikala+kolicina
            except ValueError:
                messagebox.showwarning("Greška vrednosti","Vrednost mora da se unese i mora da bude broj")
                sir.kolicina=None



            if sir.cena_artikla_PJM is not None or sir.kolicina is not None:
                session.commit()
                messagebox.showinfo("Unos uspešan!", "Uspešno ste uneli željenu količinu!")
            else:
                messagebox.showwarning("Greška sa podacima","Morate da unesete podatke")
        
    @staticmethod
    def dodavanje_sirovine(sifra,ime):
        nova_sirovina=Sirovine(
                sifra_artikla=int(sifra),
                ime_artikla=ime)
        sifre=[]
        sirovine=session.query(Sirovine).all()
        for sir in sirovine:
            sifre.append(str(sir.sifra_artikla))
        
        if str(sifra) not in sifre:
            session.add(nova_sirovina)
            session.commit()
            messagebox.showinfo("Unos uspešan!", "Uspešno ste dodali željenu sirovinu!")
        else:
            messagebox.showwarning("Šifra već postoji","Šifra već postoji! Uneti nepostojeću šifru!")
    @staticmethod
    def brisanje_sirovine(sifra: int):
        sir=session.query(Sirovine).get(sifra)
        if sir == None:
            messagebox.showwarning("Pogrešna šifra","Šifra ne postoji ili je niste uneli!")
            return 
        else:
            unos=messagebox.askyesno("Da li ste sigurni?", "Da li ste sigurni da želite  da obrišete ovu sirovinu?")
            
            if unos==True:
                session.delete(sir)
                session.commit()
                messagebox.showinfo("Brisanje uspešno", "Sirovina uspešno obrisana!")
            else:
                pass
    @staticmethod
    def brsianje_kolicine(sifra: int,kolicina:float):
        sir=session.query(Sirovine).get(sifra)
        if sir == None:
            messagebox.showwarning("Pogrešna šifra","Šifra ne postoji ili je niste uneli!")
            return 
        else:
            try:
                sir.kolicina_artikala=sir.kolicina_artikala-kolicina
            except ValueError:
                messagebox.showwarning("Greška vrednosti","Vrednost mora da se unese i mora da bude broj")
                sir.kolicina_artikala=None



            if sir.kolicina_artikala is not None:
                session.commit()
                messagebox.showinfo("Unos uspešan!", "Uspešno ste obrisali željenu količinu!")
            else:
                messagebox.showwarning("Greška sa podacima","Morate da unesete podatke")

class Proizvodi(db.DBManager.get_base()):
    __tablename__ = "proizvodi"
    sifra_proizvoda = sql.Column("sifra_proizvoda", sql.Integer,primary_key=True)
    naziv_proizvoda= sql.Column("naziv_proizvoda", sql.String, nullable=False)
    cena_proizvoda = sql.Column("cena_proizvoda", sql.Float, nullable=True)

    def __init__(self, **data):
        if len(data.keys()) == 0:
            return
        if "sifra_proizvoda" in data: 
            self.sifra_proizvoda = data["sifra_proizvoda"]
        self.naziv_proizvoda = data["naziv_proizvoda"]
        if "cena_proizvoda" in data:
            self.cena_proizvoda= data["cena_proizvoda"]
    
    def __str__(self):
        return f"sifra: {self.sifra_proizvoda}, ime: {self.naziv_proizvoda}, cena : {self.cena_proizvoda}"
    
    @staticmethod
    def dodavnje_proizvoda(sifra,naziv,cena):
        novi_proizvod=Proizvodi(
                sifra_proizvoda=int(sifra),
                naziv_proizvoda=naziv,
                cena_proizvoda=float(cena)
        )
        sifre=[]
        proizvod=session.query(Proizvodi).all()
        for pro in proizvod:
            sifre.append(str(pro.sifra_proizvoda))
        
        if str(sifra) not in sifre:
            session.add(novi_proizvod)
            session.commit()
            messagebox.showinfo("Unos uspešan!", "Uspešno ste dodali željeni proizvod!")
        else:
            messagebox.showwarning("Šifra već postoji","Šifra već postoji! Uneti nepostojeću šifru!")

    @staticmethod
    def promena_cene(sifra,cena):
        proizvod=session.query(Proizvodi).get(sifra)
        if proizvod == None:
            messagebox.showwarning("Pogrešna šifra","Šifra ne postoji ili je niste uneli!")
            return 
        else:
            try:
                proizvod.cena_proizvoda=float(cena)
            except ValueError:
                messagebox.showwarning("Greška vrednosti","Vrednost mora da se unese i mora da bude broj")
                proizvod.cena_proizvoda=None
        
            if proizvod.cena_proizvoda is not None:
                session.commit()
                messagebox.showinfo("Unos uspešan!", f"Uspešno ste promenili cenu proizvoda {proizvod.naziv_proizvoda}!")
            else:
                messagebox.showwarning("Greška sa podacima","Morate da unesete podatke")
        
class Porudzbine(db.DBManager.get_base()):
    __tablename__ = "porudzbine"
    broj_stola = sql.Column("broj_stola", sql.Integer,primary_key=True)
    naziv_proizvoda= sql.Column("naziv_proizvoda", sql.String, nullable=False,primary_key=True)
    cena_proizvoda = sql.Column("cena_proizvoda", sql.Double, nullable=False)
    kolicina = sql.Column("kolicina", sql.Integer, nullable=False)
    ukupna_cena=sql.Column("ukupna_cena",sql.Double,nullable=False)

    

    def __init__(self, **data):
        if len(data.keys()) == 0:
            return

        if "broj_stola" in data: 
            self.broj_stola = data["broj_stola"]
        self.naziv_proizvoda = data["naziv_proizvoda"]
        if "cena_proizvoda" in data:
            self.cena_proizvoda = data["cena_proizvoda"]
        if "kolicina" in data:
            self.kolicina = data["kolicina"]
        if "ukupna_cena" in data:
            self.ukupna_cena=data["ukupna_cena"]
    def __str__(self):
        return f"broj: {self.broj_stola}, ime: {self.naziv_proizvoda}, cena : {self.cena_proizvoda}, kolicina: {self.kolicina}, ukupna cena: {self.ukupna_cena}"
    @staticmethod
    def dodavanje_porudzbine(broj,naziv,cena,kolicina,ukupna_cena):
        porudzbina=session.query(Porudzbine).filter((Porudzbine.broj_stola==broj))
        nova_porudzbina=Porudzbine(
            broj_stola=int(broj),
            naziv_proizvoda=naziv,
            cena_proizvoda=float(cena),
            kolicina=int(kolicina),
            ukupna_cena=float(ukupna_cena)
        )
        for p in porudzbina:
            if p.naziv_proizvoda == naziv: 
                nova_porudzbina=None
                p.kolicina+=kolicina
                p.ukupna_cena+=float(ukupna_cena)
                session.commit()
        if nova_porudzbina is not None:
            session.add(nova_porudzbina)
            session.commit()
        else:
            pass

    @staticmethod
    def brisanje_porudzbine(broj):
        porudzbine=session.query(Porudzbine).filter(Porudzbine.broj_stola==broj)
        for por in porudzbine:
            session.delete(por)
            session.commit()