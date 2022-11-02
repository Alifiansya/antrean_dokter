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

if __name__ == "__main__":
    inputWin = InputDataWin()
    inputWin.root.mainloop()
# END MAIN
