from binary_search import binary_search


def exponential_search(sorted_array, x):
    if not sorted_array:
        return -1
    bound = 1
    while bound < len(sorted_array) and sorted_array[bound] < x:
        bound *= 2
    return binary_search(sorted_array, bound // 2, min(bound, len(sorted_array) - 1), x)


if __name__ == "__main__":
    sorted_list = [1, 2, 3, 5, 7, 9, 11, 13, 16]
    el = 7789
    result = exponential_search(sorted_list, el)

    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")
