# LU Decomposition Method

def lu_decomposition(a, b):
    n = len(a)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    # Decomposition into L and U
    for i in range(n):
        # Upper Triangular
        for k in range(i, n):
            sum_u = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = a[i][k] - sum_u

        # Lower Triangular
        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0
            else:
                sum_l = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (a[k][i] - sum_l) / U[i][i]

    # Solve L*y = b (Forward substitution)
    y = [0.0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    # Solve U*x = y (Backward substitution)
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]

    return L, U, x



A = [
    [2, 3, 1],
    [4, 1, 5],
    [-2, 5, 2]
]
B = [9, 23, 7]

L, U, solution = lu_decomposition(A, B)

print("L matrix:")
for row in L:
    print(row)

print("\nU matrix:")
for row in U:
    print(row)

print("\nSolution:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.6f}")
