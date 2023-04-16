def fib():
    fib_1 = 0
    fib_2 = 1
    i = 0
    print(fib_1)
    while i < 10:
        print(fib_2)
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        i += 1


if __name__ == "__main__":
    fib()
