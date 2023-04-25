def length_of(string):
    return f"len({string}) is {len(string)}"


def concatenate(s_1, s_2):
    return s_1 + s_2


def substring_index(main_string, substring):
    for i in range(len(main_string)):
        if main_string[i:i + len(substring)] == substring:
            return i
    return -1


def replace_substring(main_string, subs_1, subs_2):
    i = substring_index(main_string, subs_1)
    if i:
        return main_string[:i] + subs_2 + main_string[i+len(subs_1):]
    else:
        return f"Something went wrong! Couldn't find {subs_1} in {main_string}"


def how_many_time(main_string, substring):
    main_str_copy = main_string
    count = 0
    while len(main_string) > 0:
        s_i = substring_index(main_string, substring)
        if s_i > 0:
            count += 1
            main_string = main_string[s_i + len(substring):]
        else:
            break
    return f"'{substring}' in '{main_str_copy}' are {count} time"


def check_type_of_chars(input_str, type):
    numbers = "0123456789"
    symbols = """!”#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
    result = True
    for char in input_str:
        if char == " ":
            continue
        if type == "alpha":
            if char in numbers or char in symbols:
                result = False
                break
        if type == "numeric":
            if not char in numbers:
                result = False
                break
        if type == "alpha-numeric":
            if char in symbols:
                result = False
                break
    return result


def is_palindrome(input_str):
    if check_type_of_chars(input_str, 'alpha-numeric'):
        input_str = input_str.replace(' ', '').lower()
    return input_str == input_str[::-1]


def vowels_count(input_str):
    vowels = 'AaUuEeIiYyOo'
    count = 0
    for letter in input_str:
        if letter in vowels:
            count += 1
    return count


def words_count(input_str):
    # words_count = len(list(input_str))
    stop_symbols = ' .!'
    words_list = []
    word = ''
    input_str = input_str.strip()
    for letter in input_str:
        if not letter in stop_symbols:
            word += letter
        else:
            words_list.append(word)
            word = ''
    return len(words_list)


if __name__ == "__main__":
    string = "This is a test string test and test again."
    s_1 = "First part "
    s_2 = "Second part. It's working!"
    list_of_str = string.split()
    str_of_lis = " ".join(list_of_str)
    palindrome_strs = ["A man, a plan, a canal, Panama!",
                       "Was it a car or a cat I saw?",
                       "No x in Nixon"]

    # print(length_of(string))
    # print(concatenate(s_1, s_2))
    # print(substring_index(string, "test"))
    # print(replace_substring(string, "test", "!!!!!!!"))
    # print(how_many_time(string, "test"))
    # print(string.upper())
    # print(string.lower())
    # print(string.strip())
    # print(list_of_str)
    # print(str_of_lis)
    # print(is_palindrome(palindrome_strs[2]))
    # print(check_type_of_chars(string, 'alpha'))
    # print(vowels_count(string))
    # print(words_count(string))
