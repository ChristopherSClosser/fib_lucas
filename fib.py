"""Fibinachi sequence."""


fib_list = []


def fibonacci(n):
    """Fibinachi sequence function."""
    fib_list.append(n)
    fib_list.append(n + 1)
    for i in range(10):
        # print(fib_list)
        fib_list.append(fib_list[i] + fib_list[i + 1])
    # for i in fib_list:
    #     print(fib_list[i])
    return fib_list
