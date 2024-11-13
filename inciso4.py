import numpy as np

# Definimos las matrices A y B
A2 = np.array([[0.33, 1], [1, 3]])
B2 = np.array([[4, 4], [3, 5]])

A3 = np.array([[1, 4], [0.22, 1]])
B3 = np.array([[3, 5], [-2, 2]])

def calcular_normas_y_condicionamiento_con_norma_inf(A, B):
    # Cálculo de la norma infinito para A y B
    norm_A_inf = np.linalg.norm(A, ord=np.inf)
    norm_B_inf = np.linalg.norm(B, ord=np.inf)

    # Cálculo de las inversas de A y B, y de su norma infinito si son invertibles
    try:
        A_inv = np.linalg.inv(A)
        norm_A_inv_inf = np.linalg.norm(A_inv, ord=np.inf)
    except np.linalg.LinAlgError:
        norm_A_inv_inf = None  # No es invertible

    try:
        B_inv = np.linalg.inv(B)
        norm_B_inv_inf = np.linalg.norm(B_inv, ord=np.inf)
    except np.linalg.LinAlgError:
        norm_B_inv_inf = None  # No es invertible

    # Cálculo del número de condicionamiento kappa infinito para A y B
    kappa_A_inf = norm_A_inf * norm_A_inv_inf if norm_A_inv_inf is not None else None
    kappa_B_inf = norm_B_inf * norm_B_inv_inf if norm_B_inv_inf is not None else None

    # Resultado de si están bien condicionadas según kappa infinito
    condicion_A = "bien condicionada" if kappa_A_inf is not None and kappa_A_inf < 10 else "mal condicionada"
    condicion_B = "bien condicionada" if kappa_B_inf is not None and kappa_B_inf < 10 else "mal condicionada"

    # Mostramos los resultados
    print(f"||A||_inf: {norm_A_inf}")
    print(f"||B||_inf: {norm_B_inf}")
    print(f"||A^-1||_inf: {norm_A_inv_inf}")
    print(f"||B^-1||_inf: {norm_B_inv_inf}")
    print(f"Número de condicionamiento kappa_inf para A: {kappa_A_inf}")
    print(f"Número de condicionamiento kappa_inf para B: {kappa_B_inf}")
    print(f"La matriz A está {condicion_A}.")
    print(f"La matriz B está {condicion_B}.")

# Llamamos a la función con las matrices de los incisos 2 y 3
print("Resultados para el inciso 2 usando norma de filas:")
calcular_normas_y_condicionamiento_con_norma_inf(A2, B2)

print("\nResultados para el inciso 3 usando norma de filas:")
calcular_normas_y_condicionamiento_con_norma_inf(A3, B3)
