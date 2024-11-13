import numpy as np

# Definimos la matriz A
A = np.array([[1, 0, -4, 1],
              [4, 5, 7, 0],
              [1, -2, 0, 3]])

# Norma 1 (norma de columnas)
norma_1 = np.max(np.sum(np.abs(A), axis=0))

# Norma de Frobenius
norma_frobenius = np.sqrt(np.sum(A**2))

# Norma infinita (norma de filas)
norma_infinita = np.max(np.sum(np.abs(A), axis=1))

# Imprimimos los resultados
print("Norma 1 (columna):", norma_1)
print("Norma de Frobenius:", norma_frobenius)
print("Norma Infinita (fila):", norma_infinita)
