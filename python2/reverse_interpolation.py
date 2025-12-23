"""
Inverse Interpolation:
----------------------
We are given points (x, f(x)) and a target value y0 = f(x_target).
We swap roles of x and y and use Lagrange interpolation to find x_target.
"""

def inverse_interpolation(x_values, y_values, y_target):
    n = len(x_values)
    x_target = 0.0

    for i in range(n):
        term = x_values[i]
        for j in range(n):
            if j != i:
                term *= (y_target - y_values[j]) / (y_values[i] - y_values[j])
        x_target += term

    return x_target

# Example data: f(x) = x^3
x_points = [1, 2, 3]
y_points = [1, 8, 27]  # f(x) = x^3

y_target = 9  # We want x such that x^3 ≈ 9

x_est = inverse_interpolation(x_points, y_points, y_target)

print(f"Estimated x for f(x) = {y_target} is x ≈ {x_est}")
