


def numeroMayor():
    secuencia = input("Ingrese una secuencia de números: ")
    mayor = int(secuencia[0])
    for secuencia in secuencia: 
        numero = int(secuencia)
        if numero > mayor:                
            mayor = numero
    print(f"El número mayor en la secuencia es: {mayor}")



numeroMayor()