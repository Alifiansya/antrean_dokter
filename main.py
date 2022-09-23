import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data_antrean.csv")
    if df.empty:
        header = pd.DataFrame(["id", "nama", "no_hp", "dokter"])
        df.to_csv("data_antrean.csv", index=False, mode='a')
    