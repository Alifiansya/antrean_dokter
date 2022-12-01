from tkinter import *
from tkinter import ttk
from input_win import InputDataWin
from notif import DequeueNotification
import pandas as pd

class Dashboard(Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard")
        self.resizable(False, False)
        self.style = ttk.Style(self)
        self.style.configure('.', background="#f0f0ed")

        mainframe = ttk.Frame(self, padding=5)
        mainframe.grid(row=0, column=0, sticky="N E W S", padx=20)
        mainframe.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)

        topframe = ttk.Frame(mainframe, padding=5, border=5,relief="sunken")
        topframe.grid(row=0, column=0, sticky="news")
    
        ttk.Label(topframe, text="Dashboard Antrean", font=(
            "Times New Roman", 21, "bold")).pack(side=LEFT)
        ttk.Button(topframe, text='+', width=3,
                   command=self.get_data).pack(side=RIGHT)
        self.make_table(mainframe)
        self.refresh_table = lambda: self.make_table(mainframe)

    def get_data(self):
        self.input_win = InputDataWin(self)
        self.input_win.mainloop()

    def make_table(self, mainframe):
        botframe = ttk.Frame(mainframe, padding=5, border=5, relief="sunken")
        botframe.grid(row=1, column=0)

        tabel_tulus = ttk.Frame(botframe, border=5, relief=RAISED)
        tabel_tulus.grid(row=0, column=0)

        tabel_gisel = ttk.Frame(botframe, border=5, relief="raised")
        tabel_gisel.grid(row=0, column=1)

        data_tulus = pd.read_csv("data_antrean/tulus.csv")
        data_gisel = pd.read_csv("data_antrean/gisel.csv")

        label_tulus = ttk.Label(tabel_tulus, text="dr. Tulus", font=("Times New Roman", 14, "bold"))
        label_tulus.grid(row=0, column=0, columnspan=2)

        label_gisel = ttk.Label(tabel_gisel, text="dr. Gisel", font=("Times New Roman", 14, "bold"))
        label_gisel.grid(row=0, column=0, columnspan=2)

        for i in range(10):
            no_antrean_tulus = ttk.Entry(tabel_tulus, width=3, justify="center")
            nama_tulus = ttk.Entry(tabel_tulus, justify="center")

            no_antrean_tulus.grid(row=i+1, column=0)
            nama_tulus.grid(row=i+1, column=1)

            if len(data_tulus) <= i:
                no_antrean_tulus.insert(0, '')
                nama_tulus.insert(0, '')
            else:
                no_antrean_tulus.insert(0, data_tulus.iloc[i, 0])
                nama_tulus.insert(0, data_tulus.iloc[i, 1])
            no_antrean_gisel = ttk.Entry(tabel_gisel, width=3, justify="center")
            nama_gisel = ttk.Entry(tabel_gisel, justify="center")

            no_antrean_gisel.grid(row=i+1, column=0)
            nama_gisel.grid(row=i+1, column=1)

            no_antrean_gisel.insert(0, '' if len(data_gisel) <= i else data_gisel.iloc[i, 0])
            nama_gisel.insert(0, '' if len(data_gisel) <= i else data_gisel.iloc[i, 1])

        ttk.Button(tabel_tulus, text='=>', command=lambda: self.dq_table(0)).grid(row=11, column=0, columnspan=2)
        ttk.Button(tabel_gisel, text='=>', command=lambda: self.dq_table(1)).grid(row=11, column=0, columnspan=2)
    
    def dq_table(self, id):
        dr = "tulus" if not id else "gisel"
        csv_data = pd.read_csv(f"data_antrean/{dr}.csv")
        if csv_data.empty:
            return
        pass_data = csv_data.iloc[0, :].values.tolist()
        csv_data = csv_data.iloc[1:, :]
        csv_data.to_csv(f"data_antrean/{dr}.csv", index=False)
        pass_data = [pass_data[0], pass_data[1], dr]
        DequeueNotification(self, pass_data)
        self.refresh_table()