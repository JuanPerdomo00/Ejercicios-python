#!/usr/bin/python3

def main():
    nombre: str = str(input('nombre: ').upper())
    n_letra = len(nombre)
    print(f'{nombre} tiene {n_letra}')



if __name__ == '__main__':
    main()