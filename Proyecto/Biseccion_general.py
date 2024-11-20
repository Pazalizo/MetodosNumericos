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
    funciones = ['sin', 'cos', 'tan', 'exp', 'log', 'sqrt', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh', 'abs']
    for func in funciones:
        funcion_str = funcion_str.replace(func + '(', f'sp.{func}(')
    return funcion_str

def funcion_ecuacion(c, funcion_str):
    x = sp.symbols('x')
    try:
        # Reemplazar funciones por las de SymPy
        funcion_str_sympy = reemplazar_funciones(funcion_str)
        # Convertir la función ingresada a una expresión simbólica
        f = eval(funcion_str_sympy, {'sp': sp, 'x': x})
        # Crear función evaluable numéricamente
        f_eval = sp.lambdify(x, f, modules=['numpy'])
        return f_eval(c)
    except Exception as e:
        messagebox.showerror("Error", f"Error al evaluar la función: {e}")
        return None

def metodo_biseccion(funcion_str, a, b, tolerancia=0.05, max_iter=100):
    iteraciones = []
    ea_anterior = None  # Para almacenar el valor de c anterior
    iteracion = 0

    # Verificar que la función cambie de signo en el intervalo [a, b]
    fa = funcion_ecuacion(a, funcion_str)
    fb = funcion_ecuacion(b, funcion_str)
    if fa * fb > 0:
        messagebox.showerror("Error", "La función no cambia de signo en el intervalo dado.")
        return None

    while iteracion < max_iter:
        iteracion += 1
        c = (a + b) / 2.0
        fa = funcion_ecuacion(a, funcion_str)
        fb = funcion_ecuacion(b, funcion_str)
        fc = funcion_ecuacion(c, funcion_str)

        if fc is None:
            return None  # Si hay error al evaluar la función

        # Calcular el error relativo aproximado (Ea)
        if ea_anterior is not None:
            ea = abs((c - ea_anterior) / c) * 100
        else:
            ea = None

        iteraciones.append([iteracion, a, b, c, fa, fb, fc, ea])

        if fc == 0 or (ea is not None and ea < tolerancia):
            break

        if fa * fc < 0:
            b = c
        else:
            a = c

        ea_anterior = c  # Actualizar el valor de c anterior

    return iteraciones

def encontrar_raiz():
    # Limpiar el resultado anterior
    result_text.delete('1.0', tk.END)
    raiz_label.config(text="")

    # Obtener valores de los campos de entrada
    funcion_str = funcion_entry.get()
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        tolerancia = float(tolerancia_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
        return

    # Encontrar la raíz usando el método de la bisección
    datos = metodo_biseccion(funcion_str, a, b, tolerancia)
    if datos is None:
        return

    # Mostrar la raíz encontrada
    raiz_aproximada = datos[-1][3]
    raiz_label.config(text=f"Raíz aproximada: {raiz_aproximada:.6f}")

    # Tabular datos
    encabezados = ["Iteración", "Xl", "Xu", "Xr", "F(Xl)", "F(Xu)", "F(Xr)", "Ea (%)"]
    tabla_resultados = tabulate(datos, headers=encabezados, tablefmt="grid", floatfmt=".6f")
    result_text.insert(tk.END, tabla_resultados)

    # Graficar
    try:
        x_vals = np.linspace(a - 1, b + 1, 400)
        x = sp.symbols('x')
        funcion_str_sympy = reemplazar_funciones(funcion_str)
        f = eval(funcion_str_sympy, {'sp': sp, 'x': x})
        f_lambdified = sp.lambdify(x, f, modules=['numpy'])
        y_vals = f_lambdified(x_vals)

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=f"$f(x) = {sp.latex(f)}$", color='orange')
        plt.axhline(0, color='red', linestyle='--', linewidth=1)
        plt.axvline(raiz_aproximada, color='blue', linestyle='--', label=f'Raíz aproximada: x ≈ {raiz_aproximada:.4f}')

        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Método de la Bisección')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Error al graficar la función: {e}")

def main():
    global funcion_entry, a_entry, b_entry, tolerancia_entry, raiz_label, result_text

    # Configuración de la interfaz gráfica
    root = tk.Tk()
    root.title("Método de la Bisección")

    # Campos de entrada
    ttk.Label(root, text="Función f(x):").grid(column=0, row=0, sticky="W", padx=5, pady=5)
    funcion_entry = ttk.Entry(root, width=50)
    funcion_entry.grid(column=1, row=0, padx=5, pady=5)

    ttk.Label(root, text="Límite inferior (a):").grid(column=0, row=1, sticky="W", padx=5, pady=5)
    a_entry = ttk.Entry(root, width=20)
    a_entry.grid(column=1, row=1, padx=5, pady=5)

    ttk.Label(root, text="Límite superior (b):").grid(column=0, row=2, sticky="W", padx=5, pady=5)
    b_entry = ttk.Entry(root, width=20)
    b_entry.grid(column=1, row=2, padx=5, pady=5)

    ttk.Label(root, text="Tolerancia (%):").grid(column=0, row=3, sticky="W", padx=5, pady=5)
    tolerancia_entry = ttk.Entry(root, width=20)
    tolerancia_entry.grid(column=1, row=3, padx=5, pady=5)

    # Botón para encontrar la raíz
    buscar_button = ttk.Button(root, text="Encontrar Raíz", command=encontrar_raiz)
    buscar_button.grid(column=0, row=4, columnspan=2, pady=10)

    # Etiqueta para mostrar la raíz encontrada
    raiz_label = ttk.Label(root, text="")
    raiz_label.grid(column=0, row=5, columnspan=2)

    # Área de texto para mostrar la tabla de resultados
    result_text = tk.Text(root, width=100, height=20)
    result_text.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
