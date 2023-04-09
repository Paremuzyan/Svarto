def logging_dec(f):
    def info(*args):
        print(f"The function name is {f.__name__}")
        print(f"The positional arguments are {args}")
        return_val = f(*args)
        print(f"The result is {return_val}")
    return info


@logging_dec
def add(val_1, val_2):
    return val_1 + val_2


if __name__ == "__main__":
    add(1, 5)
