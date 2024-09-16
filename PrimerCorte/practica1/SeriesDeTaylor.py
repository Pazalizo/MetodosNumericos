import sympy as sp
import math
from tabulate import tabulate

# Definir la variable simbólica
x = sp.symbols('x')

# Definir funciones simbólicas
funciones = [
    25*x**3 - 6*x**2 + 7*x - 88
]

xi = 1
h = 1

# Calcular el valor de f(xi + h)
def calcularValorEsperado(xi, h, funciones):
    x_valor = xi + h
    sumatoria = sum(f.subs(x, x_valor) for f in funciones)
    print(f"El total de f(x) es: {sumatoria}")
    return sumatoria

def evaluacionFuncion(xi, funciones):
    sumatoria = 0
    for funcion in funciones:
        sumatoria += funcion.subs(x, xi)
    return sumatoria

def derivar(funcion):
    Derivada = []
    for f in funcion:
        derivadaAux = sp.diff(f, x)
        Derivada.append(derivadaAux)
    return Derivada

def serieDeTaylor(xi, h, funciones):
    valorEsperado = calcularValorEsperado(xi, h, funciones)
    
    # Declarar Variables
    n = 0
    valoresSerie = []
    funcionesDerivadas = []
    datos_tabla = []  # Lista para almacenar los datos de cada iteración
    
    # Primera parte: evaluar F(xi)
    valoresSerie.append(evaluacionFuncion(xi, funciones))
    funcionesDerivadas.append(funciones)
    
    fact = 1
    valorCalculado = valoresSerie[0]

    # Primera fila de la tabla (iteración 0, sin derivada)
    datos_tabla.append([n, valorCalculado, "N/A", funciones])

    # Bucle para calcular y mostrar cada iteración
    while n < 3:  # Cambiado para hacer 4 iteraciones
        funcionesDerivadas.append(derivar(funcionesDerivadas[n]))
        valor_evaluado = evaluacionFuncion(xi, funcionesDerivadas[n+1])
        valor_evaluado = valor_evaluado * h ** fact
        termino_serie = valor_evaluado / sp.factorial(fact)
        
        # Sumar el nuevo término al valor calculado
        valoresSerie.append(termino_serie)
        valorCalculado += termino_serie
        
        # Calcular el error relativo
        error_relativo = abs((valorEsperado - valorCalculado) / valorEsperado) * 100
        
        # Guardar los datos en la tabla, incluyendo la derivada en la iteración
        datos_tabla.append([n+1, valorCalculado, error_relativo, funcionesDerivadas[n+1]])

        # Incrementar contador de iteraciones y factorial
        fact += 1
        n += 1

    # Mostrar tabla con los resultados
    headers = ["Iteración", "Valor Calculado", "Error Relativo (%)", "Derivada"]
    print(tabulate(datos_tabla, headers=headers, tablefmt="grid"))

    print(f"\nEl valor aproximado final es: {valorCalculado}")
    print(f"El valor esperado es: {valorEsperado}")

# Llamar a la función con las funciones deseadas
serieDeTaylor(xi, h, funciones)
