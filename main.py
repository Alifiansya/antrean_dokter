import os
from art import *
from tabulate import tabulate
from time import sleep
import pandas as pd
from pasien import Pasien

if __name__ == "__main__":
    pasien = Pasien()
    while True:
        print("Data antrian dr.Samsudin: ")
        # Print table dari csv
        df1 = pd.read_csv("data_antrean/samsudin.csv")
        print(tabulate(df1, headers = 'keys', tablefmt = 'fancy_grid')) 

        print("Data antrian dr.Budi: ")
        # Print table dari csv
        df2 = pd.read_csv("data_antrean/budi.csv")
        print(tabulate(df2, headers = 'keys', tablefmt = 'fancy_grid')) 

        print("Data antrian dr.Supratman: ")
        # Print table dari csv
        df3 = pd.read_csv("data_antrean/supratman.csv")
        print(tabulate(df3, headers = 'keys', tablefmt = 'fancy_grid')) 

        match input("Apa yang ingin anda lakukan?: "):
            # Mengambil data dari console
            case "tambah data":
                pasien.ambil_data()
                pasien.masuk_csv()
            case "next":
                pass
            case default:
                print("coba lagi!")