def largest_num(n_1, n_2, n_3):
    if n_1 > n_2 and n_1 > n_3:
        largest = n_1
    elif n_2 > n_1 and n_2 > n_3:
        largest = n_2
    else:
        largest = n_3
    return largest


def smallest_num(n_1, n_2, n_3):
    if n_1 < n_2 and n_1 < n_3:
        largest = n_1
    elif n_2 < n_1 and n_2 < n_3:
        largest = n_2
    else:
        largest = n_3
    return largest


def largest_smallest(n_1, n_2, n_3):
    largest = largest_num(n_1, n_2, n_3)
    smallest = smallest_num(n_1, n_2, n_3)
    print(f"The largest number is {largest}")
    print(f"The smallest number is {smallest}")


if __name__ == "__main__":
    largest_smallest(0.5, 2, 9)
