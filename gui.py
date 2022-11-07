from tkinter import *
from tkinter import ttk
from datetime import datetime
from time import sleep
import csv

class InputDataWin:
    def __init__(self):
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
        
        self.nama = StringVar()
        self.alamat = StringVar()
        self.noTelp = StringVar()
        self.dokter = StringVar(None, "tulus")
        
        ttk.Entry(mainframe, width=28, textvariable=self.nama).grid(row=1, column=3,columnspan=3, sticky=W)
        ttk.Entry(mainframe, width=28, textvariable=self.alamat).grid(row=2, column=3,columnspan=3, sticky=W)
        ttk.Entry(mainframe, width=28, textvariable=self.noTelp).grid(row=3, column=3,columnspan=3, sticky=W)
        ttk.Radiobutton(mainframe, text="dr. Tulus", value="tulus", variable=self.dokter).grid(row=4, column=3, sticky=W)
        ttk.Radiobutton(mainframe, text="dr. Gisel", value="gisel", variable=self.dokter).grid(row=5, column=3,sticky=W)

        ttk.Button(mainframe, text="Submit", command=lambda: self.submit_data(mainframe)).grid(row=4, column=5, rowspan=2)

    def submit_data(self,mainframe, *args):
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
        ttk.Button(topframe, text='+', width=3).grid(row=1,column=2)

        botframe = ttk.Frame(mainframe, padding=5, border=5, relief="sunken")
        botframe.grid(row=1, column=0)

        tabel_tulus = ttk.Frame(botframe, border=5, relief=RAISED)
        tabel_tulus.grid(row=0, column=0)

        tabel_gisel = ttk.Frame(botframe, border=5, relief="raised")
        tabel_gisel.grid(row=0, column=1)


        for i in range(10):
            datarow = ttk.Entry(tabel_tulus, width=3, justify="center")
            datarow.insert(0, str(i+1))
            datarow.grid(row=i, column=0)
            namerow = ttk.Entry(tabel_tulus, justify="center")
            namerow.insert(0, "LoremIpsum")
            namerow.grid(row=i, column=1)

        for i in range(10):
            datarow = ttk.Entry(tabel_gisel, width=3, justify="center")
            datarow.insert(0, str(i+1))
            datarow.grid(row=i, column=0)
            namerow = ttk.Entry(tabel_gisel, justify="center")
            namerow.insert(0, "LoremIpsum")
            namerow.grid(row=i, column=1)
        



if __name__ == "__main__":
    dashboard_win = Dashboard()
    dashboard_win.root.mainloop()
# END MAIN
