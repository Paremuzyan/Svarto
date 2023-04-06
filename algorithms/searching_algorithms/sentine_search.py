def sentine_search(lst, n, el):
    last = lst[-1]
    lst[-1] = el
    i = 0
    while lst[i] != el:
        i += 1
    lst[-1] = last
    if (i < n-1) or (lst[-1] == el):
        return f"Index of {el} is {i}"
    else:
        return f"{el} not found!"


if __name__ == "__main__":
    lst = [5, 8, 78, 6, 9, 56, 3456, 987, 567, 9876, 234, 9876, 64]
    n = len(lst)
    el = 10

    print(sentine_search(lst, n, el))
