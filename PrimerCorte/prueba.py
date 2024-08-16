import sympy as sp
import math

# Definir la variable simbólica
x = sp.symbols('x')

# Definir funciones simbólicas
funciones = [
    sp.cos(x)
]

xi = math.pi/4
h = math.pi/12

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
    
    # Primera parte: evaluar F(xi)
    valoresSerie.append(evaluacionFuncion(xi, funciones))
    funcionesDerivadas.append(funciones)
    
    fact = 1
    while n < 7:
        funcionesDerivadas.append(derivar(funcionesDerivadas[n]))
        print(funcionesDerivadas[n+1])
        valor_evaluado = evaluacionFuncion(xi, funcionesDerivadas[n+1])
        valor_evaluado = valor_evaluado * h ** fact
        valoresSerie.append(valor_evaluado / sp.factorial(fact))
        
        fact += 1
        n += 1
    print(f"{valoresSerie}")
    valorCalculado = sum(valoresSerie)
    valorCalculadoRedondeado = (valorCalculado)
    
    print(f"El valor aproximado calculado es: {valorCalculadoRedondeado}")

# Llamar a la función con las funciones deseadas
serieDeTaylor(xi, h, funciones)
