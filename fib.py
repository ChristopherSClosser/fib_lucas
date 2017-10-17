"""Fibinachi sequence."""


def fibonacci(n):
    """Fibinachi sequence function."""
    fib_list = []
    fib_list.append(n)
    fib_list.append(n + 1)
    for i in range(10):
        fib_list.append(fib_list[i] + fib_list[i + 1])
