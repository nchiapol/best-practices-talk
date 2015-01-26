def my_func(numbers):
    """ Difference between sum and product of sequence. """
    total = 0
    for item in numbers:
        total += item
    total2 = 1
    for item in numbers:
        total2 *= item
    return total2 - total
