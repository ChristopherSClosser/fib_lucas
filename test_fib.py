"""Test for fibinachi sequence."""


def test_fibonacci():
    """Test fibonacci list for fibonacci pattern."""
    from fib import fibonacci
    fib_list = fibonacci(0)
    print(fib_list)
    correct_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for i in range(len(fib_list)):
        print(fib_list[i], correct_list[i])
        assert fib_list[i] is correct_list[i]
