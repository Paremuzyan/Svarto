def input_to_int(position):
    val = input(f"{position} number is: ")
    while not val.isnumeric():
        val = input("Enter only number: ")
    return int(val)


def calculate_result(n_1, n_2, action):
    if action == "-":
        result = n_1 - n_2
    elif action == "+":
        result = n_1 + n_2
    elif action == "*":
        result = n_1 * n_2
    elif action == "/":
        result = n_1 / n_2
    elif action == "//":
        result = n_1 // n_2
    elif action == "%":
        result = n_1 % n_2
    return result


def main():
    n_1 = input_to_int("First")
    n_2 = input_to_int("Second")
    action = input("Action: ")
    print(f"{n_1} {action} {n_2} = {calculate_result(n_1, n_2, action)}")


if __name__ == "__main__":
    main()
