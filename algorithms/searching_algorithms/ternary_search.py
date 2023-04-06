def ternary_search(start, end, key, arr):
    if end >= start:
        mid_1 = start + (end - start) // 3
        mid_2 = end - (end - start) // 3 
        if arr[mid_1] == key:
            return mid_1
        if arr[mid_2] == key:
            return mid_2
        if key < arr[mid_1]:
            return ternary_search(start, mid_1 - 1, key, arr)
        elif key > arr[mid_2]:
            return ternary_search(mid_2 + 1, end, key, arr)
        else:
            return ternary_search(mid_1 + 1, mid_2 - 1, key, arr)
    else:
        return -1


if __name__ == "__main__":
    lst = [1, 2, 3, 5, 7, 9, 11, 13, 16]
    print(ternary_search(0, len(lst) -1, 345678, lst))
