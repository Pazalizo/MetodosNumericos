from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    return -0.5 * x**2 + 2.5 * x + 4.5

def aproximacion(xl, xu):
    fxl = funcion(xl)
    fxu = funcion(xu)
    return xu - ((fxu * (xl - xu)) / (fxl - fxu))

def punto_falso(xl, xu, ea):
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

        if iterations > 0:
            error_relativo = abs((xr - xr_old) / xr) * 100
        else:
            error_relativo = 'N/A'

        data.append([iterations, xl, xu, xr, fxr, fxl, multiFunciones, error_relativo])
        xr_values.append(xr)  # Guardar el valor de xr
        fxr_values.append(fxr) # Guardar el valor de f(xr)
        xl_values.append(xl)
        xu_values.append(xu)

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

    headers = ["Iteración", "xl", "xu", "xr", "f(xr)", "f(xl)", "Multiplicación", "Error Relativo (%)"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    print(f"La raíz es {xr}")
    print(f"Total de iteraciones: {iterations}")

    # Crear la gráfica
    x = np.linspace(min(xl_values + xu_values) - 1, max(xl_values + xu_values) + 1, 400)
    y = funcion(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    
    # Graficar las líneas secantes y los puntos xr
    for i in range(len(xr_values)):
        xl, xu, xr = xl_values[i], xu_values[i], xr_values[i]
        plt.plot([xl, xu], [funcion(xl), funcion(xu)], 'r--', label=f'Secante Iter {i}' if i == 0 else "", alpha=0.5)
        plt.scatter(xr, 0, color='blue', zorder=5)
    
    plt.title('Método de la Falsa Posición')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    xl = float(input("Ingrese el valor de xl: "))
    xu = float(input("Ingrese el valor de xu: "))
    ea = float(input("Ingrese el error absoluto esperado (ea): "))

    punto_falso(xl, xu, ea)

if __name__ == "__main__":
    main()