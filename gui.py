from tkinter import *
from tkinter import ttk
from datetime import datetime
from time import sleep
import csv
import pandas as pd

class InputDataWin:
    def __init__(self, dashboard):
        self.root = Tk()
        self.root.title("Data pasien")

        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(row=0, column=0, sticky=(N, E, W, S), padx=20)
        mainframe.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)

        ttk.Label(mainframe, text="Nama", width=7).grid(row=1, column=1, pady=5)
        ttk.Label(mainframe, text="Alamat", width=7).grid(row=2, column=1, pady=5)
        ttk.Label(mainframe, text="No.Telp", width=7).grid(row=3, column=1, pady="5 10")
        ttk.Label(mainframe, text="Dokter", width=7).grid(row=4, column=1)

        for i in range(1,5):
            ttk.Label(mainframe, text=": ").grid(row=i, column=2)
        
        self.nama = StringVar(mainframe)
        self.alamat = StringVar(mainframe)
        self.noTelp = StringVar(mainframe)
        self.dokter = StringVar(mainframe, "tulus")
        
        ttk.Entry(mainframe, width=28, textvariable=self.nama).grid(row=1, column=3,columnspan=3, sticky=W)
        ttk.Entry(mainframe, width=28, textvariable=self.alamat).grid(row=2, column=3,columnspan=3, sticky=W)
        ttk.Entry(mainframe, width=28, textvariable=self.noTelp).grid(row=3, column=3,columnspan=3, sticky=W)
        ttk.Radiobutton(mainframe, text="dr. Tulus", value="tulus", variable=self.dokter).grid(row=4, column=3, sticky=W)
        ttk.Radiobutton(mainframe, text="dr. Gisel", value="gisel", variable=self.dokter).grid(row=5, column=3,sticky=W)

        ttk.Button(mainframe, text="Submit", command=lambda: self.submit_data(mainframe, dashboard)).grid(row=4, column=5, rowspan=2)

    def submit_data(self,mainframe, dashboard, *args):
        drId = 0 if self.dokter.get() == "tulus" else 1
        isidata = [self.nama.get(), self.alamat.get(), self.noTelp.get()]

        if "" in isidata:
            warning_label = Label(mainframe, text="Jangan kosongkan data!", foreground="red")
            warning_label.grid(row=6, column=1, columnspan=6, sticky=N)
            warning_label.after(3000, lambda: warning_label.destroy())
            return

        with open("no_antre.txt", "r") as f:
            no_antre = list(map(int, f.read().split(',')))
            no_antre[drId] += 1
            with open("no_antre.txt", "w") as fwrite:
                fwrite.write(','.join(list(map(str, no_antre))))

        isidata.insert(0, no_antre[drId])
        isidata.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

        with open(f"data_antrean/{self.dokter.get()}.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(isidata)
        self.root.destroy()
        dashboard.refresh_table()
        
class Dashboard:
    def __init__(self):
        self.root = Tk()

        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(row=0, column=0, sticky="N E W S", padx=20)
        mainframe.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)

        s = ttk.Style()
        s.configure("topframe.TFrame", font=('helvetica', 32))
        topframe = ttk.Frame(mainframe, padding=5, border=5,relief="sunken")
        topframe.grid(row=0, column=0)
        ttk.Label(topframe, text="Dashboard Antrean", padding="85 5 85 5",font=("Times New Roman", 17, "bold")).grid(row=1, column=1)
        ttk.Button(topframe, text='+', width=3, command=self.get_data).grid(row=1,column=2)
        self.make_table(mainframe)
        self.refresh_table = lambda: self.make_table(mainframe)


    def get_data(self):
        input_win = InputDataWin(self)
        input_win.root.mainloop()


    def make_table(self, mainframe):
        botframe = ttk.Frame(mainframe, padding=5, border=5, relief="sunken")
        botframe.grid(row=1, column=0)

        tabel_tulus = ttk.Frame(botframe, border=5, relief=RAISED)
        tabel_tulus.grid(row=0, column=0)

        tabel_gisel = ttk.Frame(botframe, border=5, relief="raised")
        tabel_gisel.grid(row=0, column=1)

        data_tulus = pd.read_csv("data_antrean/tulus.csv") 
        data_gisel = pd.read_csv("data_antrean/gisel.csv")

        label_tulus = ttk.Label(tabel_tulus,text="dr. Tulus", font=("Times New Roman", 14, "bold"))
        label_tulus.grid(row=0, column=0, columnspan=2)

        label_gisel = ttk.Label(tabel_gisel,text="dr. Gisel", font=("Times New Roman", 14, "bold"))
        label_gisel.grid(row=0, column=0, columnspan=2)

        for i in range(10):
            # ============== Data Tulus ======================
            no_antrean_tulus = ttk.Entry(tabel_tulus, width=3, justify="center")
            nama_tulus = ttk.Entry(tabel_tulus, justify="center")

            no_antrean_tulus.grid(row=i+1, column=0)
            nama_tulus.grid(row=i+1, column=1)
            
            if len(data_tulus) <= i:
                no_antrean_tulus.insert(0, '')
                nama_tulus.insert(0, '')
            else:
                no_antrean_tulus.insert(0, data_tulus.iloc[i,0])
                nama_tulus.insert(0, data_tulus.iloc[i,1])
            # =============== Data Gisel =======================
            no_antrean_gisel = ttk.Entry(tabel_gisel, width=3, justify="center")
            nama_gisel = ttk.Entry(tabel_gisel, justify="center")

            no_antrean_gisel.grid(row=i+1, column=0)
            nama_gisel.grid(row=i+1, column=1)

            no_antrean_gisel.insert(0, '' if len(data_gisel) <= i else data_gisel.iloc[i, 0])
            nama_gisel.insert(0, '' if len(data_gisel) <= i else data_gisel.iloc[i, 1])
        
        ttk.Button(tabel_tulus, text='=>', command=None).grid(row=11,column=0, columnspan=2)
        ttk.Button(tabel_gisel, text='=>', command=None).grid(row=11,column=0, columnspan=2)

if __name__ == "__main__":
    dashboard_win = Dashboard()
    dashboard_win.root.mainloop()
# END MAIN
