import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tabulate import tabulate

def reemplazar_funciones(funcion_str):
    """
    Reemplaza las funciones matemáticas comunes por las funciones de SymPy.
    """
    funciones = ['sin', 'cos', 'tan', 'exp', 'log', 'sqrt', 'asin', 'acos', 'atan', 
                 'sinh', 'cosh', 'tanh', 'abs', 'pi', 'e']
    for func in funciones:
        funcion_str = funcion_str.replace(func + '(', f'sp.{func}(')
    return funcion_str

def funcion(x_vals):
    x = sp.symbols('x')
    try:
        # Reemplazar funciones por las de SymPy
        funcion_str_sympy = reemplazar_funciones(funcion_entry.get())
        # Convertir la función ingresada a una expresión simbólica
        f = eval(funcion_str_sympy, {'sp': sp, 'x': x})
        # Crear función evaluable numéricamente
        f_eval = sp.lambdify(x, f, modules=['numpy'])
        return f_eval(x_vals)
    except Exception as e:
        messagebox.showerror("Error", f"Error al evaluar la función: {e}")
        return None

def regla_del_trapecio(funcion, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = funcion(x)
    if y is None:
        return None, None, None, None, None
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])

    # Datos para la tabla
    datos = []
    for i in range(n + 1):
        datos.append([i, x[i], y[i]])

    return integral, h, datos, x, y

def calcular_integral():
    # Obtener datos de entrada
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        n = int(n_entry.get())
        valor_real = valor_real_entry.get()
        valor_real = float(valor_real) if valor_real else None  # Validar si hay un valor real
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
        return

    # Calcular la integral y obtener datos
    integral, h, datos, x, y = regla_del_trapecio(funcion, a, b, n)
    if integral is None:
        return

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
            f"Error verdadero porcentual (ε_t): {error_verdadero_porcentual:.4f}%\n"
        )
    resultado_label.config(text=resultado_texto)

    # Mostrar tabla
    encabezados = ["i", "x_i", "f(x_i)"]
    tabla_text.delete(1.0, tk.END)  # Limpiar la tabla anterior
    tabla_resultados = tabulate(datos, headers=encabezados, tablefmt="grid", floatfmt=".6f")
    tabla_text.insert(tk.END, tabla_resultados + '\n')

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b', label='f(x)')
    for i in range(n):
        xs = [x[i], x[i], x[i + 1], x[i + 1]]
        ys = [0, y[i], y[i + 1], 0]
        plt.fill(xs, ys, 'r', edgecolor='black', alpha=0.2)
    plt.title('Regla del Trapecio')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def calcular_iterativo():
    # Obtener datos de entrada
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        valor_real = float(valor_real_entry.get())
        max_n = int(max_n_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos y un valor real.")
        return

    # Inicializar listas para resultados
    resultados = []
    n_values = range(2, max_n + 1)
    integrales = []
    errores_relativos = []

    # Iterar sobre valores de n
    for n in n_values:
        integral, h, _, _, _ = regla_del_trapecio(funcion, a, b, n)
        if integral is None:
            return
        error_relativo = abs((valor_real - integral) / valor_real) * 100
        resultados.append([n, h, integral, error_relativo])
        integrales.append(integral)
        errores_relativos.append(error_relativo)

    # Mostrar tabla de resultados
    encabezados = ["n", "h", "I (Integral Aproximada)", "ε_t (%)"]
    tabla_text.delete(1.0, tk.END)  # Limpiar la tabla anterior
    tabla_resultados = tabulate(resultados, headers=encabezados, tablefmt="grid", floatfmt=".6f")
    tabla_text.insert(tk.END, tabla_resultados + '\n')

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
    global funcion_entry, a_entry, b_entry, n_entry, valor_real_entry, max_n_entry, tabla_text, resultado_label

    root = tk.Tk()
    root.title("Regla del Trapecio - Todas las Funcionalidades")

    # Campos de entrada
    ttk.Label(root, text="Función f(x):").grid(row=0, column=0, sticky="W", padx=5, pady=5)
    funcion_entry = ttk.Entry(root, width=30)
    funcion_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

    ttk.Label(root, text="Límite inferior a:").grid(row=1, column=0, sticky="W", padx=5, pady=5)
    a_entry = ttk.Entry(root, width=10)
    a_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(root, text="Límite superior b:").grid(row=2, column=0, sticky="W", padx=5, pady=5)
    b_entry = ttk.Entry(root, width=10)
    b_entry.grid(row=2, column=1, padx=5, pady=5)

    ttk.Label(root, text="Número de subintervalos n:").grid(row=3, column=0, sticky="W", padx=5, pady=5)
    n_entry = ttk.Entry(root, width=10)
    n_entry.grid(row=3, column=1, padx=5, pady=5)

    ttk.Label(root, text="Valor real (opcional):").grid(row=4, column=0, sticky="W", padx=5, pady=5)
    valor_real_entry = ttk.Entry(root, width=10)
    valor_real_entry.grid(row=4, column=1, padx=5, pady=5)

    ttk.Label(root, text="Máximo n (para iteración):").grid(row=5, column=0, sticky="W", padx=5, pady=5)
    max_n_entry = ttk.Entry(root, width=10)
    max_n_entry.grid(row=5, column=1, padx=5, pady=5)

    # Botones para calcular
    ttk.Button(root, text="Calcular Integral", command=calcular_integral).grid(row=6, column=0, pady=10)
    ttk.Button(root, text="Calcular Iteración", command=calcular_iterativo).grid(row=6, column=1, pady=10)

    # Área de texto para mostrar la tabla
    tabla_text = tk.Text(root, width=80, height=20)
    tabla_text.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    # Etiqueta para mostrar el resultado
    resultado_label = ttk.Label(root, text="")
    resultado_label.grid(row=8, column=0, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    main()
