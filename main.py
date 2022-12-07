import time
from getURL import GetURL
from dataURL import DataURL
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="İşlemlere Devam Etmek İçin Tıklayınız").grid(column=0, row=0)
ttk.Button(frm, text="Devam", command=root.destroy).grid(column=1, row=0)


root.mainloop()

useDataURL = DataURL()
useGetURL = GetURL()

print("|------------------------------|")
print("-: Mini Örümceğe hoş geldiniz! :-")
print("|------------------------------|")

time.sleep(1)

while True:
    print("Yapılabilecek işlemler:")
    print("[0] Çıkış")
    print("[1] URL Listele")
    print("[2] URL Ekle")
    print("[3] Örümcek Gönder")
    print("[4] Sonuçları Listele")
    menuSecim = input("Lütfen bir işlem seçin [0/1/2/3/4]: ")
    if menuSecim.isdigit():
        menuSecim = int(menuSecim)
        if menuSecim == 0:
            print("Mini Örümcek kapatılıyor...")
            time.sleep(1)
            break
        elif menuSecim == 1:
            useDataURL.dataRead()
        elif menuSecim == 2:
            useDataURL.dataWrite()
        elif menuSecim == 3:
            useGetURL.getWeb()
        elif menuSecim == 4:
            useGetURL.getList()
    else:
        print("0 ile 4 arasında geçerli bir rakam girmeniz gerekmektedir!")
