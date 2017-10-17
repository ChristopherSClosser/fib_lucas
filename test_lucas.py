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

lucas_correct_list = []
def test_lucas():
    """Test lucas list for lucas pattern."""
    for i in range(len(lucas_list)):
        print(lucas_list[i], lucas_correct_list[i])
        assert lucas_list[i] is lucas_correct_list[i]
