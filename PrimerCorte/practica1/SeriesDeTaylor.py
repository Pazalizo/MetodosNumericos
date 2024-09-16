import sympy as sp
import math
import numpy as np

# Definir la variable simbólica
variable = sp.symbols('x')

#Definir Variables
funciones = [
    # -0.1 * variable**4,  
    # -0.15 * variable**3,
    # -0.5 * variable **2,
    # -0.25 * variable,
    # sp.S(1.2)   
    np.exp()
]

xi = 0
h = 1

#Calcular el valor de f(xi + h)
def calcularValorEsperado(xi, h, funciones):
    x_valor = xi + h
    sumatoria = sum(f.subs(variable, x_valor) for f in funciones)
    print(f"El total de f(x) es: {sumatoria:.6f}")
    return sumatoria

def evaluacionFuncion(xi, funciones):
    x = xi
    sumatoria = 0
    for i in range(len(funciones)):
        auxiliar = str(funciones[i])
        resultado = eval(auxiliar)
        sumatoria += resultado
    return sumatoria

def derivar(funcion):
    Derivada = []
    for i in range(len(funcion)):
        derivadaAux = sp.diff(funcion[i],variable)
        Derivada.append(derivadaAux)
    return Derivada

def serieDeTaylor(xi, h, funciones):
    
    valorEsperado = calcularValorEsperado(xi, h, funciones)
    
    n = 0
    valoresSerie = []
    funcionesDerivadas = []
    
    valoresSerie.append(evaluacionFuncion(xi, funciones))
    funcionesDerivadas.append(funciones)
    fact = 1

    while n < 4:
        funcionesDerivadas.append(derivar(funcionesDerivadas[n]))
        valoresSerie.append(round(evaluacionFuncion(xi, funcionesDerivadas[n+1])/math.factorial(fact), 3))
        fact = fact + 1
        n=n+1

    valorCalculado = 0

    for i in valoresSerie:
        valorCalculado = valorCalculado + i
    
    valorCalculadoRedondeado = round(valorCalculado,3)
    print(f"el valor aproximado calculado es: {valorCalculadoRedondeado}")

serieDeTaylor(xi, h, funciones)
