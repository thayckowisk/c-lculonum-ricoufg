import numpy as np

# Configurações para exibir resultados com precisão e sem notação científica
np.set_printoptions(precision=6, suppress=True)

# Definindo a matriz de coeficientes A e o vetor de constantes b
A = np.array([
    [1, 1, 0, 0, 0],
    [1, 2, 1, 0, 0],
    [0, 1, 2.001, 0, 0],
    [0, 0, 1, 2, 1],
    [0, 0, 0, 1, 1]
], dtype=float)
b = np.array([1, 1, 1, 1, 1], dtype=float)

# Funções de solução
def eliminacao_gaussiana(A, b):
    return np.linalg.solve(A, b), 1

def jacobi(A, b, tol=1e-2, max_iter=100000):
    n = len(b)
    x = np.zeros_like(b)
    for it in range(1, max_iter + 1):
        x_novo = np.copy(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_novo[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x - x_novo, ord=np.inf) < tol:
            return x_novo, it
        x = x_novo
    return x, max_iter

def gauss_seidel(A, b, tol=1e-2, max_iter=100000):
    n = len(b)
    x = np.zeros_like(b)
    for it in range(1, max_iter + 1):
        x_novo = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_novo[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_novo[i] = (b[i] - s1 - s2) / A[i][i]
        if np.linalg.norm(x - x_novo, ord=np.inf) < tol:
            return x_novo, it
        x = x_novo
    return x, max_iter

# Executando os métodos com tolerância de 10^-2
results = {
    "Eliminação Gaussiana": eliminacao_gaussiana(A, b),
    "Método de Jacobi": jacobi(A, b),
    "Método de Gauss-Seidel": gauss_seidel(A, b)
}

# Exibindo resultados
for method, (solution, iterations) in results.items():
    print(f"{method}:\nSolução: {solution}\nIterações: {iterations}\n")
