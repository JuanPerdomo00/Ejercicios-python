#!/usr/bin/python3

def problema(n: int, m: int):
    '''Solucion

    cociente = c
    resto = r
    '''

    c: int = n // m
    r: int = n % m

    print(f'''
    {n} entre {m} da un cociente de {c}
    y un resto de {r}
    ''')


def main():
    n = int(input('Ingrese un numero emtero [int]: '))
    m = int(input('Ingrese otro numero emtero [int]: '))

    problema(n, m)


if __name__ == '__main__':
    main()