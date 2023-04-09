import time


def timer(f):
    def execution_time():
        start = time.time()
        f()
        end = time.time()
        print(f"Execution time for {f.__name__} function is {end - start} seconds")
    return execution_time


@timer
def test_func():
    sum = 0
    for i in range(1000):
        sum += 1
    print(sum)


if __name__ == "__main__":
    test_func()
