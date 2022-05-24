#!/usr/bin/python3


def main():
    cantidad_depositada = float(input('Ingrese la cantidad de dinero depositada: '))
    interes = 0.04
    preimer_a = round(cantidad_depositada * (1 + interes), 2)
    segundo_a = round(preimer_a * (1 + interes), 2)
    tercer_a = round(segundo_a * (1 + interes), 2)


    print(preimer_a)
    print(segundo_a)
    print(tercer_a)


if __name__ == '__main__':
    main()