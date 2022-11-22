from tkinter import *
from tkinter import ttk

class DequeueNotification(Tk):
    def __init__(self, data_pasien : list):
        super().__init__()
        self.data_pasien = data_pasien
        self.title("Notifikasi")
        self.resizable(False, False)
        self.create_mainframe()
        self.add_style()
        self.create_nomor()
        self.create_tulisan()
        self.after(3000, self.destroy)
    
    def create_mainframe(self):
        self.mainframe = ttk.Frame(self, padding=10)
        self.mainframe.grid(row=0, column=0, sticky="news",padx=10, pady=10)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
    
    def create_nomor(self):
        no_container = ttk.Frame(self.mainframe)
        no_container.grid(row=0, column=0, sticky=W)
        ttk.Label(no_container, text="21", font=("Times New Roman", 32, "bold"),padding=20, style="Nomor.TLabel").pack(padx=10)
    
    def create_tulisan(self):
        tulisan_container = ttk.Frame(self.mainframe, padding=10)
        tulisan_container.grid(row=0, column=1, sticky=E)
        ttk.Label(tulisan_container, text="Atas nama", font=("Times New Roman", 16)).pack()
        ttk.Label(tulisan_container, text=f"{self.data_pasien[1]}", font=("Times New Roman", 16, "bold")).pack()
        ttk.Label(tulisan_container, text=f"Silahkan ke dr. {self.data_pasien[2]}", font=("Times New Roman", 16)).pack()
    
    def add_style(self):
        style = ttk.Style(self)
        style.configure('.', background="#FFFFFF")
        style.configure('Nomor.TLabel', background="#8d8daa")



if __name__ == "__main__":
    DequeueNotification([2, "daiod", "tulus"]).mainloop()

        