def number_of_operations(a, b):
    ''' For a pair of two positive integers a and b consider the following
        operation: if one of the integers is divisible by the other - replace
        this integer with the division result of the two.

        This operation is applied sequentially until it stops working.
        Return the number of times the operation is applied.
        It is guaranteed that the answer is a finite number.
    '''
    number_op = 0
    while True:
        if a % b == 0:
            a /= b
            number_op += 1
        elif b % a == 0:
            b /= a
            number_op += 1
        else:
            return number_op
