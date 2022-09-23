
class Pasien:
    def __init__(self, data: list):
        self.data = data
    def masuk_csv(self):
        data_csv = ','.join(str(x) for x in self.data)
        with open("data_antrean.csv", 'a') as f:
            f.write(f"\n{data_csv}")

