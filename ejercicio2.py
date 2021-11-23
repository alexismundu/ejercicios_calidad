def maximo(x, y, z):
    if x > y and x > z:
        return x
    return z if z > y else y
