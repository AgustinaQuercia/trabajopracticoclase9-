



respuesta = str.lower(input('ingrese un color: '))

def validar(respuesta):
    primarios = [ 'rojo', 'amarillo', 'azul' ]
    if respuesta in primarios:
        print('el color es primario')
    else:
        print('el color no es primario')


def validar2(respuesta):
    primarios = ['rojo', 'amarillo', 'azul']
    for primario in primarios:
        if primario == respuesta:
            print('El color es primario')
            break
    else:
        print('El color no es primario')

validar2(respuesta)