try:
    my_product(1,2,3)
except TypeError:
    print "'my_product' expects a sequence"
    raise TypeError