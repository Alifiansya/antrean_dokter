import json, csv

with open("dokter.json") as f:
    dokter = json.load(f)
nama_dokter = [x['nama'] for x in dokter]

class Pasien:
    def __init__(self) -> None:
        pass
    def ambil_data(self):
        self.nama = input("Masukan nama: ")
        self.hp = input("Masukan Nomor HP: ")
        print(
            "Dokter yang ada:\n",
            "1. Dr.Samsudin\n",
            "2. Dr.Supratman\n",
            "3. Dr.Budi"
        )
        dokter_pilihan = input("Pilih nomor dokter yang ada: ")
        self.drID = int(dokter_pilihan) - 1
        
    def masuk_csv(self):
        with open("nomor_antre.txt", 'r') as f:
            data = f.read().split(',')
            print(data)
            data[self.drID] = int(data[self.drID]) + 1
            self.no_antre = data[self.drID]
            data[self.drID] = str(data[self.drID])
            with open("nomor_antre.txt", 'w', newline='') as file:
                file.write(','.join(data))

        with open(f"data_antrean/{nama_dokter[self.drID][3:].lower()}.csv", 'a') as f:
            data_csv = ','.join([str(self.no_antre), self.nama])
            f.write(f"\n{data_csv}")
        
    