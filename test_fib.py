"""Test for fibinachi sequence."""


def test_fibonacci():
    """Test fibonacci list for fibonacci pattern."""
    from fib import fibonacci
    from fib import fib_list
    for i in fib_list:
        assert fibonacci((fib_list[i]) + (fib_list[i + 1])) \
            == fib_list[i + 2]
