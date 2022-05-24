#!/usr/bin/python3

def main():
    nombre = str(input('Ingrese su nombre: '))
    numero = int(input('Ingrese un numero entero: '))

    nombre_repetido = (nombre + '\n') * numero 
    print(nombre_repetido)


if __name__ == '__main__':
    main()
