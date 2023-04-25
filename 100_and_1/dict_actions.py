from list_actions import product_of, sum_of, largest_in, smallest_in, ascending_order, merge_sort_descending_order


def sorted_dict_by_key(dict, sorted_keys):
    result = {}
    for key in sorted_keys:
        result[key] = dict[key]
    return result


def keys_ascending_order(dictionary):
    sorted_keys = ascending_order(list(dictionary.keys()))
    return sorted_dict_by_key(dictionary, sorted_keys)


def keys_descending_order(dictionary):
    sorted_keys = merge_sort_descending_order(list(dictionary.keys()))
    return sorted_dict_by_key(dictionary, sorted_keys)


def find_key_by_value(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key


def sorted_dict_by_values(dict, sorted_values):
    result = {}
    for value in sorted_values:
        key = find_key_by_value(dict, value)
        result[key] = value
    return result


def values_ascending_order(dictionary):
    sorted_values = ascending_order(list(dictionary.values()))
    return sorted_dict_by_values(dictionary, sorted_values)


def values_descending_order(dictionary):
    sorted_values = merge_sort_descending_order(list(dictionary.values()))
    return sorted_dict_by_values(dictionary, sorted_values)


def revers(dictionary):
    sorted_keys = list(dictionary.keys())[::-1]
    return sorted_dict_by_key(dictionary, sorted_keys)


if __name__ == "__main__":
    numbers_dict = {'3': 3, "2": 2, "4": 4, "1": 1}
    # print(sum_of(numbers_dict.values()))
    # print(product_of(numbers_dict.values()))
    # print(largest_in(list(numbers_dict.values())))
    # print(smallest_in(list(numbers_dict.values())))
    # print(keys_ascending_order(numbers_dict))
    # print(keys_descending_order(numbers_dict))
    # print(values_ascending_order(numbers_dict))
    # print(values_descending_order(numbers_dict))
    print(numbers_dict)
    print(revers(numbers_dict))

