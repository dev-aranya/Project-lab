# Gauss-Seidel Method

def gauss_seidel(a, b, x_init=None, tol=1e-6, max_iter=100):
    n = len(b)
    x = [0.0] * n if x_init is None else x_init[:]

    print(f"{'Iter':<5}" + "".join([f"x{i+1:<15}" for i in range(n)]) + "Error")
    
    for iteration in range(1, max_iter + 1):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = sum(a[i][j] * x[j] for j in range(i))
            sum2 = sum(a[i][j] * x_old[j] for j in range(i+1, n))
            x[i] = (b[i] - sum1 - sum2) / a[i][i]
        
        # Calculate error
        error = max(abs(x[i] - x_old[i]) for i in range(n))
        
        print(f"{iteration:<5}" + "".join([f"{x[i]:<15.8f}" for i in range(n)]) + f"{error:.8f}")
        
        if error < tol:
            print("\nSolution converged.")
            break
    return x

# Example system:
# 4x +  y +  z = 7
#  x + 3y +  z = -8
#  x +  y + 5z = 6

A = [
    [4, 1, 1],
    [1, 3, 1],
    [1, 1, 5]
]
B = [7, -8, 6]

solution = gauss_seidel(A, B, x_init=[0, 0, 0])
print("\nFinal Solution:", solution)
