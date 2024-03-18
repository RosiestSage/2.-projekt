from bandak import Banda
import os

bandak: list[Banda] = []

def main():
    os.system('cls')
    banda_beolvasas()
    banda_kereses()
    banda_szerep()

def banda_beolvasas():
    f = open('banda.txt', 'r', encoding='utf-8')
    f.readline()
    for row in f:
        bandak.append(Banda(row))
    f.close()
    
def banda_kereses():
    pass

def banda_szerep():
    szerepek = {}
    for b in bandak:
        if b.szerep in szerepek:
            szerepek[b.szerep] += 1
        else:
            szerepek[b.szerep] = 1
    for key, value in szerepek.items():
        print(f'{key}: {value}')
 

main()