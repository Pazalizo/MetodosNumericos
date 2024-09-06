import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Definir la función f(m)
def f(m):
    g = 9.8
    v = 35
    t = 9
    c = 15
    return (((g * m) / c) * (1 - np.exp(-1 * (c / m) * t))) - v

# Aproximación de xr
def aproximacion(xl, xu):
    return (xl + xu) / 2

# Implementación del método de bisección
def biseccion(xl, xu, ea):
    xr = aproximacion(xl, xu)
    iterations = 0
    data = []
    xr_old = xr

    while True:
        fxr = f(xr)
        fxl = f(xl)
        multiFunciones = fxr * fxl

        if iterations > 0:
            error_relativo = abs((xr - xr_old) / xr) * 100
        else:
            error_relativo = 'N/A'

        data.append([iterations, xl, xu, xr, fxr, fxl, multiFunciones, error_relativo])
        
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

    # Mostrar tabla de iteraciones
    headers = ["Iteración", "xl", "xu", "xr", "f(xr)", "f(xl)", "Multiplicación", "Error Relativo (%)"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    print(f"La raíz es {xr}")
    print(f"Total de iteraciones: {iterations}")

    return xr

# Gráfica de la función
def graficar_funcion():
    # Definir el intervalo de m para graficar
    m_values = np.linspace(40, 100, 500)
    f_values = f(m_values)

    plt.figure(figsize=(10, 6))
    plt.plot(m_values, f_values, label='f(m)')
    plt.axhline(0, color='red', lw=1)  # Línea en y = 0
    plt.axvline(0, color='red', lw=1)  # Línea en x = 0
    plt.xlabel('m (masa)')
    plt.ylabel('f(m)')
    plt.title('Gráfico de f(m) para el método de bisección')
    plt.grid(True)
    plt.legend()

# Parámetros iniciales para la bisección
xl = 59
xu = 60
tolerancia = 0.1  # 0.1%

# Graficar la función
graficar_funcion()

# Aplicar el método de bisección
raiz = biseccion(xl, xu, tolerancia)

# Marcar la raíz en el gráfico
plt.plot(raiz, f(raiz), 'bo', label=f'Raíz: m = {raiz:.4f}')  # Punto azul en la raíz
plt.legend()

# Mostrar el gráfico final
plt.show()
