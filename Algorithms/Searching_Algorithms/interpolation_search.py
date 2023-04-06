def interpolation_search(arr, lo, hi, x):
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolation_search(arr, pos + 1,
                                       hi, x)
        if arr[pos] > x:
            return interpolation_search(arr, lo,
                                       pos - 1, x)
    return -1


if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20,
           21, 22, 23, 24, 33, 35, 42, 47]
    n = len(arr)
    x = 18
    index = interpolation_search(arr, 0, n - 1, x)
    print(index)
