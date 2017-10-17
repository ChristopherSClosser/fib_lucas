"""Test for lucas sequence."""


# def test_lucas():
#     """Test lucas list for lucas pattern."""
#     from lucas import lucas
#     from fib import fib_list
#     index = 0
#     for i in fib_list:
#         assert fibonacci((fib_list[index]) + (fib_list[index + 1])) \
#             == fib_list[index + 2]
#         index += 1

CORRECT_LIST = [2, 1, 3, 4, 7, 11, 18, 29]


def test_lucas_1():
    """Test lucas for corect item at index."""
    from lucas import lucas_list
    result = lucas_list(0)
    assert result == CORRECT_LIST[0]


def test_lucas_2():
    """Test lucas for corect item at index."""
    from lucas import lucas_list
    result = lucas_list(1)
    assert result == CORRECT_LIST[1]
