import math


def roots(a, b, c):
    discriminant = (b ** 2) - 4 * a * c
    print(discriminant)
    if discriminant > 0:
        x_1 = -b + (math.sqrt(discriminant) / 2*a)
        x_2 = -b - (math.sqrt(discriminant) / 2*a)
        return f"x_1 for {a}x2 + {b}x + c is {x_1}, x_2 is {x_2}"
    elif discriminant < 0:
        return f"{a}x2 + {b}x + c dont have a solution"
    else:
        x_1_2 = -b / (2 * a)
        return f"x_1, x_2 for {a}x2 + {b}x + c is {x_1_2}"


if __name__ == "__main__":
    print(roots(5, 4, 3))
