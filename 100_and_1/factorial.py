def factorial(num):
    result = 1
    while num:
        result *= num
        num -= 1
    return result


if __name__ == "__main__":
    print(factorial(5))
