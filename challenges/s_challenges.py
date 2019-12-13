def square_digits_sequence(a0):
    ''' Consider a sequence of numbers a0, a1, ..., an, in which an element is
        equal to the sum of squared digits of the previous element.
        The sequence ends once an element that has already been in the
        sequence appears again.
        Given the first element a0, find the length of the sequence.
    '''
    previous_numbers = set([a0])
    count = 1
    while True:
        a0 = sum([x**2 for x in map(int, str(a0))])
        count += 1
        if a0 in previous_numbers:
            return count
        previous_numbers.add(a0)
