from bandak import Banda
import os

bandak: list[Banda] = []

def main():
    os.system('cls')
    banda_beolvasas()
    #banda_kereses()
    hallgatas()
    #banda_szerep()

def banda_beolvasas():
    f = open('2.-projekt/python/banda.txt', 'r', encoding='utf-8')
    f.readline()
    for row in f:
        bandak.append(Banda(row))
    f.close()
    
def banda_kereses():
    keresett_banda = input('Keresett banda: ')
    print('Banda tagjai:')
    for b in bandak:
        if b.azonosito == keresett_banda:
            print(f'\t{b.nev}, {b.szuletes}, {b.szerep}')

'''def banda_kiadas():
    legtobbet_kiadott = bandak[0]
    legkevesebbet_kiadott = bandak[1]
    for b in bandak:
        if b.netto_ertek > legtobbet_kiadott:
            legtobbet_kiadott == b.netto_ertek
            print(f'A legtöbbet kiadott')
        if b.netto_ertek < legkevesebbet_kiadott:
            pass'''

def hallgatas():
    legtobbet_hallgatott = bandak[0]
    #legkevesebbet_hallgatott = bandak[-1]
    for b in bandak:
        if legtobbet_hallgatott.havi_hallgatok < b.havi_hallgatok :
            legtobbet_hallgatott == b
    print(f'A legtöbbet halgatott banda: {b.azonosito}')
    '''if b.havi_hallgatok < legkevesebbet_hallgatott.havi_hallgatok:
            legkevesebbet_hallgatott = b
            print(f'A legkevesebbet hallgatott banda: {b.azonosito}')'''

def ev():

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