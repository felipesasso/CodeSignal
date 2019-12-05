def get_base_b_repr(n, b):
    base = ""
    while n != 0:
        n, base = n // b, str(n % b) + base
    return base


def max_zeros(n):
    """ Given a decimal integer n, find an integer k ≥ 2 such that the
        representation of n in base k has the maximum possible number of zeros.
        If there are several answers, output the smallest one.
    """
    max_zeros = 0
    max_base = 0
    for i in range(2, 126):
        repr = get_base_b_repr(n, i)
        count_zeros = repr.count("0")
        if count_zeros > max_zeros:
            max_zeros = count_zeros
            max_base = i
    return max_base


def max_subarray(inputArray):
    """ Given an array of integers inputArray, find the contiguous subarray
        which has the maximum sum. Return that sum.
    """
    best_sum = 0
    current_sum = 0

    for n in inputArray:
        current_sum = max(0, current_sum + n)
        best_sum = max(best_sum, current_sum)

    return best_sum
