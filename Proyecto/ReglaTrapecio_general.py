import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate as tab
import tkinter as tk
from tkinter import ttk

def funcion(x):
    return eval(funcion_entry.get())

def regla_del_trapecio(funcion, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = funcion(x)
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])

    # Datos para la tabla
    datos = []
    for i in range(n + 1):
        datos.append([i, x[i], y[i]])

    return integral, h, datos, x, y

def calcular_integral():
    # Obtener datos de entrada
    a = float(a_entry.get())
    b = float(b_entry.get())
    n = int(n_entry.get())
    valor_real = valor_real_entry.get()
    valor_real = float(valor_real) if valor_real else None  # Validar si hay un valor real

    # Calcular la integral y obtener datos
    integral, h, datos, x, y = regla_del_trapecio(funcion, a, b, n)

    # Calcular errores si hay un valor real ingresado
    error_verdadero = None
    error_verdadero_porcentual = None
    if valor_real is not None:
        error_verdadero = valor_real - integral
        error_verdadero_porcentual = (error_verdadero / valor_real) * 100

    # Mostrar resultados
    resultado_texto = f"Valor aproximado de la integral: {integral:.6f}\n"
    if valor_real is not None:
        resultado_texto += (
            f"Error verdadero (E_t): {error_verdadero:.6f}\n"
            f"Error verdadero porcentual (ε_t): {error_verdadero_porcentual:.2f}%\n"
        )
    resultado_label.config(text=resultado_texto)

    # Mostrar tabla
    encabezados = ["i", "x_i", "f(x_i)"]
    tabla_text.delete(1.0, tk.END)  # Limpiar la tabla anterior
    tabla_text.insert(tk.END, tab(datos, headers=encabezados, tablefmt="grid") + '\n')

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b', label='f(x)')
    for i in range(n):
        xs = [x[i], x[i], x[i + 1], x[i + 1]]
        ys = [0, funcion(x[i]), funcion(x[i + 1]), 0]
        plt.fill(xs, ys, 'r', edgecolor='black', alpha=0.2)
    plt.title('Regla del Trapecio')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def calcular_iterativo():
    # Obtener datos de entrada
    a = float(a_entry.get())
    b = float(b_entry.get())
    valor_real = float(valor_real_entry.get())
    max_n = int(max_n_entry.get())

    # Inicializar listas para resultados
    resultados = []
    n_values = range(2, max_n + 1)
    integrales = []
    errores_relativos = []

    # Iterar sobre valores de n
    for n in n_values:
        integral, h, _, _, _ = regla_del_trapecio(funcion, a, b, n)
        error_relativo = abs((valor_real - integral) / valor_real) * 100
        resultados.append([n, h, integral, error_relativo])
        integrales.append(integral)
        errores_relativos.append(error_relativo)

    # Mostrar tabla de resultados
    encabezados = ["n", "h", "I (Integral Aproximada)", "ε_t (%)"]
    tabla_text.delete(1.0, tk.END)  # Limpiar la tabla anterior
    tabla_text.insert(tk.END, tab(resultados, headers=encabezados, tablefmt="grid") + '\n')

    # Graficar
    plt.figure(figsize=(10, 6))

    # Gráfico de integrales aproximadas
    plt.subplot(2, 1, 1)
    plt.plot(n_values, integrales, marker='o', label="I (Integral Aproximada)")
    plt.axhline(valor_real, color='r', linestyle='--', label="Valor Real")
    plt.title('Cambio en I (Integral Aproximada) con n')
    plt.xlabel('n (Número de Subintervalos)')
    plt.ylabel('I (Integral Aproximada)')
    plt.legend()
    plt.grid(True)

    # Gráfico de errores relativos
    plt.subplot(2, 1, 2)
    plt.plot(n_values, errores_relativos, marker='o', color='orange', label="ε_t (%)")
    plt.title('Cambio en ε_t (Error Relativo Porcentual) con n')
    plt.xlabel('n (Número de Subintervalos)')
    plt.ylabel('ε_t (%)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    root = tk.Tk()
    root.title("Regla del Trapecio - Todas las Funcionalidades")

    # Campos de entrada
    ttk.Label(root, text="Función f(x):").grid(row=0, column=0, sticky="W")
    global funcion_entry
    funcion_entry = ttk.Entry(root, width=30)
    funcion_entry.grid(row=0, column=1, columnspan=2)

    ttk.Label(root, text="Límite inferior a:").grid(row=1, column=0, sticky="W")
    global a_entry
    a_entry = ttk.Entry(root, width=10)
    a_entry.grid(row=1, column=1)

    ttk.Label(root, text="Límite superior b:").grid(row=2, column=0, sticky="W")
    global b_entry
    b_entry = ttk.Entry(root, width=10)
    b_entry.grid(row=2, column=1)

    ttk.Label(root, text="Número de subintervalos n:").grid(row=3, column=0, sticky="W")
    global n_entry
    n_entry = ttk.Entry(root, width=10)
    n_entry.grid(row=3, column=1)

    ttk.Label(root, text="Valor real (opcional):").grid(row=4, column=0, sticky="W")
    global valor_real_entry
    valor_real_entry = ttk.Entry(root, width=10)
    valor_real_entry.grid(row=4, column=1)

    ttk.Label(root, text="Máximo n (para iteración):").grid(row=5, column=0, sticky="W")
    global max_n_entry
    max_n_entry = ttk.Entry(root, width=10)
    max_n_entry.grid(row=5, column=1)

    # Botones para calcular
    ttk.Button(root, text="Calcular Integral", command=calcular_integral).grid(row=6, column=0, pady=10)
    ttk.Button(root, text="Calcular Iteración", command=calcular_iterativo).grid(row=6, column=1, pady=10)

    # Área de texto para mostrar la tabla
    global tabla_text
    tabla_text = tk.Text(root, width=80, height=20)
    tabla_text.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    # Etiqueta para mostrar el resultado
    global resultado_label
    resultado_label = ttk.Label(root, text="")
    resultado_label.grid(row=8, column=0, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    main()
