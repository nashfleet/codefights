"""
You found two items in a treasure chest! The first item weighs
    weight1 and is worth value1, and the second item weighs
    weight2 and is worth value2. What is the total maximum value
    of the items you can take with you, assuming that your max
    weight capacity is maxW and you can't come back for the
    items later?
"""


def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    elif weight1 <= maxW and (value1 >= value2 or weight2 >= maxW):
        return value1
    elif weight2 <= maxW and (value2 >= value1 or weight1 >= maxW):
        return value2
    else:
        return 0
