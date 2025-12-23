from sympy import symbols, expand

def lagrange_interpolation_polynomial(x_values, y_values):
    x = symbols('x')
    n = len(x_values)
    polynomial = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        polynomial += term

    return expand(polynomial)

# Example data points
x_points = [1, 2, 3]
y_points = [2, 3, 5]

# Find the polynomial
poly = lagrange_interpolation_polynomial(x_points, y_points)
print("Lagrange Interpolating Polynomial:")
print(poly)
