def maximo(x, y, z):
    max = None
    if x > y and x > z:
        max = x
    elif z > y:
        max = z  
    else:
        max = y
    print("El máximo es: " + str(max))