import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular_derivada_regresion():
    try:
        # Obtener datos de entrada
        x_values = [float(entry.get()) for entry in x_entries]
        y_values = [float(entry.get()) for entry in y_entries]
        grado = int(grado_entry.get())
        x0 = float(x0_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
        return

    n = len(x_values)

    # Validar que el grado del polinomio sea menor que el número de puntos
    if grado >= n:
        messagebox.showerror("Error", "El grado del polinomio debe ser menor que el número de puntos.")
        return

    # Ajustar polinomio
    coeficientes = np.polyfit(x_values, y_values, grado)
    polinomio = np.poly1d(coeficientes)

    # Calcular derivada del polinomio
    derivada_polinomio = np.polyder(polinomio)

    # Evaluar polinomio y su derivada en x0
    valor_en_x0 = polinomio(x0)
    derivada_en_x0 = derivada_polinomio(x0)

    # Mostrar resultados
    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, f"En x0 = {x0}:\n")
    resultado_text.insert(tk.END, f"Polinomio ajustado: y(x0) = {valor_en_x0:.6f}\n")
    resultado_text.insert(tk.END, f"Derivada: y'(x0) = {derivada_en_x0:.6f}\n\n")

    # Mostrar coeficientes del polinomio
    coef_table = []
    for i, coef in enumerate(coeficientes[::-1]):
        coef_table.append([f"a_{i}", coef])
    resultado_text.insert(tk.END, "Coeficientes del polinomio:\n")
    resultado_text.insert(tk.END, tabulate(coef_table, headers=["Coeficiente", "Valor"], tablefmt="grid", floatfmt=".6f"))
    resultado_text.insert(tk.END, "\n")

    # Graficar
    x_grafica = np.linspace(min(x_values), max(x_values), 100)
    y_grafica = polinomio(x_grafica)
    y_derivada = derivada_polinomio(x_grafica)

    plt.figure(figsize=(10, 6))
    plt.plot(x_grafica, y_grafica, label='Polinomio Ajustado')
    plt.plot(x_grafica, y_derivada, label='Derivada del Polinomio', linestyle='--')
    plt.scatter(x_values, y_values, color='red', label='Datos Originales')
    plt.scatter(x0, valor_en_x0, color='green', label=f'y(x0) = {valor_en_x0:.6f}')
    plt.scatter(x0, derivada_en_x0, color='purple', label=f"y'(x0) = {derivada_en_x0:.6f}")

    plt.axvline(x0, color='gray', linestyle=':', label=f'x0 = {x0}')
    plt.title('Regresión Polinomial y su Derivada')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def solicitar_datos_regresion():
    try:
        n = int(n_entry.get())
        if n < 2:
            messagebox.showerror("Error", "Debe haber al menos 2 puntos de datos.")
            return
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número entero válido para n.")
        return

    # Crear ventana para ingresar datos
    datos_window = tk.Toplevel()
    datos_window.title("Ingresar Datos")

    global x_entries, y_entries, grado_entry, x0_entry, resultado_text
    x_entries = []
    y_entries = []

    ttk.Label(datos_window, text="x").grid(row=0, column=0, padx=5, pady=5)
    ttk.Label(datos_window, text="y").grid(row=0, column=1, padx=5, pady=5)

    for i in range(n):
        x_entry = ttk.Entry(datos_window, width=10)
        x_entry.grid(row=i+1, column=0, padx=5, pady=5)
        x_entries.append(x_entry)

        y_entry = ttk.Entry(datos_window, width=10)
        y_entry.grid(row=i+1, column=1, padx=5, pady=5)
        y_entries.append(y_entry)

    ttk.Label(datos_window, text="Grado del Polinomio:").grid(row=n+1, column=0, sticky="W", padx=5, pady=5)
    grado_entry = ttk.Entry(datos_window, width=10)
    grado_entry.grid(row=n+1, column=1, padx=5, pady=5)

    ttk.Label(datos_window, text="Punto x0 para derivada:").grid(row=n+2, column=0, sticky="W", padx=5, pady=5)
    x0_entry = ttk.Entry(datos_window, width=10)
    x0_entry.grid(row=n+2, column=1, padx=5, pady=5)

    ttk.Button(datos_window, text="Calcular Derivada", command=calcular_derivada_regresion).grid(row=n+3, column=0, columnspan=2, pady=10)

    # Área de texto para mostrar resultados
    resultado_text = tk.Text(datos_window, width=60, height=10)
    resultado_text.grid(row=n+4, column=0, columnspan=2, padx=5, pady=5)

def main():
    root = tk.Tk()
    root.title("Derivada mediante Regresión Polinomial")

    ttk.Label(root, text="Número de puntos de datos (n):").grid(row=0, column=0, sticky="W", padx=5, pady=5)
    global n_entry
    n_entry = ttk.Entry(root, width=10)
    n_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Button(root, text="Ingresar Datos", command=solicitar_datos_regresion).grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
