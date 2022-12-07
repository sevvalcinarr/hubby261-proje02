import os
class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
    http = siteURL[:7]
    https = siteURL[:8]

    if http == "http://" or https == "https://":
        dataOpen.write(siteURL + "\n")
        dataOpen.close()
        print("Girmiş olduğunuz URL başarıyla kaydedildi.")
    else:
        print("Hata!")
        print("Lütfen URL'in ön ekini ('http://' veya 'https://') giriniz.")

  def dataRead(self):
      dataOpen = open(self.dataFile, 'r')
      if os.stat(self.dataFile).st_size==0:
          print("Henüz kaydedilmiş adres yok!")
      else:
            for dataShow in dataOpen:
                print(dataShow)
      dataOpen.close()