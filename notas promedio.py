

nota1 = int(input('ingrese nota uno a caldular: '))
nota2 = int(input('ingrese nota dos a caldular: '))
nota3 = int(input('ingrese nota tres a caldular: '))


def evaluarNotas(nota1,nota2,nota3):
    notasSumadas= (nota1 + nota2 + nota3) /3
    return f"El mensaje generado es: {notasSumadas}"

promedio = evaluarNotas(nota1,nota2,nota3)

print(promedio)