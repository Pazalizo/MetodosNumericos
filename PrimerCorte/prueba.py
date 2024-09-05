from tabulate import tabulate
import numpy as np
import math

def funcion(m):
    g = 9.8
    v = 35
    t = 9
    c = 15
    return (((g*m)/(c))*(1-np.exp(-1*((c/m)*t)))) - v

def funcion(x):
    x_radianes = math.radians(x)  # Convertir x de grados a radianes
    return math.sin(x_radianes) - x_radianes

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
        
        if (multiFunciones < 0):
            xu = xr
        elif (multiFunciones > 0):
            xl = xr
        else:
            break
        
        xr_old = xr
        xr = aproximacion(xl, xu)
        iterations += 1

        if error_relativo != 'N/A' and error_relativo < ea:
            break

    data.append([iterations, xl, xu, xr, funcion(xr), funcion(xl), 'N/A', 'N/A'])

    headers = ["Iteración", "xl", "xu", "xr", "f(xr)", "f(xl)", "Multiplicación", "Error Relativo (%)"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    print(f"La raíz es {xr}")
    print(f"Total de iteraciones: {iterations}")

def main():

    xl = float(input("Ingrese el valor de xl: "))
    xu = float(input("Ingrese el valor de xu: "))
    ea = float(input("Ingrese el error absoluto esperado (ea): "))

    biseccion(xl, xu, ea)

if __name__ == "__main__":
    main()
