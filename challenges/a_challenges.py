def arithmetic_expression(a, b, c):
    ''' Consider an arithmetic expression of the form a#b=c.
        Check whether it is possible to replace # with one of the four signs:
        +, -, * or / to obtain a correct expression.
    '''
    return c in (a+b, a-b, a*b, a/b)
