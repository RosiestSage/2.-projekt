from bandak import Banda
import os

bandak: list[Banda] = []

def main():
    banda_beolvasas()
    os.system('cls')
    v = ''
    while v != 0:
        v = menu()
        match v:
            case '1':
                return statisztika()
            case '2':
                return banda()
            case '3':
                return egyedulallo()
            case '4':
                return modositas()
    
def menu():
    os.system('cls')
    print('1 - Statisztika')
    print('2 - Bandák')
    print('3 - Egyedülálló')
    print('4 - Módosítás')
    return input('\nVálasztás: ')

def statisztika():
    os.system('cls')
    v = ''
    print('1 - Havi bevétel')
    print('2 - Hány zenész')
    print('3 - Hány banda')
    print('4 - Összes album')
    print('5 - Összes szám')
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '1':
                return havi_bevetel()
            case '2':
                return zeneszek_szama()
            case '3':
                return bandak_szama()
            case '4':
                return ossz_album()
            case '5':
                return ossz_szam()
            case '0':
                return main()
            
def banda():
    os.system('cls')
    v = ''
    print('1 - Keresett banda tagjai')
    print('2 - Bandák listája')
    print('3 - Legtöbbet(/legkevesebbet) kiadott')
    print('4 - Legtöbbet(/legkevesebbet) hallgatott')
    print('5 - Legfiatalabb')
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '1':
                return banda_kereses()
            case '2':
                return bandak_listaja()
            case '3':
                pass
                # return A3()
            case '4':
                return banda_kiadas()
            case '5':
                pass
            case '0':
                return main()

def egyedulallo():
    os.system('cls')
    v = ''
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '0':
                return main()
            
def modositas():
    os.system('cls')
    v = ''
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '0':
                return main()

def havi_bevetel():
    os.system('cls')
    pass

def zeneszek_szama():
    os.system('cls')
    pass

def bandak_szama():
    os.system('cls')
    pass

def banda_kereses():
    os.system('cls')
    keresett_banda = input('Keresett banda: ')
    for ba in bandak:
        if ba.azonosito != keresett_banda:
            return banda_kereses()
        else:
            print(f'\n{keresett_banda} tagjai:')    
            for b in bandak:
                if b.azonosito == keresett_banda:
                    print(f'\t{b.nev}, {b.szuletes}, {b.szerep}')
                
            input('\n<Vissza>')
            return banda()
        
def ossz_album():
    pass

def ossz_szam():
    pass

def bandak_listaja():
    os.system('cls')
    banda_lista = {}
    for b in bandak:
        if b.azonosito in banda_lista:
            break
        else:
            banda_lista[b.azonosito] = 1
    for key, value in banda_lista.items():
        print(f'{key}, {b.netto_ertek}, {b.havi_hallgatok}')

def A3():
    os.system('cls')
    pass

def banda_kiadas():
    os.system('cls')
    pass

def G1():
    os.system('cls')
    pass

def G2():
    os.system('cls')
    pass

def G3():
    os.system('cls')
    pass

def banda_beolvasas():
    f = open('2.-projekt/python/banda.txt', 'r', encoding='utf-8')
    f.readline()
    for row in f:
        bandak.append(Banda(row))
    f.close()

main()