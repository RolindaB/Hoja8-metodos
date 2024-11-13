import numpy as np

# Definimos las matrices A y B
A = np.array([[0.33, 1], [1, 3]])
B = np.array([[4, 4], [3, 5]])

def calcular_normas_y_condicionamiento_preciso(A, B):
    # 2.1 Cálculo de las normas ||A||_2 y ||B||_2 (norma espectral)
    norm_A_2 = np.linalg.norm(A, 2)
    norm_B_2 = np.linalg.norm(B, 2)
    
    # Cálculo de las inversas de A y B, y sus normas si son invertibles
    try:
        A_inv = np.linalg.inv(A)
        norm_A_inv_2 = np.linalg.norm(A_inv, 2)
    except np.linalg.LinAlgError:
        norm_A_inv_2 = None  # No es invertible

    try:
        B_inv = np.linalg.inv(B)
        norm_B_inv_2 = np.linalg.norm(B_inv, 2)
    except np.linalg.LinAlgError:
        norm_B_inv_2 = None  # No es invertible

    # 2.2 Cálculo del número de condicionamiento kappa para A y B, si son invertibles
    kappa_A = norm_A_2 * norm_A_inv_2 if norm_A_inv_2 is not None else None
    kappa_B = norm_B_2 * norm_B_inv_2 if norm_B_inv_2 is not None else None
    
    # 2.3 Cálculo de la pequeñez del determinante (1 / |determinante|) si el determinante no es cero
    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)
    nu_A = 1 / abs(det_A) if det_A != 0 else None
    nu_B = 1 / abs(det_B) if det_B != 0 else None

    # Resultados
    resultados = {
        "||A||_2": norm_A_2,
        "||B||_2": norm_B_2,
        "||A^-1||_2": norm_A_inv_2,
        "||B^-1||_2": norm_B_inv_2,
        "kappa_A": kappa_A,
        "kappa_B": kappa_B,
        "nu_A": nu_A,
        "nu_B": nu_B
    }
    return resultados

# Calculamos todos los valores
resultados = calcular_normas_y_condicionamiento_preciso(A, B)

# Mostramos los resultados por inciso
print("Respuesta inciso 2.1:")
print("||A||_2:", resultados["||A||_2"])
print("||B||_2:", resultados["||B||_2"])
print("||A^-1||_2:", resultados["||A^-1||_2"])
print("||B^-1||_2:", resultados["||B^-1||_2"])

print("\nRespuesta inciso 2.2:")
print("Número de condicionamiento kappa para A:", resultados["kappa_A"])
print("Número de condicionamiento kappa para B:", resultados["kappa_B"])

print("\nRespuesta inciso 2.3:")
print("Pequeñez del determinante de A (nu_A):", resultados["nu_A"])
print("Pequeñez del determinante de B (nu_B):", resultados["nu_B"])

print("\nRespuesta inciso 2.4:")
if resultados["kappa_A"] is not None and resultados["kappa_A"] < 10:
    print("La matriz A está bien condicionada.")
else:
    print("La matriz A está mal condicionada.")

if resultados["kappa_B"] is not None and resultados["kappa_B"] < 10:
    print("La matriz B está bien condicionada.")
else:
    print("La matriz B está mal condicionada.")

