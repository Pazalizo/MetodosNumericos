# Series de Taylor
import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

#Prueba de Arrays
funciones = [
    -0.1 * x**4,  
    -0.15 * x**3,
    -0.5 * x **2,
    -0.25 * x,
    1.2   
]

primeraDerivada = []

for i in range(len(funciones)):
    print(i)
    derivada = sp.diff(funciones[i],x)
    print(f"primera derivada: {derivada}")
    primeraDerivada.append(derivada)

