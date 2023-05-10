def is_negative(number):
    return number < 0


def is_odd(number):
    return number % 2 != 0


def is_vowel(letter):
    vowels = ['A', 'a', 'E', 'e', 'O', 'o', 'U', 'u', 'I', 'i', 'Y', 'y']
    return letter in vowels


def is_numeric(string_obj):
    print(len(string_obj))
    nums = "0123456789"
    result = []
    tmp_num = ""
    i = 0
    while i < len(string_obj):
        if string_obj[i] in nums:
            j = i
            while string_obj[j] in nums and j < len(string_obj) - 1:
                j += 1
            tmp_num = string_obj[i:] if j == len(string_obj) - 1 else string_obj[i: j]
            result.append(tmp_num)
            tmp_num = ""
            i += j
        else:
            i += 1
    return result


def is_small(number):
    return number < 8000
