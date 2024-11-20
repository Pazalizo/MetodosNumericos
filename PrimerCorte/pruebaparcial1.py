from math import sin, sqrt, asin, degrees
def biseccion(func, xl, xu, ea):
    xr = (xl + xu) / 2
    iterations = 0
    xr_old = xr
    while True:
        fxr = func(xr)
        fxl = func(xl)
        if iterations > 0:
            error_relativo = abs((xr - xr_old) / xr) * 100
        else:
            error_relativo = float('inf')
        iterations += 1
        if error_relativo < ea:
            break
        if fxr * fxl < 0:
            xu = xr
        else:
            xl = xr
        xr_old = xr
        xr = (xl + xu) / 2
    return xr
def main():
    from math import pi
    a = 0.2
    ve_v0 = 2
    C = (1 + a) * sqrt(1 - (a / (1 + a)) * ve_v0 ** 2)
    C_low = C * 0.99
    C_high = C * 1.01
    def funcion_low(f0):
        return sin(f0) - C_low
    def funcion_high(f0):
        return sin(f0) - C_high
    f0_low = biseccion(funcion_low, 0, pi / 2, 0.0001)
    f0_high = biseccion(funcion_high, 0, pi / 2, 0.0001)
    print(f"El rango de f0 es desde {degrees(f0_low)} hasta {degrees(f0_high)} grados")
if __name__ == "__main__":
    main()
