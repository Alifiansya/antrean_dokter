from time import sleep
from tkinter import *
from tkinter import ttk


class InputDataWin:
    def __init__(self):
        self.root = Tk()

        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(row=0, column=0, sticky=(N, E, W, S))
        mainframe.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)

        ttk.Label(mainframe, text="Nama", width=7).grid(row=1, column=1, pady=5)
        ttk.Label(mainframe, text="Alamat", width=7).grid(row=2, column=1, pady=5)
        ttk.Label(mainframe, text="No.Telp", width=7).grid(row=3, column=1, pady="5 10")
        ttk.Label(mainframe, text="Dokter", width=7).grid(row=4, column=1)

        for i in range(1,5):
            ttk.Label(mainframe, text=": ").grid(row=i, column=2)
        
        self.nama = StringVar()
        self.alamat = StringVar()
        self.noTelp = StringVar()
        self.dokter = StringVar()
        
        ttk.Entry(mainframe, width=28, textvariable=self.nama).grid(row=1, column=3,columnspan=3, sticky=W)
        ttk.Entry(mainframe, width=28, textvariable=self.alamat).grid(row=2, column=3,columnspan=3, sticky=W)
        ttk.Entry(mainframe, width=28, textvariable=self.noTelp).grid(row=3, column=3,columnspan=3, sticky=W)
        ttk.Radiobutton(mainframe, text="dr. Tulus", value="tulus", variable=self.dokter).grid(row=4, column=3, sticky=W)
        ttk.Radiobutton(mainframe, text="dr. Gisel", value="gisel", variable=self.dokter).grid(row=5, column=3,sticky=W)

        ttk.Button(mainframe, text="Submit", command=self.root.destroy).grid(row=4, column=5, rowspan=2)
    
if __name__ == "__main__":
    inputWin = InputDataWin()
    inputWin.root.mainloop()
# END MAIN
