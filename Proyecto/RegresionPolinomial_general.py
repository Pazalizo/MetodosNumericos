import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate as tab
import tkinter as tk
from tkinter import ttk

def calcular_derivada_regresion():
    # Obtener datos de entrada
    x_values = [float(entry.get()) for entry in x_entries]
    y_values = [float(entry.get()) for entry in y_entries]
    grado = int(grado_entry.get())
    x0 = float(x0_entry.get())

    # Ajustar polinomio
    coeficientes = np.polyfit(x_values, y_values, grado)
    polinomio = np.poly1d(coeficientes)

    # Calcular derivada del polinomio
    derivada_polinomio = np.polyder(polinomio)

    # Evaluar polinomio y su derivada en x0
    valor_en_x0 = polinomio(x0)
    derivada_en_x0 = derivada_polinomio(x0)

    # Mostrar resultados
    resultado_label.config(text=f"En x0 = {x0}:\nPolinomio ajustado: y(x0) = {valor_en_x0:.6f}\nDerivada: y'(x0) = {derivada_en_x0:.6f}")

    # Graficar
    x_grafica = np.linspace(min(x_values), max(x_values), 100)
    y_grafica = polinomio(x_grafica)
    y_derivada = derivada_polinomio(x_grafica)

    plt.figure(figsize=(10, 6))
    plt.plot(x_grafica, y_grafica, label='Polinomio Ajustado')
    plt.plot(x_grafica, y_derivada, label='Derivada del Polinomio', linestyle='--')
    plt.scatter(x_values, y_values, color='red', label='Datos Originales')
    plt.axvline(x0, color='green', linestyle=':', label=f'x0 = {x0}')
    plt.title('Regresión Polinomial y su Derivada')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def solicitar_datos_regresion():
    n = int(n_entry.get())

    # Crear ventana para ingresar datos
    datos_window = tk.Toplevel()
    datos_window.title("Ingresar Datos")

    global x_entries, y_entries
    x_entries = []
    y_entries = []

    ttk.Label(datos_window, text="x").grid(row=0, column=0)
    ttk.Label(datos_window, text="y").grid(row=0, column=1)

    for i in range(n):
        x_entry = ttk.Entry(datos_window, width=10)
        x_entry.grid(row=i+1, column=0, padx=5, pady=5)
        x_entries.append(x_entry)

        y_entry = ttk.Entry(datos_window, width=10)
        y_entry.grid(row=i+1, column=1, padx=5, pady=5)
        y_entries.append(y_entry)

    ttk.Label(datos_window, text="Grado del Polinomio:").grid(row=n+1, column=0, sticky="W")
    global grado_entry
    grado_entry = ttk.Entry(datos_window, width=10)
    grado_entry.grid(row=n+1, column=1)

    ttk.Label(datos_window, text="Punto x0 para derivada:").grid(row=n+2, column=0, sticky="W")
    global x0_entry
    x0_entry = ttk.Entry(datos_window, width=10)
    x0_entry.grid(row=n+2, column=1)

    ttk.Button(datos_window, text="Calcular Derivada", command=calcular_derivada_regresion).grid(row=n+3, column=0, columnspan=2, pady=10)

    global resultado_label
    resultado_label = ttk.Label(datos_window, text="")
    resultado_label.grid(row=n+4, column=0, columnspan=2)

def main():
    root = tk.Tk()
    root.title("Derivada mediante Regresión")

    ttk.Label(root, text="Número de puntos de datos:").grid(row=0, column=0, sticky="W")
    global n_entry
    n_entry = ttk.Entry(root, width=10)
    n_entry.grid(row=0, column=1)

    ttk.Button(root, text="Ingresar Datos", command=solicitar_datos_regresion).grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
