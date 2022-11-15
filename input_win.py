from tkinter import *
from tkinter import ttk
from datetime import datetime
import csv

# Membuat class untuk window input
# bakal di-inisialisasi pas pencet tombol '+' di dashboard
class InputDataWin(Tk):
    # Ini untuk ngebuat windownya
    def __init__(self, dashboard):
        # root window dimasukin ke self biar bisa manggil mainloop
        super().__init__()
        self.title("Data pasien")
        self.resizable(False, False)
        
        self.style = ttk.Style(self)
        self.style.theme_use('classic')
        self.style.configure('.', background="#f0f0ed")
        

        # Container utama
        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(row=0, column=0, sticky=(N, E, W, S), padx=20)
        mainframe.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)

        # Ini buat ngebuat widget label tulisan data yang harus dimasukin
        ttk.Label(mainframe, text="Nama", width=7).grid(
            row=1, column=1, pady=5)
        ttk.Label(mainframe, text="Alamat", width=7).grid(
            row=2, column=1, pady=5)
        ttk.Label(mainframe, text="No.Telp", width=7).grid(
            row=3, column=1, pady="5 10")
        ttk.Label(mainframe, text="Dokter", width=7).grid(row=4, column=1)

        # Biar titik-dua nya sejajar pake ini
        for i in range(1, 5):
            ttk.Label(mainframe, text=": ").grid(row=i, column=2)

        # Buat variabel yang bakal dimasukin ke collection
        self.nama = StringVar(mainframe)
        self.alamat = StringVar(mainframe)
        self.noTelp = StringVar(mainframe)
        self.dokter = StringVar(mainframe, "tulus")

        # Buat widget yang inputnya masuk ke variabel diatas
        ttk.Entry(mainframe, width=28, textvariable=self.nama).grid(
            row=1, column=3, columnspan=3, sticky=W)
        ttk.Entry(mainframe, width=28, textvariable=self.alamat).grid(
            row=2, column=3, columnspan=3, sticky=W)
        ttk.Entry(mainframe, width=28, textvariable=self.noTelp).grid(
            row=3, column=3, columnspan=3, sticky=W)
        ttk.Radiobutton(mainframe, text="dr. Tulus", value="tulus",
                        variable=self.dokter).grid(row=4, column=3, sticky=W)
        ttk.Radiobutton(mainframe, text="dr. Gisel", value="gisel",
                        variable=self.dokter).grid(row=5, column=3, sticky=W)

        # Pastiin data udah terisi semua, baru bisa pindahin data ke csv pake
        # button ini
        ttk.Button(mainframe, text="Submit", command=lambda: self.submit_data(
            mainframe, dashboard)).grid(row=4, column=5, rowspan=2)

    # Fungsi yang dipanggil pas submit data
    def submit_data(self, mainframe, dashboard, *args):
        # Ngebuat Collection (list) dari data entry/radiobutton
        drId = 0 if self.dokter.get() == "tulus" else 1
        isidata = [self.nama.get(), self.alamat.get(), self.noTelp.get()]

        # Melakukan pengecekkan apabila ada data kosong bakal keluar 
        # label warning
        if "" in isidata:
            warning_label = Label(
                mainframe, text="Jangan kosongkan data!", foreground="red")
            warning_label.grid(row=6, column=1, columnspan=6, sticky=N)
            warning_label.after(3000, lambda: warning_label.destroy())
            return

        # Melakukan increment pada nomor antrean yang ada pada file txt
        # dan pada list
        with open("no_antre.txt", "r") as f:
            no_antre = list(map(int, f.read().split(',')))
            no_antre[drId] += 1
            with open("no_antre.txt", "w") as fwrite:
                fwrite.write(','.join(list(map(str, no_antre))))

        # Memasukkan data no_antre pada index paling depan dan memasukkan
        # waktu men-submit data pada index paling belakang
        isidata.insert(0, no_antre[drId])
        isidata.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

        # Pindahin data dari list ke csv
        with open(f"data_antrean/{self.dokter.get()}.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(isidata)
        
        # Menghilangkan window dan merefresh tabel pada dashboard
        self.destroy()
        dashboard.refresh_table()