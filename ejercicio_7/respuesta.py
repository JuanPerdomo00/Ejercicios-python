#!/usr/bin/python3

def masa_corp(peso, altura):
    '''Solucion
    '''
    ecuacion =  peso / altura**2
    imc = round(ecuacion, 2)

    print(f'Su indice de masa corporal es {imc}')

    


def main():
    peso = float(input('Ingrese el peso en [kg]: '))
    altura = float(input('Ingrese la estatura en metros [m]: '))
    masa_corp(peso, altura)

if __name__ == '__main__':
    main()