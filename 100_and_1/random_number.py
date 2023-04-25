import random


def random_number_in(start, stop):
    return random.randint(start, stop)


if __name__ == "__main__":
    print(random_number_in(0, 100))
