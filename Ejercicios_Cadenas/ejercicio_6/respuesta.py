#!/usr/bin/python3

def main():
    frase = input("Please enter frase: ")
    vocal  = input('Introdusca una vocal en minuscula: ')

    print(f'{frase.replace(vocal, vocal.upper())}')


if __name__ == '__main__':
    main()