from gui import *
import csv
import os


"""
    Projek Akhir praktikum Pemrograman Lanjut
    Muhammad Hilmi Alfaris (NIM 205150301111023)
    Muhammad Alifiansyah Firdaus (NIM 215150307111025)

    Deskripsi Program:
    • Sebuah Klinik membutuhkan system antrean untuk pemeriksaan 
      dokter(GUI), dimana system tersebut memiliki menu sebagai 
      berikut:
        1. Dashboard urutan antrean dokter
        2. Tambah Data
        3. Next 
    • Pada awal program akan menampilkan tampilan pada menu 
      nomor 1 dimana nantinya dashboard itu digunakan untuk 
      menampilkan nama pasien yang ingin berobat.
    • Jika user memilih nomor 1, kemudian tampilkan menu berikut.
        1. Mengisi identitas pasien seperti nama nomor telepon dan lain-lain nya
        2. Memilih dokter mana yang ingin di kunjungi
        3. Nama sudah muncul di dalam menu utama dashboard antrean
        4. Kembali ke menu utama dashboard antrean
    • Ketentuan atau prosedur pada program tersebut adalah
    1. Sebelum memasuki kedalam ruangan dokter, user diminta untuk 
       melakukan pengisian data berupa Nama, No. HP, dan Dokter  
       Pilihan agar mendapatkan nomer antrean.
    2. Jika menu next ditekan maka akan menampilkan sebuah popup yang 
       berisikan silahkan pasien dengan nama untuk memasukin ruangan dokter.
"""

# Cuma buat ngeluarin window dashboardnya doang
if __name__ == "__main__":
    dashboard_win = Dashboard()
    dashboard_win.root.mainloop()