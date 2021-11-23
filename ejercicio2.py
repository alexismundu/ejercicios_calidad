def maximo(x,y,z):
    max=0
    if x>y and x>z:
        max=x
    else:
        if z>y:
            max=z
        else:
            max=y
    print(max)
    return max
