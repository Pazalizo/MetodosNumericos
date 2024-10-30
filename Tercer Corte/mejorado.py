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

def newthon_raphson_mejorado(funcion, X0, error):
    x = sp.symbols('x')
    f, df, d2f = calcular_derivadas(funcion)

    X0 = float(X0)
    Eminimo = float(error)
    er = 0
    iteracion = 0

    # Lista para almacenar los datos de cada iteración
    resultados = []
    x0_values = []  # Lista para almacenar los valores de X0 en cada iteración

    while True:
        iteracion += 1
        fev = f.subs(x, X0)
        dfev = df.subs(x, X0)
        d2fev = d2f.subs(x, X0)
        
        Xante = X0
        X0 = X0 - ((fev * dfev) / ((dfev)**2 - (fev * d2fev)))
        er = abs(((X0 - Xante) / X0) * 100)
        
        # Almacena la iteración, el valor de X0 y el error relativo en la lista
        resultados.append([iteracion, X0, er])
        x0_values.append(X0)  # Agrega X0 a la lista de valores para graficar
        
        if er <= Eminimo:
            break

    # Muestra la tabla de resultados usando tabulate
    headers = ["Iteración", "X0", "Error relativo (%)"]
    print(tabulate(resultados, headers=headers, floatfmt=".7f"))

    # Graficar la función original
    f_lambdified = sp.lambdify(x, f, 'numpy')
    x_values = np.linspace(min(x0_values) - 1, max(x0_values) + 1, 400)
    y_values = f_lambdified(x_values)

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, label=f"$f(x)={sp.latex(f)}$", color='orange')
    plt.axhline(0, color='red', linestyle='--', linewidth=1)  # Línea en y=0
    plt.axvline(0, color='black', linestyle='--', linewidth=1)  # Línea en x=0
    
    # Graficar los valores de X0
    plt.scatter(x0_values, f_lambdified(np.array(x0_values)), color='blue', label='Valores de X0', marker='o')
    
    plt.xlabel('X')
    plt.ylabel('f(X)')
    plt.title('Aproximación de Newton-Raphson mejorado')
    plt.legend()
    plt.grid(True)

    # Anotación del último valor de X0 (aproximación de la raíz)
    plt.annotate(f'Raíz: x ≈ {x0_values[-1]:.4f}', xy=(x0_values[-1], f_lambdified(x0_values[-1])), 
                 xytext=(x0_values[-1], f_lambdified(x0_values[-1]) + 5),
                 textcoords='data',
                 arrowprops=dict(arrowstyle="->", color='blue'))

    plt.show()
    return X0


def main():
    funcion = input("Ingresa una función de x: ")
    X0 = input("Digite el valor inicial de x: ")
    error = input("Error mínimo: ")
    
    newthon_raphson_mejorado(funcion, X0, error)

if __name__ == "__main__":
    main()