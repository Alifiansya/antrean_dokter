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
        query = input("Apa yang ingin anda lakukan?: ")
        match query:
            # Mengambil data dari console
            case "tambah data":
                pasien.ambil_data()
                pasien.masuk_csv()
            case "next samsudin":
                df = pd.read_csv("data_antrean/samsudin.csv")
                df = df.iloc[1:, :]
                print(df)
                df.to_csv('data_antrean/samsudin.csv', index=False)
                
            case "next budi":
                df = pd.read_csv("data_antrean/budi.csv")
                df = df.iloc[1:, :]
                print(df)
                df.to_csv('data_antrean/budi.csv', index=False)
            case "next supratman":
                df = pd.read_csv("data_antrean/supratman.csv")
                df = df.iloc[1:, :]
                print(df)
                df.to_csv('data_antrean/supratman.csv', index=False)
            case default:
                print("coba lagi!")