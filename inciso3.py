import numpy as np

# Definimos las matrices A y B
A = np.array([[1, 4], [0.22, 1]])
B = np.array([[3, 5], [-2, 2]])

def calcular_normas_y_condicionamiento(A, B):
    # Inciso 3.1: Cálculo de las normas ||A||_1, ||A||_2 y ||A||_∞
    norm_A_1 = np.linalg.norm(A, ord=1)
    norm_A_2 = np.linalg.norm(A, ord='fro')
    norm_A_inf = np.linalg.norm(A, ord=np.inf)
    
    norm_B_1 = np.linalg.norm(B, ord=1)
    norm_B_2 = np.linalg.norm(B, ord='fro')
    norm_B_inf = np.linalg.norm(B, ord=np.inf)

    # Cálculo de las inversas de A y B
    A_inv = np.linalg.inv(A)
    B_inv = np.linalg.inv(B)

    # Cálculo de las normas ||A^-1||_1, ||A^-1||_2 y ||A^-1||_∞
    norm_A_inv_1 = np.linalg.norm(A_inv, ord=1)
    norm_A_inv_2 = np.linalg.norm(A_inv, ord='fro')
    norm_A_inv_inf = np.linalg.norm(A_inv, ord=np.inf)
    
    norm_B_inv_1 = np.linalg.norm(B_inv, ord=1)
    norm_B_inv_2 = np.linalg.norm(B_inv, ord='fro')
    norm_B_inv_inf = np.linalg.norm(B_inv, ord=np.inf)

    # Inciso 3.2: Cálculo del número de condicionamiento para A y B
    kappa_A_1 = norm_A_1 * norm_A_inv_1
    kappa_A_2 = norm_A_2 * norm_A_inv_2
    kappa_A_inf = norm_A_inf * norm_A_inv_inf
    
    kappa_B_1 = norm_B_1 * norm_B_inv_1
    kappa_B_2 = norm_B_2 * norm_B_inv_2
    kappa_B_inf = norm_B_inf * norm_B_inv_inf

    # Inciso 3.3: Cálculo del determinante (valor absoluto)
    det_A = np.abs(np.linalg.det(A))
    det_B = np.abs(np.linalg.det(B))

    # Resultados para cada inciso
    print("Respuesta inciso 3.1:")
    print("||A||_2:", norm_A_2)
    print("||B||_2:", norm_B_2)   
    print("||A^-1||_2:", norm_A_inv_2)
    print("||B^-1||_2:", norm_B_inv_2)

    print("\nRespuesta inciso 3.2 (Número de condicionamiento):")
    print("Número de condicionamiento kappa_2 para A:", kappa_A_2)
    print("Número de condicionamiento kappa_2 para B:", kappa_B_2)

    print("\nRespuesta inciso 3.3 (Determinante):")
    print("Determinante de A (pequeñez):", det_A)
    print("Determinante de B (pequeñez):", det_B)

    print("\nRespuesta inciso 3.4:")
    if kappa_A_2 < 10:
        print("La matriz A está bien condicionada.")
    else:
        print("La matriz A está mal condicionada.")

    if kappa_B_2 < 10:
        print("La matriz B está bien condicionada.")
    else:
        print("La matriz B está mal condicionada.")

# Llamamos a la función para resolver el problema
calcular_normas_y_condicionamiento(A, B)
