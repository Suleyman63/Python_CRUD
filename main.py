from tkinter import *
from tkinter import messagebox, ttk
import random
from tkinter.font import BOLD
import data
import sqlite3
from tkcalendar import Calendar, DateEntry
import tempfile, os
from fpdf import FPDF


randomnum1 = random.randrange(26000,27000,20)

randomnum2 = random.choice(['plaka1','plaka2','plaka3','plaka4','plaka5', 'plaka6', 'plaka7', 'plaka8','plaka9','plaka10'])


class Urunler:
    def __init__(self, root):
        self.root=root
        self.root.title('MANAGEMENT SYSTEM')
        self.root.geometry('1790x800+0+0')


        self.firmaadi = StringVar()
        self.adres = StringVar()
        self.tarih = StringVar()
        self.tarih2 = StringVar()
        self.urunadi = StringVar()
        self.miktar = StringVar()
        self.plaka = StringVar()  
        self.numara = StringVar()
        self.aciklama = StringVar()


        self.top=Label(self.root, text='MANAGEMENT SYSTEM', font=('arial', 20), bg='#164A58', fg='white', pady=10)
        self.top.place(x=0, y=0, relwidth=1)

        self.leftframe = Frame(self.root, bg='#164A58')
        self.leftframe.place(x=10, y=64, width=450, height=750)


########################## LABEL ######################################

        self.l1 = Label(self.leftframe, text='Firma adi', font=('arial', 14), bg='#164A58', fg='white')
        self.l1.place(x=30, y=80) 

        self.l2 = Label(self.leftframe, text='Teslim adresi', font=('arial', 14), bg='#164A58', fg='white')
        self.l2.place(x=30, y=130)

        self.l3 = Label(self.leftframe, text='Tarih', font=('arial', 14), bg='#164A58', fg='white')
        self.l3.place(x=30, y=180)

        self.l4 = Label(self.leftframe, text='Tarih2', font=('arial', 14), bg='#164A58', fg='white')
        self.l4.place(x=30, y=230)

        self.l5 = Label(self.leftframe, text='Urun Adi', font=('arial', 14), bg='#164A58', fg='white')
        self.l5.place(x=30, y=280)

        self.l6 = Label(self.leftframe, text='Miktar', font=('arial', 14), bg='#164A58', fg='white', pady=10)
        self.l6.place(x=30, y=330)

        self.l7 = Label(self.leftframe, text='Plaka', font=('arial', 14), bg='#164A58', fg='white', pady=10)
        self.l7.place(x=30, y=380)

        self.l8 = Label(self.leftframe, text='No', font=('arial', 14), bg='#164A58', fg='white', pady=10)
        self.l8.place(x=30, y=430)
        
        self.l9 = Label(self.leftframe, text='Aciklama', font=('arial', 14), bg='#164A58', fg='white', pady=10)
        self.l9.place(x=30, y=480)
        
        
        ########################## ENTRY ######################################
        
        self.e1 =ttk.Combobox(self.leftframe, textvariable=self.firmaadi, font=('arial', 14))
        self.e1['values'] = ('Male', 'Female')
        self.e1.config(width=30)
        self.e1.current(0)
        self.e1.place(x=150, y=80, width=260)


        self.e2 =ttk.Combobox(self.leftframe, textvariable=self.adres, font=('arial', 14))
        self.e2['values'] = ('A', 'B', 'C', 'D')
        self.e2.config(width=30)
        self.e2.current(0)
        self.e2.place(x=150, y=130, width=260)
        
        
        self.e3 =DateEntry(self.leftframe, textvariable=self.tarih, font=('arial', 14))
        self.e3.place(x=150, y=180, width=260)
        
        self.e4 =DateEntry(self.leftframe, textvariable=self.tarih2, font=('arial', 14))
        self.e4.place(x=150, y=230, width=260)
        
        
        self.e5 =Entry(self.leftframe, textvariable=self.urunadi, font=('arial', 14))
        self.e5.place(x=150, y=280, width=260)
        
        
        self.e6 =Entry(self.leftframe, textvariable=self.miktar, font=('arial', 14))
        self.e6.place(x=150, y=330, width=260)
        self.e6.insert(END, str(randomnum1))
        
        

        self.e7 =Entry(self.leftframe, textvariable=self.plaka, font=('arial', 14))
        self.e7.place(x=150, y=380, width=260)
        self.e7.insert(END, str(randomnum2))
        
        
        self.e8 =Entry(self.leftframe, textvariable=self.numara, font=('arial', 14))
        self.e8.place(x=150, y=430, width=260)
        
        
        self.e9 =Entry(self.leftframe, textvariable=self.aciklama, font=('arial', 14))
        self.e9.place(x=150, y=480, width=260, height=40)
        
        
        ################################  BUTTON ##################################

        self.b1 = Button(self.leftframe, command=self.ekle,  text='EKLE', font=('arial', 14, BOLD), bg="white", fg="red", pady=7, width=10, activebackground='brown')
        self.b1.place(x=30, y=600)

        self.b2 = Button(self.leftframe, command=self.guncelle,  text='GUNCELLE', font=('arial', 14, BOLD), bg="white", fg='red', pady=7, width=10, activebackground='brown')
        self.b2.place(x=180, y=600)

        self.b3 = Button(self.leftframe, command=self.sil, text='SIL', font=('arial', 14, BOLD), bg="white", fg='red', pady=7, width=10, activebackground='brown')
        self.b3.place(x=320, y=600)

        self.b4 = Button(self.leftframe, command=self.temizle,  text='TEMIZLE', font=('arial', 14, BOLD), bg='white', fg='red', pady=7, width=10, activebackground='brown')
        self.b4.place(x=30, y=680)

        self.b5 = Button(self.leftframe, command=self.listele, text='TUM KAYITLAR', font=('arial', 14, BOLD), bg="white", fg='red', pady=7, width=10, activebackground='brown')
        self.b5.place(x=180, y=680)

        self.b6 = Button(self.leftframe, command=self.cikis,  text='CIKIS', font=('arial', 14, BOLD), bg="white", fg='red', pady=7, width=10, activebackground='brown')
        self.b6.place(x=320, y=680)


############################ TABLE HEADER #########################################################

        self.table = Frame(self.root, bg='#164A58')
        self.table.place(x=430, y=64, width=1350, height=760)
        

        self.tableframe = Frame(self.table)
        self.tableframe.place(x=25, y=60, width=1300, height=670)

            ### search button ######
        self.b7 = Button(self.table, command=self.ara, text='ARA', pady=4, font=('arial', 14, BOLD), bg='white', fg='red', width=7, activebackground='brown')
        self.b7.place(x=1100, y=15)
        
        self.b8 = Button(self.table, command=self.yazdir, text='yazdir', pady=4, font=('arial', 14, BOLD), bg='white', fg='red', width=7, activebackground='brown')
        self.b8.place(x=1200, y=15)

            ### search entry #####
        self.e10 =Entry(self.table, textvariable=self.numara, font=('arial', 12))
        self.e10.place(x=850, y=16, height=35, width=250)
        
        
        ############################# TABLE DETAILS #################################################
        style = ttk.Style()
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 14,'bold')) 
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 

        self.scrollx = Scrollbar(self.table, orient=HORIZONTAL)
        self.scrolly = Scrollbar(self.table, orient=VERTICAL)
        
        self.Studenttable = ttk.Treeview(self.tableframe, columns=('id', 'firmaadi', 'adres', 'tarih', 'tarih2', 'urunadi', 'miktar', 'plaka', 'numara', 'aciklama'), \
        xscrollcommand=self.scrollx.set, yscrollcommand=self.scrolly.set)
        
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.scrolly.pack(side=RIGHT, fill=Y)

        self.scrollx.config(command=self.Studenttable.xview)
        self.scrolly.config(command=self.Studenttable.yview)


        self.Studenttable.heading("id", text="ID")
        self.Studenttable.heading('firmaadi', text='FIRMA ADI')
        self.Studenttable.heading('adres', text='TESLIM ADRESI')
        self.Studenttable.heading('tarih', text='TARIH')
        self.Studenttable.heading('tarih2', text='TARIH2')
        self.Studenttable.heading('urunadi', text='URUN ADI')
        self.Studenttable.heading('miktar', text='MIKTAR')
        self.Studenttable.heading('plaka', text='PLAKA')
        self.Studenttable.heading('numara', text='NO')
        self.Studenttable.heading('aciklama', text='ACIKLAMA')


        self.Studenttable.column("id", width=40, anchor=CENTER)
        self.Studenttable.column('firmaadi', width=200, anchor=CENTER)
        self.Studenttable.column('adres', width=200, anchor=CENTER)
        self.Studenttable.column('tarih', width=120, anchor=CENTER)
        self.Studenttable.column('tarih2', width=120, anchor=CENTER)
        self.Studenttable.column('urunadi', width=120, anchor=CENTER)
        self.Studenttable.column('miktar', width=120, anchor=CENTER)
        self.Studenttable.column('plaka', width=120, anchor=CENTER)
        self.Studenttable.column('numara', width=60, anchor=CENTER)
        self.Studenttable.column('aciklama', width=250, anchor=CENTER)
        


        self.Studenttable['show'] ='headings'
        self.Studenttable.pack(fill=BOTH, expand=1)
        self.Studenttable.bind('<ButtonRelease>', self.getrecord)
        self.listele()
        
        #############################################
        
        
    def ekle(self):
                    
                        connection = sqlite3.connect('urunler.db')
                        cursor = connection.cursor()
                        q="INSERT INTO urunler VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)" 
                        cursor.execute(q,(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), self.e6.get(), self.e7.get(), self.e8.get(), self.e9.get()))
                        connection.commit()
                        
                        self.e1.current(0),
                        self.e2.current(0),
                        self.e3.delete(0, END),
                        self.e4.delete(0, END),
                        self.e5.delete(0, END),
                        self.e6.delete(0, END),
                        self.e6.insert(END, str(randomnum1)),
                        self.e7.delete(0, END),
                        self.e7.insert(END, str(randomnum2)),
                        self.e8.delete(0, END),
                        self.e9.delete(0,END)
                        self.listele()
                        self.temizle()
                        connection.close()

                        
                        
    def temizle(self):
            self.e1.current(0),
            self.e2.current(0),
            self.e3.delete(0,END),
            self.e4.delete(0, END),
            self.e5.delete(0, END),
            self.e6.delete(0, END),
            self.e6.insert(END, str(randomnum1)),
            self.e7.delete(0, END),
            self.e7.insert(END, str(randomnum2)),
            self.e8.delete(0, END),
            self.e9.delete(1.0,END)
                        
                        
                        
    def listele(self):
            connection = sqlite3.connect('urunler.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM urunler")
            rows = cursor.fetchall()
            self.Studenttable.delete(*self.Studenttable.get_children())
            for row in rows:
                singlerow = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], [9]]
                self.Studenttable.insert("",END,values=singlerow)
            connection.commit()
            connection.close() 
            
            
            
    def getrecord(self, event):
        copy = self.Studenttable.focus()
        content = self.Studenttable.item(copy)
        row = content['values']
        if (len(row) !=0):
          self.e1.delete(0,END)
          self.e1.insert(END,row[1])
          self.e2.delete(0,END)
          self.e2.insert(END,row[2])
          self.e3.delete(0,END)
          self.e3.insert(END,row[3])
          self.e4.delete(0,END)
          self.e4.insert(END,row[4])
          self.e5.delete(0,END)
          self.e5.insert(END,row[5])
          self.e6.delete(0,END)
          self.e6.insert(END,row[6])
          self.e7.delete(0,END)
          self.e7.insert(END,row[7])
          self.e8.delete(0, END)
          self.e8.insert(END,row[8])
          self.e9.delete(1.0,END)
          self.e9.insert(END,row[9])         
        
    
    
    def sil(self):
                connection = sqlite3.connect("urunler.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM urunler where numara=?", (self.numara.get(),))       
                connection.commit()
                messagebox.showerror("silindi")
                self.listele()
                self.temizle()
                connection.close()
                
                
    
    def guncelle(self):
                    connection = sqlite3.connect("urunler.db")
                    cursor = connection.cursor()          
                    cursor.execute("UPDATE urunler SET firmaadi=?,adres=?,tarih=?,tarih2=?,urunadi=?,miktar=?,plaka=?, \
                        aciklama=? where numara=?",
                        (self.firmaadi.get(), self.adres.get(), self.tarih.get(), self.tarih2.get(),  self.urunadi.get(),  
                        self.miktar.get(), self.plaka.get(), self.aciklama.get(), self.numara.get()))
                    connection.commit()
                    messagebox.showerror("guncellendi")
                    self.listele()
                    self.temizle()
                    connection.close()
            
            
            
    def ara(self):
            connection = sqlite3.connect('urunler.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM urunler WHERE numara = ?", [self.e8.get()])
            rows = cursor.fetchall()
            if(len(rows)!=0):
                self.Studenttable.delete(*self.Studenttable.get_children())
                for row in rows:
                    self.Studenttable.insert('',END,values=row)
            connection.commit()
            connection.close()     

        

    def cikis(self):
            message = messagebox.askyesno("cikmak istediginden emin misin?")
            if message > 0:
                root.destroy()
            return 
        
        
    def yazdir(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(7, 20, self.e1.get())
        pdf.cell(7, 35, self.e2.get())
        pdf.cell(7, 50, self.e3.get())
        pdf.cell(7, 65, self.e4.get())
        pdf.cell(7, 80, self.e5.get())
        pdf.cell(7, 95, self.e6.get())
        pdf.cell(7, 110, self.e7.get())
        pdf.cell(7, 130, self.e8.get())
        pdf.cell(7, 145, self.e9.get())
        pdf.output('xxx.pdf', 'F')
        


if __name__=='__main__':
    root=Tk()
    obj = Urunler(root)
    root.mainloop()