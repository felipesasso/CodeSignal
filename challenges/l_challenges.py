import re
def last_digit_reg_exp(n):
    ''' Given a string with at least one digit,
        extract the rightmost digit from it.
    '''
    return re.findall(r'\d', n)[-1]
