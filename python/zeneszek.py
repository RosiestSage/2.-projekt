class Zenesz:
    def __init__(self, sor):
        #Név;Műfaj;Szerep;Kiadott_számok;Kiadott_albumok;Születés;Nettó_érték;Havi_hallgatók;Mióta;
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.mufaj = adatok[1]
        self.szerep = adatok[2]
        self.kiadott_szam = int(adatok[3])
        self.kiadott_album = int(adatok[4])
        self.szuletes = int(adatok[5])
        self.netto_ertek = int(adatok[6].replace(",", ""))
        self.havi_hallgatok = int(adatok[7].replace(",", ""))
        self.miota = int(adatok[8])

class Banda:
    def __init__(self, sor: str):
        #Banda_név;Név;Műfaj;Szerep;Kiadott_számok;Kiadott_albumok;Születés;Nettó_érték;Havi_hallgatók;Mióta;
        adatok = sor.strip().split(';')
        self.bandanev = adatok[0]
        self.nev = adatok[1]
        self.mufaj = adatok[2]
        self.szerep = adatok[3]
        self.kiadott_szam = int(adatok[4])
        self.kiadott_album = int(adatok[5])
        self.szuletes = int(adatok[6])
        self.netto_ertek = int(adatok[7].replace(",", ""))
        self.havi_hallgatok = int(adatok[8].replace(",", ""))
        self.miota = int(adatok[9])
