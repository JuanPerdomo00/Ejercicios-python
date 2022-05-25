#!/usr/bin/python3

def main():
    numero_tel = str(input('Ingrese un numero telefono [prefijo-numero-extencion]: '))
    print(numero_tel[4: -3])

    # if len(numero_tel[:4]) <= 4:
    #     prefijo = numero_tel[:4] 
    #     print(prefijo)


if __name__ == '__main__':
    main()
