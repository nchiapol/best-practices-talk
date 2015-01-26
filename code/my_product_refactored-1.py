from my_math import my_product, my_sum

def my_func(numbers):
    """ Difference between sum and product of sequence. """
    sum_value = my_sum(numbers)
    product_value = my_product(numbers)
    return product_value - sum_value
