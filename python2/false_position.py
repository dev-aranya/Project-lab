def false_position(f, a, b, iterations):
    # Exact root for error calculation
    exact_root = 4 ** (1/3)

    # Store results
    results = []

    for i in range(iterations + 1):
        # False position formula
        fa = f(a)
        fb = f(b)
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)

        # Error calculations
        error = abs(exact_root - x)
        percent_error = (error / abs(exact_root)) * 100

        results.append((i, a, b, x, fx, error, percent_error))

        # Update interval
        if fa * fx < 0:
            b = x
        else:
            a = x

    return results


if __name__ == "__main__":
    def func(x):
        return x**3 - 4

    results = false_position(func, 1, 3, 3)

    print(f"{'Iter':<5}{'a':<12}{'b':<12}{'x':<12}{'f(x)':<12}{'Error':<12}{'%Error':<12}")
    for i, a, b, x, fx, err, perr in results:
        print(f"{i:<5}{a:<12.6f}{b:<12.6f}{x:<12.6f}{fx:<12.6f}{err:<12.6e}{perr:<12.6f}")
