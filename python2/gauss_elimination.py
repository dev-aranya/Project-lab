# Basic Gauss Elimination Method

def gauss_elimination(a, b):
    n = len(b)
    
    # Forward elimination
    for i in range(n):
        # Pivoting (optional for numerical stability)
        if a[i][i] == 0:
            for k in range(i+1, n):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]
                    b[i], b[k] = b[k], b[i]
                    break
        
        for j in range(i+1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= ratio * a[i][k]
            b[j] -= ratio * b[i]
    
    # Back substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        sum_ax = sum(a[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - sum_ax) / a[i][i]
    
    return x

# Example system:
# 2x + 3y -  z =  5
# 4x +  y + 5z =  6
# -2x + 5y + 2z = 7

A = [
    [2, 3, -1],
    [4, 1, 5],
    [-2, 5, 2]
]
B = [5, 6, 7]

solution = gauss_elimination(A, B)
print("Solution:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.6f}")
