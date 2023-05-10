def is_leap_year(year):
    if year % 4 == 0:
        return f"{year} is a leap year!"
    return f"{year} is not a leap year!"


if __name__ == "__main__":
    print(is_leap_year(2023))
