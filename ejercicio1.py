def funcion(x, y):
    if x <= 0 or y <= 0:
        print("deben ser no negativos")
        return -1
    if x == 1 or y == 1:
        return 1
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x
