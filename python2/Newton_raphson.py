# Newton-Raphson method using Horner's rule

def horner(coeffs, x):
    """Evaluates polynomial and its derivative using Horner's rule."""
    n = len(coeffs) - 1
    b = coeffs[0]
    c = b  # derivative array start
    for i in range(1, n):
        b = b * x + coeffs[i]
        c = c * x + b
    b = b * x + coeffs[n]
    return b, c  # f(x), f'(x)

def newton_raphson(coeffs, x0, tol=1e-6, max_iter=20):
    print(f"{'Iter':<5}{'x':<15}{'f(x)':<15}{'Error':<15}{'% Error':<15}")
    prev_x = x0
    for i in range(1, max_iter+1):
        fx, dfx = horner(coeffs, prev_x)
        if dfx == 0:
            print("Derivative zero. Stopping.")
            break
        x_new = prev_x - fx / dfx
        error = abs(x_new - prev_x)
        pct_error = (error / abs(x_new)) * 100 if x_new != 0 else 0
        print(f"{i:<5}{x_new:<15.8f}{fx:<15.8f}{error:<15.8f}{pct_error:<15.8f}")
        if error < tol:
            break
        prev_x = x_new

# Example polynomial: x^3 - x - 2 = 0
coeffs = [1, 0, -1, -2]  # 1*x^3 + 0*x^2 - 1*x - 2
x0 = 1.5
newton_raphson(coeffs, x0)
