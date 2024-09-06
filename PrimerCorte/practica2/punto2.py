from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt 

# Definimos la función f(x)
def f(x):
    return np.sin(x) - x**2

# Implementación del método de bisección
def bisection_method(f, xl, xu, tol):
    max_iter = 1000  # Para evitar un bucle infinito, fijamos un máximo de iteraciones
    ea = None  # Inicializamos el error relativo como None
    iter_count = 0  # Contador de iteraciones

    while True:
        xr = (xl + xu) / 2.0
        fxr = f(xr)
        
        # Solo calculamos el error relativo después de la primera iteración
        if iter_count > 0:
            ea = abs((xr - xl) / xr) * 100
            if ea < tol:  # Si el error es menor que la tolerancia, salimos del bucle
                break

        #print(f"Iteración {iter_count+1}: a={xl:.2f}, b={xu:.2f}, c={xr:.2f}, ea={ea if ea is not None else 'N/A'}%")

        if f(xl) * fxr < 0:
            xu = xr
        else:
            xl = xr

        iter_count += 1

        # Si alcanzamos el máximo de iteraciones, salimos del bucle
        if iter_count >= max_iter:
            break

    return xr, ea

# Intervalo inicial
a = 0.5
b = 1.0
tolerancia = 1.0  # 1%

# Graficar la función para ver su comportamiento
x = np.linspace(0.4, 1.1, 400)
y = f(x)
plt.plot(x, y, label='f(x) = sin(x) - x^2')
plt.axhline(0, color='red', lw=0.5)
plt.axvline(0, color='red', lw=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de f(x)')
plt.grid(True)
plt.legend()

# Aplicamos el método de bisección
raiz, error_relativo = bisection_method(f, a, b, tolerancia)

# Marcamos la raíz en el gráfico
plt.plot(raiz, f(raiz), 'bo')  # 'bo' es para un punto azul
plt.text(raiz, f(raiz), f'  Raíz: x = {raiz:.4f}', verticalalignment='bottom')

# Mostrar el gráfico
plt.show()

def funcion(x):
    return np.sin(x) - x**2

def aproximacion(xl, xu):
    return (xl + xu) / 2

def biseccion(xl, xu, ea):
    xr = aproximacion(xl, xu)
    iterations = 0

    data = []

    xr_old = xr

    while True:
        fxr = funcion(xr)
        fxl = funcion(xl)
        multiFunciones = fxr * fxl

        if iterations > 0:
            error_relativo = abs((xr - xr_old) / xr) * 100
        else:
            error_relativo = 'N/A'

        data.append([iterations, xl, xu, xr, fxr, fxl, multiFunciones, error_relativo])
        
        iterations += 1
        
        if error_relativo != 'N/A' and error_relativo < ea:
            break
        
        if (multiFunciones < 0):
            xu = xr
        elif (multiFunciones > 0):
            xl = xr
        else:
            break
        
        xr_old = xr
        xr = aproximacion(xl, xu)
        
        


    #data.append([iterations, xl, xu, xr, funcion(xr), funcion(xl), 'N/A', 'N/A'])

    headers = ["Iteración", "xl", "xu", "xr", "f(xr)", "f(xl)", "Multiplicación", "Error Relativo (%)"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    print(f"La raíz es {xr}")
    print(f"Total de iteraciones: {iterations}")

def main():

    xl = 0.5
    xu = 1
    ea = 1

    biseccion(xl, xu, ea)
    

if __name__ == "__main__":
    main()
