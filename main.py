import os
from tabulate import tabulate
from time import sleep
import pandas as pd
from pasien import Pasien

def tampil_next(data_awal, dokter):
    print(f"\nNomor antrean {data_awal[0]}")
    print(f"Atas nama {data_awal[1]}")
    print(f"Silahkan ke {dokter}\n")
    sleep(3)

if __name__ == "__main__":
    pasien = Pasien()
    while True:
        print("Data antrian dr.Tulus: ")
        # Print table dari csv
        df1 = pd.read_csv("data_antrean/tulus.csv")
        print(tabulate(df1, headers = 'keys', tablefmt = 'fancy_grid')) 

        print("Data antrian dr.Gisel: ")
        # Print table dari csv
        df2 = pd.read_csv("data_antrean/gisel.csv")
        print(tabulate(df2, headers = 'keys', tablefmt = 'fancy_grid')) 

        query = input("Apa yang ingin anda lakukan?: ").lower().lstrip().rstrip()
        match query:
            # Mengambil data dari console
            case "tambah data":
                pasien.ambil_data()
                pasien.masuk_csv()
            case "next tulus":
                df = pd.read_csv("data_antrean/tulus.csv")
                tampil_next(df.iloc[0][:].to_list(), "dr. Tulus")
                df = df.iloc[1:, :]
                df.to_csv('data_antrean/tulus.csv', index=False)
            case "next gisel":
                df = pd.read_csv("data_antrean/gisel.csv")
                df = df.iloc[1:, :]
                df.to_csv('data_antrean/gisel.csv', index=False)
            case default:
                print("coba lagi!")
