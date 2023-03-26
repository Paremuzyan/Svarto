def binary_search(sorted_list, l, r, el):
    if r >= l:
        mid = l + (r - l)
        if sorted_list[mid] == el:
            return mid
        elif sorted_list[mid] > el:
            return binary_search(sorted_list, l, mid - 1, el)
        else:
            return binary_search(sorted_list, mid + 1, r, el)
    else:
        return -1


# sorted_list = [1, 2, 3, 5, 7, 9, 11, 13, 16]
# el = 7
# result = binary_search(sorted_list, 0, len(sorted_list) - 1, el)
#
# if result != -1:
#     print(f"Element is present at index {result}")
# else:
#     print("Element is not present in array")