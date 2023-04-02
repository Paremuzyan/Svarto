def is_negative(number):
    return number < 0


def is_odd(number):
    return number % 2 != 0


def is_vowel(letter):
    vowels = ['A', 'a', 'E', 'e', 'O', 'o', 'U', 'u', 'I', 'i', 'Y', 'y']
    return letter in vowels


def is_numeric(str):
    return str.isnumeric()


def is_small(number):
    return number < 8000


def custom_filter(func, iter_obj):
    result = []
    for obj in iter_obj:
        if func(obj):
            result.append(obj)
    return result


def custom_map(func, iter_obj):
    result = []
    for obj in iter_obj:
        result.append(func(obj))
    return result


word = 'I love Svarto 2023'
numbers_arr = [-10, 2, 5, 9, 3, -5, 8000]
print(list(custom_filter(is_negative, numbers_arr)))
print(list(custom_filter(is_odd, numbers_arr)))
print(list(custom_filter(is_vowel, word)))
print(list(custom_filter(is_numeric, word)))
print(list(custom_map(lambda n: n + 2000, custom_filter(is_small, numbers_arr))))

