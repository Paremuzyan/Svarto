def find_gcd_of(n_1, n_2):
    if n_1 < n_2:
        smaller = n_1
    else:
        smaller = n_2
    for i in range(2, smaller+1):
        if ((n_1 % i == 0) and (n_2 % i == 0)):
            return i
    return 1


def find_lcd_of(n_1, n_2):
    if n_1 > n_2:
        greater = n_1
    else:
        greater = n_2

    while True:
        if ((greater % n_1 == 0) and (greater % n_2 == 0)):
            lcm = greater
            return lcm
        greater += 1


if __name__ == "__main__":
    print(find_gcd_of(24, 39))
    print(find_lcd_of(24, 39))
