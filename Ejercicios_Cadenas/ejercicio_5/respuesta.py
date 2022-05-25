#!/usr/bin/python3
import time


def main():
    frase = input('Ingrese una frase: ')
    print('su frase es {}'.format(frase))
    time.sleep(1)

    frase_invertida = frase[::-1]
    print('su frase invertida es: {}'.format(frase_invertida))


if __name__ == '__main__':
    main()