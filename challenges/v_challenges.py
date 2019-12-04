def visits_on_circular_road(n, visits_order):
    res = 0
    pre = 1
    for i in range(len(visits_order)):
        dist = (visits_order[i] - pre + n) % n
        dist = min(dist, n - dist)
        res += dist
        pre = visits_order[i]

    return res
