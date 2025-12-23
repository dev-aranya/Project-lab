def bisection_method(f, x1, x2, E):
    f1 = f(x1)
    f2 = f(x2)

    if f1 * f2 > 0:
        raise ValueError("x1 and x2 do not bracket any root.")

    step = 0
    print(f"{'Step':<5} {'x1':<15} {'x2':<15} {'x0':<15} {'f(x0)':<15}")

    while True:
        step += 1
        x0 = (x1 + x2) / 2
        f0 = f(x0)

        # Print current step
        print(f"{step:<5} {x1:<15.10f} {x2:<15.10f} {x0:<15.10f} {f0:<15.10e}")

        if f0 == 0:
            return x0, step

        if f1 * f0 < 0:
            x2 = x0
            f2 = f0
        else:
            x1 = x0
            f1 = f0

        if abs(x2 - x1) / abs(x2) < E:
            return (x1 + x2) / 2, step


if __name__ == "__main__":
    def func(x):
        return 2*x**3 + 3*x - 1

    root, steps = bisection_method(func, 0, 1, 1e-8)
    print(f"\nRoot found: {root:.10f} in {steps} steps")
