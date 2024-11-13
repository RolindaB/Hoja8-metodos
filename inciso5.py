import numpy as np

# Matriz inicial
matriz = np.array([
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
])

# Número de condición utilizando normas de Frobenius
norma_matriz = np.linalg.norm(matriz, 'fro')
norma_inversa = np.linalg.norm(np.linalg.inv(matriz), 'fro')
condicion_matriz = norma_matriz * norma_inversa

# Determinante de la matriz
determinante = np.linalg.det(matriz)

# Valor absoluto del determinante
magnitud_determinante = abs(determinante)

# Valores propios de la matriz
valores_propios = np.linalg.eigvals(matriz)

# Resultados
print("Inciso 5.1 - Número de condición κ:", condicion_matriz)
print("Inciso 5.2 - Determinante:", determinante)
print("Inciso 5.3 - Pequeñez del determinante:", magnitud_determinante)
print("Inciso 5.4 - Eigenvalores:", valores_propios)

