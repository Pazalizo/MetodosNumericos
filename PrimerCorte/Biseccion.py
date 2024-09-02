def funcion(x):
    return x**10 - 1

xl = 0
xu = 1.3

def aproximacion(xl, xu):
    return (xl + xu)/2

xr = aproximacion(xl, xu)
print(xr)
iterations = 0
while True:
    fxr = funcion(xr)
    fxl = funcion(xl)
    multiFunciones = fxr * fxl
    if (multiFunciones < 0):
        xu = xr
        print(f"el valor de xu: {xu}, el valor de xl: {xl}")
        xr = aproximacion(xl, xu)
    elif (multiFunciones > 0):
        xl = xr
        print(f"el valor de xu: {xu}, el valor de xl: {xl}")
        xr = aproximacion(xl, xu)
    else:
        break
    iterations += 1

print(f"La raiz es {xr}")
print(f"total de iteraciones: {iterations}")