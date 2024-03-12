from zeneszek import Zenesz, Banda


zenesz: list[Zenesz] = []
bandak= []
def main():
    beolvasas()


def beolvasas():
    f = open("python/zenesz.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        zenesz.append(Zenesz(sor))
    f.close()

    i = 0
    x = []
    f = open("python/banda.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        banda = Banda(sor)
        kov = f.readline()
        kovetkezo = Banda(kov)
        if kov != '\n':
            if banda.azonosito == kovetkezo.azonosito:
                x.append(banda)
                x.append(kov)
                elozo = kov
        elif banda.azonosito != kov.azonosito and banda.azonosito == elozo.azonosito:
            x.append(banda)
            bandak.append(x)
            x = []

    f.close()

main()