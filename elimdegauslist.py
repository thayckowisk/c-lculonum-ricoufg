def gauss_elimination_with_pivoting(A, b):
    n = len(b)
    
    # Construir a matriz aumentada
    for i in range(n):
        # Pivotamento parcial
        max_row = max(range(i, n), key=lambda k: abs(A[k][i]))
        if i != max_row:
            # Trocar linhas na matriz A e no vetor b
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
        
        # Eliminação Gaussiana
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            b[j] -= factor * b[i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
    
    return A, b

# Função para resolver uma matriz triangular superior
def solveUpperTriangularMatrix(U, b):
    n = len(b)
    x = [0] * n
    x[n-1] = b[n-1] / U[n-1][n-1]
    
    for i in range(n - 2, -1, -1):
        s = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - s) / U[i][i]
    return x

# Dados do problema
A = [[1, 1, 1],
     [2, 1, 1],
     [2, 2, 1]]
b = [1, 0, 1]

# Aplicando Eliminação de Gauss com Pivotamento Parcial
U, new_b = gauss_elimination_with_pivoting(A, b)

# Resolvendo o sistema triangular superior
x = solveUpperTriangularMatrix(U, new_b)

print("Solução do sistema:")
print("x =", x)
