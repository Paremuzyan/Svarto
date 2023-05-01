def difference(set_1, set_2):
    return set_1.difference(set_2)


if __name__ == "__main__":
    set_1 = {1, 2, 3, 4}
    set_2 = {4, 5, 6, 7}
    print(difference(set_1, set_2))
