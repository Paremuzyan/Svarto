def sum_of(numbers_list):
    result = 0
    for n in numbers_list: result += n
    return result


def product_of(numbers_list):
    result = 1
    for n in numbers_list: result *= n
    return result


def largest_in(numbers_list):
    l_n = numbers_list[0]
    length = len(numbers_list)
    if length < 2:
        return l_n
    for i in range(1, len(numbers_list)):
        if numbers_list[i] > l_n:
            l_n = numbers_list[i]
    return l_n


def smallest_in(numbers_list):
    s_n = numbers_list[0]
    length = len(numbers_list)
    if length < 2:
        return s_n
    for i in range(1, len(numbers_list)):
        if numbers_list[i] < s_n:
            s_n = numbers_list[i]
    return s_n


def ascending_order(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    return unsorted_list


def merge_sort_descending_order(unsorted_list):
    if len(unsorted_list):
        mid = len(unsorted_list) // 2
        left_list = unsorted_list[: mid]
        right_list = unsorted_list[mid:]

        i = 0
        j = 0

        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] > right_list[j]:
                unsorted_list[k] = left_list[i]
                i += 1
            else:
                unsorted_list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            unsorted_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            unsorted_list[k] = right_list[j]
            j += 1
            k += 1

        return unsorted_list


def reverse_of(numbers_list):
    # numbers_list.reverse()
    # return  numbers_list
    return numbers_list[::-1]


if __name__ == "__main__":
    numbers = [8, 0, 41, 2, 1]
    print(f"sum -->  {sum_of(numbers)}")
    print(f"product -->  {product_of(numbers)}")
    print(f"largest element -->  {largest_in(numbers)}")
    print(f"smallest element -->  {smallest_in(numbers)}")
    print(f"ascending order --> {ascending_order(numbers)}")
    print(f"descending order --> {merge_sort_descending_order(numbers)}")
    print(f"revers of {numbers}  --> {reverse_of(numbers)}")
