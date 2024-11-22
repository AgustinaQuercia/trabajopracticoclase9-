

filas = int(input('ingrese cantidad de filas: '))
columnas = int(input('ingrese cantidad de columnas: '))




def rectangulo(filas, columnas):
    i = 0
    while i < filas:
        print("*" * columnas)
        i += 1


rectangulo(filas,columnas)
