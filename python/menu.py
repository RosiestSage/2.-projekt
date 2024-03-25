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
    print('5 - Legfiatalabb(/legidősebb)')
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '1':
                return banda_kereses()
            case '2':
                return bandak_listaja()
            case '3':
                return banda_kiadas()
            case '4':
                return banda_hallgatas()
            case '5':
                return banda_kor()
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
    bandak_szama = {}
    for b in bandak:
        if b.bandanev in bandak_szama:
            bandak_szama[b.bandanev] += 1
        else:
            bandak_szama[b.bandanev] = 1
    for key, value in bandak_szama.items():
        print(f'{key}')

def banda_kereses():
    os.system('cls')
    keresett_banda = input('Keresett banda: ')
    for ba in bandak:
        if ba.bandanev != keresett_banda:
            return banda_kereses()
        else:
            print(f'\n{keresett_banda} tagjai:')    
            for b in bandak:
                if b.bandanev == keresett_banda:
                    print(f'\t{b.nev}, {b.szuletes}, {b.szerep}')
                
            input('\n<Vissza>')
            return banda()
        
def bandak_listaja():
    os.system('cls')
    bandak_szama = {}
    for b in bandak:
        if b.bandanev in bandak_szama:
            bandak_szama[b.bandanev] = b
        else:
            bandak_szama[b.bandanev] = b
    for key, value in bandak_szama.items():
        print(f'{key}, {value.netto_ertek}, {value.havi_hallgatok}')

    input('\n<Vissza>')
    return banda()

#---------------------------------------

def banda_kiadas():
    os.system('cls')
    v = ''
    print('1 - Legtöbbet kiadott')
    print('2 - Legkevesebbet kiadott')
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '1':
                return banda_legtobbet_kiadott()
            case '2':
                return banda_legkevesebbet_kiadott()
            case '0':
                return banda()

def banda_legtobbet_kiadott():
    os.system('cls')
    legtobbet_kiadott = bandak[0]
    for b in bandak:
        if legtobbet_kiadott.kiadott_szam < b.kiadott_szam:
            legtobbet_kiadott = b
    print(f'Legtöbb albumot kiadott: {legtobbet_kiadott.bandanev}')
    print(f'Legtöbb számot kiadott: {legtobbet_kiadott}')
    input('\n<Vissza>')
    return banda()  

def banda_legkevesebbet_kiadott():
    os.system('cls')
    legkevesebbet_kiadott = bandak[0]
    for b in bandak:
        if legkevesebbet_kiadott. < b.:
            legkevesebbet_kiadott = b
    print(f'Legtöbbet hallgatott banda: {legkevesebbet_kiadott.bandanev}')
    input('\n<Vissza>')
    return banda()  

#--------------------------------------

def banda_hallgatas():
    os.system('cls')
    v = ''
    print('1 - Legtöbbet hallgatott')
    print('2 - Legkevesebbet hallgatott')
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '1':
                return banda_legtobbet_hallgatott()
            case '2':
                return banda_legkevesebbet_hallgatott()
            case '0':
                return banda()

def banda_legtobbet_hallgatott():
    os.system('cls')
    legtobbet_hallgatott = bandak[0]
    for b in bandak:
        if legtobbet_hallgatott.havi_hallgatok < b.havi_hallgatok:
            legtobbet_hallgatott = b
    print(f'Legtöbbet hallgatott banda: {legtobbet_hallgatott.bandanev}')
    input('\n<Vissza>')
    return banda()        

def banda_legkevesebbet_hallgatott():
    os.system('cls')
    legkevesebbet_hallgatott = bandak[0]
    for b in bandak:
        if legkevesebbet_hallgatott.havi_hallgatok > b.havi_hallgatok:
            legkevesebbet_hallgatott = b
    print(f'Legkevesebbet hallgatott banda: {legkevesebbet_hallgatott.bandanev}')
    input('\n<Vissza>')
    return banda() 

#-------------------------------

def banda_kor():
    os.system('cls')
    v = ''
    print('1 - Legfiatalabb')
    print('2 - Legidősebb')
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '1':
                return banda_legfiatalabb()
            case '2':
                return bandak_legidosebb()
            case '0':
                return banda()

def banda_legfiatalabb():
    os.system('cls')
    legfiatalabb = bandak[0]
    for b in bandak:
        if legfiatalabb.szuletes < b.szuletes:
            legfiatalabb = b
    print(f'Legkevesebbet hallgatott banda: {legfiatalabb.nev}')
    input('\n<Vissza>')
    return banda() 

def bandak_legidosebb():
    os.system('cls')
    legidosebb = bandak[0]
    for b in bandak:
        if legidosebb.szuletes > b.szuletes:
            legidosebb = b
    print(f'Legkevesebbet hallgatott banda: {legidosebb.nev}')
    input('\n<Vissza>')
    return banda() 

#------------------------------------

def ossz_album():
    pass

def ossz_szam():
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
    f = open('python/banda.txt', 'r', encoding='utf-8')
    f.readline()
    for row in f:
        bandak.append(Banda(row))
    f.close()

main()