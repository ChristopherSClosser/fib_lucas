"""Test for fibinachi sequence."""


CORRECT_LIST = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# def test_fibonacci():
#     """Test fibonacci list for fibonacci pattern."""
#     from fib import fibonacci
#     fib_list = fibonacci(0)
#     print(fib_list)

#     for i in range(len(fib_list)):
#         print(fib_list[i], CORRECT_LIST[i])
#         assert fib_list[i] is CORRECT_LIST[i]


def test_fib():
    """Test fibonacci for corect item at index."""
    from fib import fibinacci
    result = fibinacci(0)
    assert result == CORRECT_LIST[0]
