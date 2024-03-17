from zeneszek import Zenesz
zenesz: list[Zenesz] = []

def main():
    beolvasas()


def beolvasas():
    f = open("python/zenesz.txt", "r", encoding="utf-8")
    f.readline()
    for sor in f:
        zenesz.append(Zenesz(sor))
    f.close()


main()