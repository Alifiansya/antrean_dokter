from tkinter import *
from tkinter import ttk
from datetime import datetime
from time import sleep

# Impor library ini untuk yang ada hubungan sama csv
# Library csv untuk mindahin dari collection ke csv
# Library pandas untuk ngebaca csv terus dimasukin ke tabel
import csv
import pandas as pd

# Membuat class dashboard yang berisi tabel data antrean
# Dapat membuat instance dari objek InputDataWin dengan
# menekan button '+' pada bagian kanan atas

class Dashboard(Tk):
    # Di-derive dari class Tk agar dapat bisa langsung jadi window
    def __init__(self):
        super().__init__()
        self.title("Dashboard")

        # Menginisialisasikan theme dashboard menggunakan theme yg
        # sama di semua os
        self.style = ttk.Style()
        self.style.theme_use('classic')
        self.style.configure('.', background="#f0f0ed")


        # Container utama Dashboard
        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(row=0, column=0, sticky="N E W S", padx=20)
        mainframe.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)

        # Membuat top container yang berisi label dashboard dan button '+'
        topframe = ttk.Frame(mainframe, padding=5, relief="sunken")
        topframe.grid(row=0, column=0, sticky="news")
        ttk.Label(topframe, text="Dashboard Antrean", font=(
            "Times New Roman", 17, "bold")).grid(row=1, column=1, padx="51 27")
        ttk.Button(topframe, text='+', width=3,
                   command=self.get_data).grid(row=1, column=3)
        self.make_table(mainframe)
        # Ngebuat lambda function biar bisa ngerefresh dari window lain
        self.refresh_table = lambda: self.make_table(mainframe)

    # Fungsi buat instance objek InputDataWin
    def get_data(self):
        input_win = InputDataWin(self)
        input_win.mainloop()

    # Fungsi untuk membuat dan merefresh tabel (ngga bisa dipanggil langsung
    # dari window lain karena harus ngepass argumen mainframe dashboardnya 
    # yang cuma ada di constructor aja, makanya dibuatlah lambda function
    # di constructornya)
    def make_table(self, mainframe):
        # Membuat bot container
        botframe = ttk.Frame(mainframe, padding=5, border=5, relief="sunken")
        botframe.grid(row=1, column=0)

        # Membuat container untuk setiap tabel dr. Tulus & dr. Gisel
        tabel_tulus = ttk.Frame(botframe, border=5, relief=RAISED)
        tabel_tulus.grid(row=0, column=0)

        tabel_gisel = ttk.Frame(botframe, border=5, relief="raised")
        tabel_gisel.grid(row=0, column=1)

        # Membaca data dari csv setiap dokter
        data_tulus = pd.read_csv("data_antrean/tulus.csv")
        data_gisel = pd.read_csv("data_antrean/gisel.csv")

        # Membuat Label di row paling atas pada container/frame
        label_tulus = ttk.Label(tabel_tulus, text="dr. Tulus", font=(
            "Times New Roman", 14, "bold"))
        label_tulus.grid(row=0, column=0, columnspan=2)

        label_gisel = ttk.Label(tabel_gisel, text="dr. Gisel", font=(
            "Times New Roman", 14, "bold"))
        label_gisel.grid(row=0, column=0, columnspan=2)

        # Melakukan pembuatan tabel
        for i in range(10):
            # ============== Data Tulus ======================
            no_antrean_tulus = ttk.Entry(
                tabel_tulus, width=3, justify="center")
            nama_tulus = ttk.Entry(tabel_tulus, justify="center")

            no_antrean_tulus.grid(row=i+1, column=0)
            nama_tulus.grid(row=i+1, column=1)

            # Kalau besar i sudah samadengan atau lebih besar dari
            # banyak row pada dataframe, maka akan memasukkan empty
            # string pada tabel
            if len(data_tulus) <= i:
                no_antrean_tulus.insert(0, '')
                nama_tulus.insert(0, '')
            else:
                no_antrean_tulus.insert(0, data_tulus.iloc[i, 0])
                nama_tulus.insert(0, data_tulus.iloc[i, 1])
            # =============== Data Gisel =======================
            no_antrean_gisel = ttk.Entry(
                tabel_gisel, width=3, justify="center")
            nama_gisel = ttk.Entry(tabel_gisel, justify="center")

            no_antrean_gisel.grid(row=i+1, column=0)
            nama_gisel.grid(row=i+1, column=1)

            # Sebenernya sama aja untuk nanganin index yang lebih
            # besar, cuma beda gaya doang
            no_antrean_gisel.insert(0, '' if len(
                data_gisel) <= i else data_gisel.iloc[i, 0])
            nama_gisel.insert(0, '' if len(data_gisel) <=
                              i else data_gisel.iloc[i, 1])

        # Membuat button next untuk setiap tabel, melakukan 
        # dequeue (NOT IMPLEMENTED)
        ttk.Button(tabel_tulus, text='=>', command=None).grid(
            row=11, column=0, columnspan=2)
        ttk.Button(tabel_gisel, text='=>', command=None).grid(
            row=11, column=0, columnspan=2)

# Membuat class untuk window input
# bakal di-inisialisasi pas pencet tombol '+' di dashboard
class InputDataWin(Tk):
    # Ini untuk ngebuat windownya
    def __init__(self, dashboard):
        # root window dimasukin ke self biar bisa manggil mainloop
        super().__init__()
        self.title("Data pasien")

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





