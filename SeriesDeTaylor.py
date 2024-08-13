# Series de Taylor
import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

#Definir Variables
funciones = [
    -0.1 * x**4,  
    -0.15 * x**3,
    -0.5 * x **2,
    -0.25 * x,
    1.2   
]

xi = 0
h = 1

#Calcular el valor de f(xi + h)
def valorEsperado(xi, h, funciones):
    sumatoria = 0
    x = xi + h
    for i in range(len(funciones)):
        prueba = str(funciones[i])
        resultado = eval(prueba)
        sumatoria += resultado
    print(f"el total de f(x) es :{sumatoria}")

#Derivadas
primeraDerivada = []
for i in range(len(funciones)):
    derivada = sp.diff(funciones[i],x)
    #print(f"primera derivada: {derivada}")
    primeraDerivada.append(derivada)

valorEsperado(xi, h, funciones)