def factorial(num):
    result = 1
    while num:
        result *= num
        num -= 1
    return result


def factorial_recursive(num):
    if num == 1:
        return num
    else:
        return num * factorial_recursive(num - 1)


if __name__ == "__main__":
    # print(factorial(5))
    print(factorial_recursive(5))
