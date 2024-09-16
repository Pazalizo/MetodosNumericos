import math

# Valor exacto de cos(pi/4)
x = math.pi / 4
cos_exacto = math.cos(x)

# Inicializamos variables
cos_approx = 0  # Almacenará la aproximación acumulada de la serie
error_aprox = None
n = 0  # Contador de términos
criterio_error = 0.01  # El criterio de error aproximado, se detendrá cuando sea menor que este

# Listas para almacenar resultados de cada iteración
resultados = []

# Bucle para calcular la serie de Maclaurin término por término
while True:
    # Calcular el término n-ésimo de la serie de Maclaurin
    termino = ((-1)**n * x**(2*n)) / math.factorial(2*n)
    
    # Sumar el término a la aproximación actual
    cos_approx_anterior = cos_approx
    cos_approx += termino
    
    # Calcular el error relativo exacto
    error_relativo_exacto = abs((cos_exacto - cos_approx) / cos_exacto) * 100
    
    # Calcular el error aproximado (comparando con la iteración anterior)
    if n > 0:
        error_aprox = abs((cos_approx - cos_approx_anterior) / cos_approx) * 100
    
    # Almacenar los resultados de esta iteración
    resultados.append([n, cos_approx, error_relativo_exacto, error_aprox if n > 0 else "N/A"])
    
    # Verificar si el criterio de error aproximado se cumple
    if error_aprox is not None and error_aprox < criterio_error:
        break
    
    n += 1

# Mostrar los resultados
print(f"Valor exacto de cos(pi/4) = {cos_exacto}")
print(f"Resultados de la aproximación usando la serie de Maclaurin:")
print(f"{'Iteración':<10} {'Aproximación':<20} {'Error Relativo Exacto (%)':<30} {'Error Aproximado (%)':<30}")
for res in resultados:
    print(f"{res[0]:<10} {res[1]:<20} {res[2]:<30} {res[3]}")
