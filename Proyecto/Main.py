import tkinter as tk

def biseccion():
    import Biseccion_general
    Biseccion_general.main()

def Newton():
    import Newton_general as Newton_general
    Newton_general.main()

def RegresionPolinomial():
    import RegresionPolinomial_general
    RegresionPolinomial_general.main()

def ReglaTrapecio():
    import ReglaTrapecio_general
    ReglaTrapecio_general.main()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicativo con botón")

# Botones para los métodos
btn_bis = tk.Button(ventana, text="Metodo de biseccion", command=biseccion)
btn_bis.pack(pady=20)
btn_newton = tk.Button(ventana, text="Metodo de Newton", command=Newton)
btn_newton.pack(pady=20)
btn_regresion = tk.Button(ventana, text="Regresion Polinomial", command=RegresionPolinomial)
btn_regresion.pack(pady=20)

# Nuevo botón para el método de Regla del Trapecio
btn_trapecio = tk.Button(ventana, text="Regla del Trapecio", command=ReglaTrapecio)
btn_trapecio.pack(pady=20)

# Ejecutar el bucle principal
ventana.mainloop()