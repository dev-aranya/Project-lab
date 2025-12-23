# Secant Method for finding roots of nonlinear equations

def f(x):
    # Example: f(x) = x^3 - x - 2
    return x**3 - x - 2

def secant(x0, x1, tol=1e-6, max_iter=20):
    print(f"{'Iter':<5}{'x0':<15}{'x1':<15}{'x2':<15}{'Error':<15}{'% Error':<15}")
    for i in range(1, max_iter+1):
        f0 = f(x0)
        f1 = f(x1)
        if f1 - f0 == 0:
            print("Division by zero in secant formula.")
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        error = abs(x2 - x1)
        pct_error = (error / abs(x2)) * 100 if x2 != 0 else 0
        print(f"{i:<5}{x0:<15.8f}{x1:<15.8f}{x2:<15.8f}{error:<15.8f}{pct_error:<15.8f}")
        if error < tol:
            print(f"\nRoot found: {x2:.8f}")
            break
        x0, x1 = x1, x2

# Initial guesses
x0 = 1.0
x1 = 2.0
secant(x0, x1)
