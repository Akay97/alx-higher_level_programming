#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    score = 0
    weight = 0

    for x_score, x_weight in my_list:
        score += x_score * x_weight
        weight += x_weight

    return score / weight
