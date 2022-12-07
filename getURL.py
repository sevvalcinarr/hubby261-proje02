import os
import urllib.request
from bs4 import BeautifulSoup

class GetURL:
    dataFile = "dataURL.txt"
    getFile = "getURL.txt"

    def __init__(self):
        fileTest = open(self.getFile, 'a')
        fileTest.close()

    def getWeb(self):

        print("Örümcek çalışıyor...")

        dataOpen = open(self.dataFile, 'r')
        getOpen = open(self.getFile, 'w')

        for dataGet in dataOpen:
            webSite = urllib.request.urlopen(dataGet)
            getBytes = webSite.read()
            webPage = getBytes.decode("utf8")
            webSite.close()
            soup = BeautifulSoup(webPage, 'html.parser')
            getOpen.write(dataGet.strip() + " - " + soup.title.contents[0] + "\n" + soup.find("<p>").text)
            print("Site "+dataGet+" kaydedildi!")
        dataOpen.close()
        getOpen.close()
        print(" Örümcek başarıyla gönderildi.")

    def getList(self):
        getOpen = open(self.getFile, 'r')
        if os.stat(self.getFile).st_size == 0:
            print("Henüz ziyaret edilmiş adres bulunmamaktadır")
        else:
            for dataShow in getOpen:
                print(dataShow)
        getOpen.close()