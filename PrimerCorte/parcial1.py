from tabulate import tabulate
import numpy as np
import math

def funcion(x):
    return (1 + 0.2)*math.sqrt(1-(0.2/1.2)*(2**2)) - math.sin(x)

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
    print(f"El angulo tiene que estar entre: {xl} y {xu}, para un error relativo de {error_relativo}")	

def main():

    xl = 40
    xu = 50
    ea = 0.01

    biseccion(xl, xu, ea)

if __name__ == "__main__":
    main()
