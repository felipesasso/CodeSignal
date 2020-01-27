def reverse_integer(x):
    ''' Reverse the digits of the given integer
    '''
    x = str(x)
    return int(''.join(reversed((x[1 if x[0] == '-' else 0:]) +\
                                ('-' if x[0] == '-' else ''))))
