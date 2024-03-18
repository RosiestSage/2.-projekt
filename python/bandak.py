class Banda:
    def __init__(self, sor: str):
        adatok = sor.strip().split(';')
        self.azonosito = adatok[0]
        self.nev = adatok[1]
        self.szuletes = int(adatok[2])
        self.szerep = adatok[3]
        self.netto_ertek = int(adatok[4].replace(",", ""))
        self.havi_hallgatok = int(adatok[5].replace(",", ""))
        
        
