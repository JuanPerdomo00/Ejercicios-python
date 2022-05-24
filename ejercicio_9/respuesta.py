#!/usr/bin/python3



def main():
    peso_payaso = 112
    peso_muneca = 75

    payasos = int(input("Introduce el número de payasos a enviar: "))
    muñecas = int(input("Introduce el número de muñecas a enviar: "))
    peso_total = peso_payaso * payasos + peso_muñeca * muñecas
    print("El peso total del paquete es " + str(peso_total))


if __name__ == '__main__':
    main()