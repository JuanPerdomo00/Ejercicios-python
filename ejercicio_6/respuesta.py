#!/usr/bin/python3

def suma(n):
    ''' solucion
    '''
    suma = n * (n + 1) / 2
    print(f'la suma desde 1 hasta {n} es {suma}')



def main():
    n = int(input('Ingrese un numero: '))
    suma(n)


if __name__ == '__main__':
    main()