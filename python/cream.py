from zeneszek import Zenesz, Banda

zenesz: list[Zenesz] = []
bandak: list[Banda] = []
felhasznalok: list[Felhasznalo] = []


def main():
    beolvasas()
    banda_beolvasas()

def beolvasas():
    f = open("python/zenesz.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        zenesz.append(Zenesz(sor))
    f.close()

def banda_beolvasas():
    f = open("python/banda.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        bandak.append(Banda(sor))
    f.close()

def jogosultság_beolv():
    f = open("python/jogosultság.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        bandak.append(Banda(sor))
    f.close()



main()