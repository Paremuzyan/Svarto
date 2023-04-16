def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f"{c} °C is {f} °F"


def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    return f"{f} °F is {c} °C"


if __name__ == "__main__":
    print(celsius_to_fahrenheit(1))
    print(fahrenheit_to_celsius(33.9))
