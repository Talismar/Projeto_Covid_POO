def aritmetrica(x,y,soma=False, subtracao=False):
    if soma:
        return x + y
    if subtracao:
        return x - y

print(aritmetrica(5,6,soma=True))