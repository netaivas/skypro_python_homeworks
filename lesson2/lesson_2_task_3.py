import math

def square():
    side = float(input("Сторона квадрата: "))
    S = (side) * (side)
    print(math.ceil(S))


square()