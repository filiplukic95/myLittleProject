import tkinter as tk
from tkinter import ttk
from gui import constants as cst
import db
from db import models as mdl



session=db.DBManager.session()
class Sto(tk.Frame):

    def __init__(self,master,sto:str):
        super().__init__(master)
        width=self.winfo_screenwidth()
        height=self.winfo_screenheight()
        self.pack(expand=True,fill="both")
        self.sto=int(sto)

        self.gornji_frame=tk.Frame(self,bg="blue",bd=2)
        self.srednji_frame=tk.Frame(self, bg="grey",bd=2)
        self.donji_frame=tk.Frame(self, bg="blue",bd=2)
        
        self.gornji_frame.pack(side="top",fill="both")
        self.srednji_frame.pack(after=self.gornji_frame,fill="both")
        self.donji_frame.pack(side="bottom",fill="x")

        self.cena_var=tk.DoubleVar()

        

        self.prodaja=tk.Button(self.gornji_frame, text="PRODAJA", font=cst.MAIN_FONT,bg="green",fg="black",width=10,height=2,command=lambda: Prodaja(self,self.sto))
        self.prodaja.pack(side="right",ipadx=50,ipady=5,padx=5,pady=5)
        self.kasa=tk.Button(self.donji_frame,text="KASA", font=cst.MAIN_FONT,bg="green",fg="black",width=10,height=2,command=lambda: self.naplata(self.sto))
        self.kasa.pack(side="left",ipadx=50,ipady=5,padx=5,pady=5)
        self.izlaz=tk.Button(self.donji_frame,text="IZLAZ", font=cst.MAIN_FONT,bg="red",fg="black",width=10,height=2,command=self.forget)
        self.izlaz.pack(side="right",ipadx=50,ipady=5,padx=5,pady=5)
        self.total=tk.Label(self.donji_frame, text="Ukupna cena: ",font=cst.MAIN_FONT,bg="blue",fg="black",width=10,height=1)
        self.total.pack(anchor="center",ipadx=20,ipady=1,padx=5,pady=5)
        self.total_cena=tk.Entry(self.donji_frame, textvariable=self.cena_var, font=cst.MAIN_FONT,bg="gray",fg="black",width=11,state="readonly")
        self.total_cena.pack(anchor="center",ipadx=20,ipady=1,padx=5,pady=5)


        self.tree=ttk.Treeview(self.srednji_frame,columns=("Količina","Cena","Ukupna cena"))
        self.tree.heading("#0",text="Naziv proizvoda")
        self.tree.heading("#1",text="Količina")
        self.tree.column("#1",stretch=True)
        self.tree.heading("#2",text="Cena")
        self.tree.heading("#3",text="Ukupna cena")
        self.tree.pack(fill="both",expand="yes",)

        self.porudzbine=session.query(mdl.Porudzbine).all()
        
        
        for porudzbina in self.porudzbine:
            if porudzbina.broj_stola==self.sto:
                self.tree.insert("", "end", text=porudzbina.naziv_proizvoda,values=(porudzbina.kolicina,porudzbina.cena_proizvoda,porudzbina.ukupna_cena)) 

        Sto.zbir_cena(self)


    def naplata(self,broj):
        mdl.Porudzbine.brisanje_porudzbine(broj)
        self.forget()

    def refresh(self):
        self.destroy()
        self.__init__(self.master,self.sto)

    def zbir_cena(self):
        cene=[]
        for child in self.tree.get_children():
            cene.append(float(self.tree.item(child)["values"][2]))
        self.cena_var.set(sum(cene))


class Prodaja(tk.Frame):

    def __init__(self,master:tk.Frame,sto):
        super().__init__(master)
        width=self.winfo_screenwidth()
        height=self.winfo_screenheight()
        self.sto=sto
        self.pack(fill="both",expand=True)


        self.levi_frame=tk.Frame(self)
        self.desni_frame=tk.Frame(self)

        self.levi_frame.pack(side='left',fill="both")
        self.desni_frame.pack(side="right",fill="both",expand="yes")

        

        self.poruci=tk.Button(self.desni_frame, text="PORUČI", font=cst.MAIN_FONT,bg="green",fg="black",width=10,height=2,command=lambda: self.naruci(self.tree,))
        self.poruci.pack(anchor="se",side="bottom",ipadx=50,ipady=5,padx=5,pady=5)
        
       
        
        self.tree=ttk.Treeview(self.desni_frame,columns=("Količina","Cena","Ukupna cena"))
        self.tree.heading("#0",text="Naziv proizvoda")
        self.tree.heading("#1",text="Količina")
        self.tree.column("#1",stretch=True)
        self.tree.heading("#2",text="Cena")
        self.tree.heading("#3",text="Ukupna cena")
        self.tree.pack(fill="both",expand="yes",)
        proizvodi=session.query(mdl.Proizvodi).all()
        r=1
        c=0
        for proizvod in proizvodi:
            self.kreiraj_dugme(self.levi_frame,proizvod,r,c)
            c+=1
            if c==4:
                c=0
                r+=1

        

    

        

    def kreiraj_dugme(self,frame,proizvod:mdl.Proizvodi,r,c):
        dugme=tk.Button(frame,text=proizvod.naziv_proizvoda,font=cst.MAIN_FONT,fg="black",width=20,height=4,padx=5,justify='center',command=lambda:self.dodaj_proizvod(self.tree,proizvod.naziv_proizvoda,proizvod.cena_proizvoda))
        dugme.grid(row=r,column=c)

    def dodaj_proizvod(self,tree,naziv,cena):
        amount = 1
        for child in tree.get_children():
            if tree.item(child)["text"] == naziv:
                amount += int(tree.item(child)["values"][0])
                tree.delete(child)
        ukupna_c=cena*amount
        tree.insert("", "end", text=naziv, values=(amount,cena,ukupna_c))

    def naruci(self, tree):
        for child in tree.get_children():
            item = tree.item(child)
            name = item["text"]
            amount = item["values"][0]
            cena=item["values"][1]
            ukupna_c=item["values"][2]
            mdl.Porudzbine.dodavanje_porudzbine(self.sto,name,cena,amount,ukupna_c)
        self.forget()
        Sto.refresh(self.master)
        Sto.zbir_cena(self.master)

        