from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    """Define la función que se usará en el método."""
    return -0.5 * x**2 + 2.5 * x + 4.5

def aproximacion(xl, xu):
    """Calcula la aproximación de la raíz utilizando el método de la falsa posición."""
    fxl = funcion(xl)
    fxu = funcion(xu)
    return xu - ((fxu * (xl - xu)) / (fxl - fxu))

def punto_falso(xl, xu, ea):
    """Implementa el método de la falsa posición para encontrar la raíz de la función."""
    xr = aproximacion(xl, xu)
    iterations = 0

    data = []
    xr_values = []  # Lista para almacenar los valores de xr
    fxr_values = [] # Lista para almacenar los valores de f(xr)
    xl_values = []
    xu_values = []

    xr_old = xr

    while True:
        fxr = funcion(xr)
        fxl = funcion(xl)
        fxu = funcion(xu)
        multiFunciones = fxr * fxl

        error_relativo = abs((xr - xr_old) / xr) * 100 if iterations > 0 else 'N/A'

        data.append([iterations, xl, xu, xr, fxr, fxl, multiFunciones, error_relativo])
        xr_values.append(xr)  # Guardar el valor de xr
        fxr_values.append(fxr) # Guardar el valor de f(xr)
        xl_values.append(xl)
        xu_values.append(xu)

        iterations += 1
        
        if error_relativo != 'N/A' and error_relativo < ea:
            break
        
        if multiFunciones < 0:
            xu = xr
        elif multiFunciones > 0:
            xl = xr
        else:
            break
        
        xr_old = xr
        xr = aproximacion(xl, xu)

    headers = ["Iteración", "xl", "xu", "xr", "f(xr)", "f(xl)", "Multiplicación", "Error Relativo (%)"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    print(f"\nLa raíz aproximada es {xr}")
    print(f"Total de iteraciones: {iterations}")

    # Graficar la función y las iteraciones
    graficar_funcion(xl_values, xu_values, xr_values)

def graficar_funcion(xl_values, xu_values, xr_values):
    """Genera una gráfica de la función y las aproximaciones de xr."""
    x = np.linspace(min(xl_values + xu_values) - 1, max(xl_values + xu_values) + 1, 400)
    y = funcion(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Graficar las líneas secantes y los puntos xr
    for i in range(len(xr_values)):
        xl, xu, xr = xl_values[i], xu_values[i], xr_values[i]
        plt.plot([xl, xu], [funcion(xl), funcion(xu)], 'r--', alpha=0.5)
        plt.scatter(xr, 0, color='blue', zorder=5, label=f'xr Iter {i}' if i == 0 else "")
    
    plt.title('Método de la Falsa Posición')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    xl = 6  # Valor de xl fijo
    xu = 7  # Valor de xu fijo
    ea = 0  # Error relativo fijo

    punto_falso(xl, xu, ea)

if __name__ == "__main__":
    main()
