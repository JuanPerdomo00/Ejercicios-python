#!/usr/bin/python3

def preguntar_nombre_apellido(primer_nombre: str,segundo_nombre: str, apellido: str, segundo_apellido: str):
    
    minusculas = primer_nombre.lower() + ' ' + segundo_nombre.lower() + ' ' + apellido.lower() + ' ' + segundo_apellido.lower()

    mayúsculas = primer_nombre.upper() + ' ' + segundo_nombre.upper() + ' ' + apellido.upper() + ' ' + segundo_apellido.upper() 

    primera_letra_mayus = primer_nombre.capitalize() +' '+ segundo_nombre.capitalize() +' '+ apellido.capitalize() + ' ' + segundo_apellido.capitalize()
    
    print('''
    {}
    {}
    {}
    '''.format(minusculas, mayúsculas, primera_letra_mayus))

def main():
    nombre = str(input('nombre: '))
    segundo_nombre = str(input('segundo_nombre: '))
    apellido = str(input('primer apellido: '))
    segundo_apellido = str(input('segundo_apellido: '))

    preguntar_nombre_apellido(nombre, segundo_nombre, apellido, segundo_apellido)
    

if __name__ == '__main__':
    main()