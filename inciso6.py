import numpy as np

# Inciso 6.1: Sistema de ecuaciones 1
A1 = np.array([[-0.10, 1.00],
               [0.11, -1.00]])
b1 = np.array([-2.0, 2.1])

# Solución exacta del sistema de ecuaciones 1
solucion1 = np.linalg.solve(A1, b1)

# Inciso 6.2: Sistema de ecuaciones 2
A2 = np.array([[-0.10, 1.00],
               [0.11, -1.00]])
b2 = np.array([-2.00, 2.14])

# Solución exacta del sistema de ecuaciones 2
solucion2 = np.linalg.solve(A2, b2)

# Inciso 6.3: Evaluación del número de condición de la matriz de coeficientes
kappa_A = np.linalg.cond(A1)

# Inciso 6.4: Cálculo del determinante y eigenvalores de la matriz de coeficientes
determinante_A = np.linalg.det(A1)
eigenvalores_A = np.linalg.eigvals(A1)

# Resultados
print("Inciso 6.1 - Solución del sistema 1 (x, y):", solucion1)
print("Inciso 6.2 - Solución del sistema 2 (x, y):", solucion2)
print("Inciso 6.3 - Número de condición κ de la matriz de coeficientes:", kappa_A)
print("Inciso 6.4 - Determinante de la matriz de coeficientes:", determinante_A)
print("Inciso 6.4 - Eigenvalores de la matriz de coeficientes:", eigenvalores_A)
