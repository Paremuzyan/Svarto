import time
from Svarto.algorithms.searching_algorithms.binary_search import binary_search


def timer(f):
    def execution_time(*args, **kwargs):
        start = time.time()
        if args:
            f(*args)
        else:
            f(**kwargs)
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
    test_b = timer(binary_search)
    test_b([1,2,3,4], 0, 3, 3)
