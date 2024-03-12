class Zenesz:
    def __init__(self, sor):
        #Név;Mióta;Műfaj;Kiadott_számok;Kiadott_albumok;Azonosító
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.miota = int(adatok[1])
        self.mufaj = adatok[2]
        self.kiadott_szam = int(adatok[3])
        self.kiadott_album = int(adatok[4])
        self.azonosito = adatok[5]

class Szemelyes:
    def __init__(self, sor):
        #Azonosító;Név;Születés;Szerep;Nettó_érték;Havi_hallgatók
        adatok = sor.strip().split(";")
        self.azonosito = adatok[0]
        self.nev = int(adatok[1])
        self.szuletes = adatok[2]
        self.szerep = int(adatok[3])
        self.netto_ertek = int(adatok[4])
        self.havi_hallgatok = adatok[5]

class Banda:
    def __init__(self, sor):
        #Azonosító;Név;Születés;Szerep;Nettó_érték;Havi_hallgatók
        adatok = sor.strip().split(";")
        if sor != '':
            self.azonosito = adatok[0]
            self.netto_ertek = int(adatok[4])
            self.havi_hallgatok = int(adatok[5])
            self.szerep = adatok[3]
            self.nev = adatok[1]
            self.szuletes = int(adatok[2])