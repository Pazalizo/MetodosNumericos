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

def newton_raphson(funcion_str, x0_str, error_str):
    x = sp.symbols('x')
    try:
        # Reemplazar funciones por las de SymPy
        funcion_str_sympy = reemplazar_funciones(funcion_str)
        # Convertir la función ingresada a una expresión simbólica
        f = eval(funcion_str_sympy, {'sp': sp, 'x': x})
    except (SyntaxError, NameError):
        messagebox.showerror("Error", "Función inválida. Por favor, revisa la sintaxis.")
        return

    # Calcular la derivada de la función
    f_prime = sp.diff(f, x)

    # Convertir x0 y error a valores numéricos
    try:
        x0 = float(x0_str)
        error_min = float(error_str)
    except ValueError:
        messagebox.showerror("Error", "Valor inicial o error mínimo inválido.")
        return

    # Funciones evaluables numéricamente
    f_eval = sp.lambdify(x, f, modules=['numpy'])
    f_prime_eval = sp.lambdify(x, f_prime, modules=['numpy'])

    # Listas para almacenar los valores de x0 y errores
    iteraciones = []
    iteracion = 0
    x_values = [x0]

    while True:
        iteracion += 1
        try:
            f_x0 = f_eval(x0)
            f_prime_x0 = f_prime_eval(x0)
        except Exception as e:
            messagebox.showerror("Error", f"Error al evaluar la función: {e}")
            return

        if f_prime_x0 == 0:
            messagebox.showerror("Error", "La derivada es cero. No se puede continuar.")
            return

        x1 = x0 - f_x0 / f_prime_x0
        error = abs(x1 - x0)

        # Guardar datos de la iteración
        iteraciones.append([iteracion, x0, f_x0, f_prime_x0, x1, error])
        x_values.append(x1)

        if error < error_min:
            break

        x0 = x1

        if iteracion > 1000:
            messagebox.showwarning("Aviso", "Se alcanzó el número máximo de iteraciones.")
            break

    # Mostrar resultados en la interfaz gráfica
    resultado_texto = f"Raíz aproximada: x = {x1:.6f}\nNúmero de iteraciones: {iteracion}"
    resultado_label.config(text=resultado_texto)

    # Generar tabla con los resultados
    encabezados = ["Iteración", "x_i", "f(x_i)", "f'(x_i)", "x_i+1", "Error"]
    tabla_resultados = tabulate(iteraciones, headers=encabezados, tablefmt="grid")
    tabla_text.delete(1.0, tk.END)
    tabla_text.insert(tk.END, tabla_resultados)

    # Graficar la función y las aproximaciones
    f_lambdified = sp.lambdify(x, f, modules=['numpy'])
    x_min = min(x_values) - 1
    x_max = max(x_values) + 1
    x_vals = np.linspace(x_min, x_max, 400)
    y_vals = f_lambdified(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=f"$f(x) = {sp.latex(f)}$", color='orange')
    plt.axhline(0, color='red', linestyle='--', linewidth=1)
    plt.axvline(0, color='black', linestyle='--', linewidth=1)

    # Graficar los valores de x
    plt.scatter(x_values, f_lambdified(np.array(x_values)), color='blue', label='Aproximaciones', marker='o')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Método de Newton-Raphson')
    plt.legend()
    plt.grid(True)

    # Anotación del último valor de x
    plt.annotate(f'Raíz: x ≈ {x_values[-1]:.4f}', xy=(x_values[-1], 0),
                 xytext=(x_values[-1], max(y_vals)/2),
                 arrowprops=dict(arrowstyle="->", color='blue'))

    plt.show()

def calcular():
    funcion_str = funcion_entry.get()
    x0_str = x0_entry.get()
    error_str = error_entry.get()
    newton_raphson(funcion_str, x0_str, error_str)

def main():
    global funcion_entry, x0_entry, error_entry, resultado_label, tabla_text

    root = tk.Tk()
    root.title("Método de Newton-Raphson")

    ttk.Label(root, text="Función f(x):").grid(row=0, column=0, sticky="W", padx=5, pady=5)
    funcion_entry = ttk.Entry(root, width=30)
    funcion_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(root, text="Valor inicial x0:").grid(row=1, column=0, sticky="W", padx=5, pady=5)
    x0_entry = ttk.Entry(root, width=20)
    x0_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(root, text="Error mínimo:").grid(row=2, column=0, sticky="W", padx=5, pady=5)
    error_entry = ttk.Entry(root, width=20)
    error_entry.grid(row=2, column=1, padx=5, pady=5)

    calcular_btn = ttk.Button(root, text="Calcular Raíz", command=calcular)
    calcular_btn.grid(row=3, column=0, columnspan=2, pady=10)

    resultado_label = ttk.Label(root, text="")
    resultado_label.grid(row=4, column=0, columnspan=2)

    tabla_text = tk.Text(root, width=80, height=20)
    tabla_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
