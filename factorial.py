
numero = int(input('ingrese un numero para calcular su factorial: '))
def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
    elif n>1:
        resultado = n * factorial(n-1)
    return resultado




fact = factorial(numero)

print('El factorial de', numero, 'es:', fact)