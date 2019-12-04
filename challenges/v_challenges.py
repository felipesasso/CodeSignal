def visits_on_circular_road(n, visits_order):
    """ There are n houses in a village on a circular road numbered from 1 to n
        starting from some house in clockwise order. It takes one minute to get
        from one house to any of two adjacent houses and there are no other
        roads in this village besides the circular one. Find the minimal time
        required to make all visits in the desired order starting from house 1.
    """
    res = 0
    pre = 1
    for i in range(len(visits_order)):
        dist = (visits_order[i] - pre + n) % n
        dist = min(dist, n - dist)
        res += dist
        pre = visits_order[i]

    return res
