import math
from linear_search import linear_search


def jump_search(sorted_arr, el):
    n = len(sorted_arr)
    m = int(math.sqrt(n))
    i = 0
    while sorted_arr[i] < el and i != n - 1:
        if sorted_arr[i+m-1] == el:
            return i+m-1
        elif sorted_arr[i+m-1] > el:
            B = sorted_arr[i: i+m-1]
            return linear_search(B, el)
        if i + m < n-1:
            i += m
        else:
            return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(jump_search(arr, 3))
