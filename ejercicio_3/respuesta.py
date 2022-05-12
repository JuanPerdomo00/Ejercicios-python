#!/usr/bin/python3

def main():
    '''Solucion

    pedir nombre al usuario

    almacenar usuariuo en variable

    imprimir el nombre con la cadena Hola
    '''

    name: str = input('Ingrese su nombre: ')

    print(f'HOLA {name}!')


if __name__ == '__main__':
    main()