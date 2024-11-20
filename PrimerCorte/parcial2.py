from tabulate import tabulate
import math
import cmath

def funcion(R_val):
    L = 5  # Henry
    C = 1e-4  # Faradios
    q0 = 1  # Carga inicial
    t = 0.05  # Tiempo

    omega_0 = 1 / math.sqrt(L * C)
    alpha = R_val / (2 * L)
    discriminant = omega_0**2 - alpha**2

    omega_d = cmath.sqrt(discriminant)
    q_t = q0 * cmath.exp(-alpha * t) * cmath.cos(omega_d * t)

    # Tomamos la parte real de q_t para compararla
    q_t_real = q_t.real
    return q_t_real - 0.01

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
        
    headers = ["Iteración", "xl", "xu", "xr", "f(xr)", "f(xl)", "Multiplicación", "Error Relativo (%)"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    print(f"La raíz es {xr}")
    print(f"Total de iteraciones: {iterations}")
    print(f"El valor de R tiene que estar entre: {xl} y {xu}, para un error relativo de {ea}")	

def main():
    xl = 1       # Límite inferior de R
    xu = 1000    # Límite superior de R
    ea = 0.01    # Error absoluto esperado

    biseccion(xl, xu, ea)

if __name__ == "__main__":
    main()
