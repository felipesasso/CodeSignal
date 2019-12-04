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
