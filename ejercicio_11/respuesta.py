#!/usr/bin/python3


def pan (x,y):
    costo = 3.49*x
    costo2 = 3.49*.06*y
    costototal = costo + costo2
    costototal = round(costototal, 3)
    print ("""
    Este es el costo de una barra fresca : $3.49
    Este es el descuento de una barra de ayer : 60%
    Este es el costo total : $""" + str(costototal) 
    )


def main():
    a =int(input('Cuantos panes de hoy has elegido: '))
    b =int(input('Cuantos panes de ayer has elegido: '))
    pan(a,b)



if __name__ == '__main__':
    main()