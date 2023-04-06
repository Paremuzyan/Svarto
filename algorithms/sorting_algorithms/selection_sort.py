def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        min_val_index = i
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[i]:
                min_val_index = j
        unsorted_list[i], unsorted_list[min_val_index] = unsorted_list[min_val_index], unsorted_list[i]
    return unsorted_list


if __name__ == "__main__":
    unsorted_list = [9, 7, 2, 789]
    print(selection_sort(unsorted_list))
