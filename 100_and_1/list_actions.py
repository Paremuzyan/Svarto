import random
import math
from is_even_odd import is_odd, is_even


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


def evens_sum(numbers_list):
    result = 0
    for number in numbers_list:
        if is_even(number):
            result += number
    return result


def odds_sum(numbers_list):
    result = 0
    for number in numbers_list:
        if is_odd(number):
            result += number
    return result


def average_of(numbers_list):
    average = sum_of(numbers_list) / len(numbers_list)
    return average


def without_duplicates(numbers_list):
    # return set(numbers_list)
    only_uniqes = []
    for element in numbers_list:
        if element in only_uniqes:
            continue
        else:
            only_uniqes.append(element)
    return only_uniqes


def second_smallest_in(numbers_list):
    smallest_1 = smallest_in(numbers_list)
    numbers_list.remove(smallest_1)
    smallest_2 = smallest_in(numbers_list)
    return smallest_2


def second_largest_in(numbers_list):
    largest_1 = largest_in(numbers_list)
    numbers_list.remove(largest_1)
    largest_2 = largest_in(numbers_list)
    return largest_2


def median_of(sorted_list):
    length = len(sorted_list)
    mid = length // 2
    if is_odd(length):
        return sorted_list[mid]

    return (sorted_list[mid] + sorted_list[mid - 1]) / 2


def find_key_by_value(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key


def mode_of(numbers_list):
    sorted_list = ascending_order(numbers_list)
    frequency = {}
    for n in sorted_list:
        if n in frequency:
            frequency[n] += 1
        else:
            frequency[n] = 1
    max_count = largest_in(list(frequency.values()))
    mode = find_key_by_value(frequency, max_count)
    return mode


def n_list_to_bin_str(numbers_list):
    binary_str = ''.join(format(x, '08b') for x in numbers_list)
    return binary_str


def bin_str_to_n_list(binary_str):
    chunks = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]
    numbers_list = []
    for chunk in chunks:
        for n in chunk:
            numbers_list.append(int(n))
    return numbers_list


def variance_for(numbers_list):
    average = average_of(numbers_list)
    length = len(numbers_list)
    variance = sum((x - average) ** 2 for x in numbers) / (length - 1)
    return variance


def standard_deviation_for(numbers_list):
    variance = variance_for(numbers_list)
    s_d = math.sqrt(variance)
    return s_d


def natural_numbers(number):
    result = []
    for i in range(1, number + 1):
        result.append(i)
    return result


def sum_square_of_natural_numbers(n):
    naturals = natural_numbers(n)
    squares_sum = sum(list(map(lambda x: x**2, naturals)))
    return squares_sum


def sum_cube_of_natural_numbers(n):
    naturals = natural_numbers(n)
    squares_sum = sum(list(map(lambda x: x**3, naturals)))
    return squares_sum


def random_numbers():
    numbers = []
    while len(numbers) < 10:
        numbers.append(random.randint(1, 100))
    return numbers


if __name__ == "__main__":
    numbers = [8, 0, 41, 2, 1]
    # print(f"sum -->  {sum_of(numbers)}")
    # print(f"product -->  {product_of(numbers)}")
    # print(f"largest element -->  {largest_in(numbers)}")
    # print(f"smallest element -->  {smallest_in(numbers)}")
    # print(f"ascending order --> {ascending_order(numbers)}")
    # print(f"descending order --> {merge_sort_descending_order(numbers)}")
    # print(f"revers of {numbers}  --> {reverse_of(numbers)}")
    # print(evens_sum(numbers))
    # print(odds_sum(numbers))
    # print(average_of(numbers))
    # print(without_duplicates(numbers))
    # print(second_smallest_in(numbers))
    # print(second_largest_in(numbers))
    # print(median_of([1,2,3,4,5]))
    # print(mode_of([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]))
    # print(n_list_to_bin_str([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]))
    # print(bin_str_to_n_list([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]))
    # print(standard_deviation_for(numbers))
    # print(sum_cube_of_natural_numbers(10))
    print(random_numbers())

    