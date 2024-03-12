import os

def main():
    os.system('cls')
    v = ''
    while v != 0:
        v = menu()
        match v:
            case '1':
                return D1()
            case '2':
                return D2()
            case '3':
                return D3()
    
def menu():
    os.system('cls')
    print('1 - D1')
    print('2 - D2')
    print('3 - D3')
    return input('\nVálasztás: ')

def D1():
    os.system('cls')
    v = ''
    print('1 - S1')
    print('2 - S2')
    print('3 - S3')
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '0':
                return main()
            
def D2():
    os.system('cls')
    v = ''
    print('1 - A1')
    print('2 - A2')
    print('3 - A3')
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '1':
                pass
                # return A1()
            case '2':
                pass
                # return A2()
            case '3':
                pass
                # return A3()
            case '0':
                return main()

def D3():
    os.system('cls')
    v = ''
    print('1 - G1')
    print('2 - G2')
    print('3 - G3')
    print('\n0 - Vissza')
    while v != 0:
        v = input('\nVálasztás: ')
        match v:
            case '1':
                pass
                # return G1()
            case '2':
                pass
                # return G2()
            case '3':
                pass
                # return G3()
            case '0':
                return main()
            
def S1():
    os.system('cls')
    pass

def S2():
    os.system('cls')
    pass

def S3():
    os.system('cls')
    pass

def A1():
    os.system('cls')
    pass

def A2():
    os.system('cls')
    pass

def A3():
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

main()