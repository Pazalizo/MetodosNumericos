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
    sp.S(1.2)   
]

xi = 0
h = 1

#Calcular el valor de f(xi + h)
def calcularValorEsperado(xi, h, funciones):
    x_valor = xi + h
    sumatoria = sum(f.subs(x, x_valor) for f in funciones)
    print(f"El total de f(x) es: {sumatoria}")
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
        derivadaAux = sp.diff(funcion[i],x)
        #print(f"primera derivada: {derivada}")
        Derivada.append(derivadaAux)
    return Derivada

def serieDeTaylor(xi, h, funciones):
    
    valorEsperado = calcularValorEsperado(xi, h, funciones)
    #Declarar Variables
    n = 0
    valoresSerie = []
    funcionesDerivadas = []
    #Primera parte evaluar F(xi)
    valoresSerie.append(evaluacionFuncion(xi, funciones))
    sumatoriaSerie = valoresSerie[0]
    funcionesDerivadas.append(funciones)
    #print(funcionesDerivadas[0])
    while n < 4:
        funcionesDerivadas.append(derivar(funcionesDerivadas[n]))
        print(funcionesDerivadas)
        valoresSerie.append(evaluacionFuncion(xi, funcionesDerivadas[n+1]))
        n=n+1
    print(valoresSerie)
    print(funcionesDerivadas[-1])

serieDeTaylor(xi, h, funciones)