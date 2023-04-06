def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        key = unsorted_list[i]
        j = i - 1
        while j >= 0 and unsorted_list[j] > key:
            unsorted_list[j+1] = unsorted_list[j]
            j -= 1
        unsorted_list[j+1] = key
    return unsorted_list


if __name__ == "__main__":
    unsorted_list = [8, 7, 4, 1, 65, 456]
    sorted_list = insertion_sort(unsorted_list)
    print(sorted_list)
