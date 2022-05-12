#!/usr/bin/python3

def main():
    '''solucion

    preguntar cuantas hora trabajo (h)

    preguntar cuanto le pagan por horas (p)

    mostrar la paga h*p 
    '''

    horas = int(input('horas trabajadas: '))
    paga_hora = float(input('pago x hora: '))

    total_pagar = horas * paga_hora

    print(f'total a pagarle es {total_pagar}')


if __name__ == '__main__':
    main()