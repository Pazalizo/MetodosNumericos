import sympy as sp
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt

def calcular_derivadas(funcion):
    x = sp.symbols('x')
    f = sp.sympify(funcion)
    df = sp.diff(f, x)
    d2f = sp.diff(df, x)
    return f, df, d2f

def newthon_raphson(funcion, X0, error):
    x = sp.symbols('x')
    f, df, _ = calcular_derivadas(funcion)

    X0 = float(X0)
    Eminimo = float(error)
    er = 0
    iteracion = 0

    resultados = []
    x0_values = []

    while True:
        iteracion += 1
        fev = f.subs(x, X0)
        dfev = df.subs(x, X0)
        
        Xante = X0
        X0 = X0 - (fev/dfev)
        er = abs(((X0 - Xante) / X0) * 100)
        
        resultados.append([iteracion, X0, er])
        x0_values.append(X0)
        
        if er <= Eminimo:
            break

    print(tabulate(resultados, headers=["Iteración", "X0", "Error relativo (%)"], floatfmt=".7f"))

    return f, x0_values

def newthon_raphson_mejorado(funcion, X0, error):
    x = sp.symbols('x')
    f, df, d2f = calcular_derivadas(funcion)

    X0 = float(X0)
    Eminimo = float(error)
    er = 0
    iteracion = 0

    resultados = []
    x0_values = []

    while True:
        iteracion += 1
        fev = f.subs(x, X0)
        dfev = df.subs(x, X0)
        d2fev = d2f.subs(x, X0)
        
        Xante = X0
        X0 = X0 - ((fev * dfev) / ((dfev)**2 - (fev * d2fev)))
        er = abs(((X0 - Xante) / X0) * 100)
        
        resultados.append([iteracion, X0, er])
        x0_values.append(X0)
        
        if er <= Eminimo:
            break

    print(tabulate(resultados, headers=["Iteración", "X0", "Error relativo (%)"], floatfmt=".7f"))

    return f, x0_values

def graficar_funcion(funcion, x0_values, ax, titulo):
    x = sp.symbols('x')
    f_lambdified = sp.lambdify(x, funcion, 'numpy')
    x_values = np.linspace(min(x0_values) - 1, max(x0_values) + 1, 400)
    y_values = f_lambdified(x_values)

    ax.plot(x_values, y_values, label=f"$f(x)={sp.latex(funcion)}$", color='orange')
    ax.axhline(0, color='red', linestyle='--', linewidth=1)
    ax.axvline(0, color='black', linestyle='--', linewidth=1)
    ax.scatter(x0_values, f_lambdified(np.array(x0_values)), color='blue', label='Valores de X0', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('f(X)')
    ax.set_title(titulo)
    ax.legend()
    ax.grid(True)
    ax.annotate(f'Raíz: x ≈ {x0_values[-1]:.4f}', xy=(x0_values[-1], f_lambdified(x0_values[-1])), 
                 xytext=(x0_values[-1], f_lambdified(x0_values[-1]) + 5),
                 textcoords='data',
                 arrowprops=dict(arrowstyle="->", color='blue'))

def main():
    funcion = input("Ingresa una función de x: ")
    X0 = input("Digite el valor inicial de x: ")
    error = input("Error mínimo: ")
    
    f1, x0_values1 = newthon_raphson_mejorado(funcion, X0, error)
    f2, x0_values2 = newthon_raphson(funcion, X0, error)

    # Crear la figura y los ejes para las dos gráficas en paralelo
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    graficar_funcion(f1, x0_values1, ax1, 'Aproximación de Newton-Raphson Mejorado')
    graficar_funcion(f2, x0_values2, ax2, 'Aproximación de Newton-Raphson')
    plt.show()

if __name__ == "__main__":
    main()

a= Nan
