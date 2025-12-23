import math

def cholesky_decomposition(A, b):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    # Cholesky Decomposition
    for i in range(n):
        for j in range(i+1):
            sum_val = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = math.sqrt(A[i][i] - sum_val)
            else:
                L[i][j] = (A[i][j] - sum_val) / L[j][j]

    # Forward substitution: L*y = b
    y = [0.0] * n
    for i in range(n):
        y[i] = (b[i] - sum(L[i][k] * y[k] for k in range(i))) / L[i][i]

    # Backward substitution: L^T*x = y
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(L[k][i] * x[k] for k in range(i+1, n))) / L[i][i]

    return L, x

# Example: Symmetric positive-definite matrix
A = [
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]
]
b = [1, 2, 3]

L, x_cholesky = cholesky_decomposition(A, b)
print("Cholesky L matrix:")
for row in L:
    print(row)

print("\nSolution (Cholesky):", x_cholesky)
