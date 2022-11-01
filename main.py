import csv
import os

path = [
    './tulus.csv',
    './gisel.csv'
]

fieldnames = (
    'no_antre',
    'nama',
    'alamat',
    'no_hp'
)

def get_data():
    data = dict()
    for x in fieldnames[1:]:
        data.update({x: input("Masukkan " + x + ': ')} )
    data.update({'dr': input('pilih dokter konsultasi dr. (tulus / gisel): ')})
    return data

if __name__ == "__main__":
    while True:
        data = get_data()
        csv_path = data['dr'] + '.csv'
        data.pop('dr')
        if not os.path.exists(csv_path):
            with open(csv_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(fieldnames)
        
        with open(csv_path, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames) 
            writer.writerow(data)