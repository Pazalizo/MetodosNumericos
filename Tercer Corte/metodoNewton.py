import sympy as sp
from tabulate import tabulate
import matplotlib.pyplot as plt

def calcular_derivadas(funcion):
    x = sp.symbols('x')
    f = sp.sympify(funcion)
    df = sp.diff(f, x)
    return f, df

def newthon_raphson_mejorado(funcion, X0, error):
    x = sp.symbols('x')
    f, df = calcular_derivadas(funcion)

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
        
        Xante = X0
        X0 = X0 - (fev/dfev)
        er = abs(((X0 - Xante) / X0) * 100)
        
        # Almacena la iteración, el valor de X0 y el error relativo en la lista
        resultados.append([iteracion, X0, er])
        x0_values.append(X0)  # Agrega X0 a la lista de valores para graficar
        
        if er <= Eminimo:
            break

    # Muestra la tabla de resultados usando tabulate
    headers = ["Iteración", "X0", "Error relativo (%)"]
    print(tabulate(resultados, headers=headers, floatfmt=".7f"))

    # Graficar los valores de X0 en un plano cartesiano en el eje x y y=0
    plt.scatter(x0_values, [0]*len(x0_values),color='blue', label='Valores de X0', marker='o')
    plt.axhline(0, color='red', linestyle='--', linewidth=1)  # Línea en y=0 para referencia
    plt.axvline(0, color='black', linestyle='--', linewidth=1)  # Línea en x=0 para referencia
    plt.xlabel('X0')
    plt.ylabel('y')
    plt.title('Aproximación de X0 hacia la raíz')
    plt.legend()
    plt.grid(True)

    # Anotación del último valor de X0 (aproximación de la raíz)
    plt.annotate(f'Raíz: x ≈ {x0_values[-1]:.4f}', xy=(x0_values[-1], 0), 
                 xytext=(x0_values[-1], 0.1),
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