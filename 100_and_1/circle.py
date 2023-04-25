import math


def area(r):
    return math.pi * (r ** 2)


def circumference(r):
    return 2 * math.pi * r


if __name__ == "__main__":
    print(area(5))
    print(circumference(5))
