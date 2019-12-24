uber_type_dict = {
    1: "UberX",
    2: "UberXL",
    3: "UberPlus",
    4: "UberBlack",
    5: "UberSUV",
}


def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    """ Uber is building a Fare Estimator that can tell you how much your ride
        will cost before you request it. It works by passing approximated ride
        distance and ride time through this formula:

        (Cost per minute) * (ride time) + (Cost per mile) * (ride distance)

        where Cost per minute and Cost per mile depend on the car type.

        You are one of the engineers building the Fare Estimator, so knowing
        cost per minute and cost per mile for each car type, as well as ride
        distance and ride time, return the fare estimates for all car types.
    """
    return [
        round(ride_time * x + ride_distance * y, 2)
        for x, y in zip(cost_per_minute, cost_per_mile)
    ]


def fancyRide(l, fares):
    """ Being a new Uber user, you have $20 off your first ride. You want to
        make the most out of it and drive in the fanciest car you can afford,
        without spending any out-of-pocket money. There are 5 options, from
        the least to the most expensive: "UberX", "UberXL", "UberPlus",
        "UberBlack" and "UberSUV".

        You know the length l of your ride in miles and how much one mile
        costs for each car. Find the best car you can afford.
    """
    for index, fare in enumerate(fares, start=1):
        if fare * l > 20:
            continue
        else:
            best = index

    return uber_type_dict[best]
