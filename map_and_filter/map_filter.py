from checking_scripts import is_odd, is_vowel, is_small, is_numeric, is_negative


if __name__ == "__main__":
    word = 'I love Svarto 2567 709 -5'
    numbers_arr = [-10, 2, 5, 9, 3, -5, 8000]
    print(list(filter(is_negative, numbers_arr)))
    print(list(filter(is_odd, numbers_arr)))
    print(list(filter(is_vowel, word)))
    print(list(filter(is_numeric, word)))
    print(is_numeric(word))
    print(list(map(lambda n: n + 2000, filter(is_small, numbers_arr))))
