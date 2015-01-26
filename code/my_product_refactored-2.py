from numpy import prod, sum

def my_func(numbers):
    """ Difference between sum and product of sequence. """
    sum_value = sum(numbers)
    product_value = prod(numbers)
    return product_value - sum_value
