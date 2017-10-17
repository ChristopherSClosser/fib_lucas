"""Test for fibinachi sequence."""


def test_fibonacci(fib_sequence):
    """Test fibonacci list for fibonacci pattern."""
    from fib import fibonacci
    for i in fib_sequence:
        assert fibonacci((fib_sequence[i]) + (fib_sequence[i + 1])) \
            == fib_sequence[i + 2]
