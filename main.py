from art import *
from tabulate import tabulate
from time import sleep
import pandas as pd
import pasien as ps

if __name__ == "__main__":
    while True:
        print("Data antrian: ")
        # Print table dari csv
        df = pd.read_csv("data_antrean.csv")
        print(tabulate(df, headers = 'keys', tablefmt = 'fancy_grid')) 
        match input("Apa yang ingin anda lakukan?: "):
            # Mengambil data dari console
            case "tambah data":
                data = ['nama', 'Nomor Handphone']
                for i in range(len(data)):
                    data[i] = input(f"Masukan {data[i]}")
                print("Nama Dokter yang tersedia: ")
                dr = ["dr.Supratman", "dr.Budi", "dr.Samsudin"]
                for i in range(len(dr)):
                    print(f"{i+1}. {dr[i]}")
                data.append(dr[int(input("Pilih dokter yang akan ditemui: ")) - 1])
                if df.empty:
                    data.insert(0, 1)
                else: 
                    # Mengambil id data terakhir di csv
                    data.insert(0, int(df.iloc[-1][0])+1)
                pasien = ps.Pasien(data)
                pasien.masuk_csv()
            case "next":
                data_front = list(df.iloc[0])
                print("\n")
                print(text2art(f"{data_front[0]}", font="block", chr_ignore=False))
                sleep(10)
                print("\n")
                df = df[df.index != 0]
                df.to_csv("data_antrean.csv", index=False)
            case default:
                print("coba lagi!")