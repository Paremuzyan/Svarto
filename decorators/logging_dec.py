def logging_dec(f):
    def info(*args, **kwargs):
        print(f"The function name is {f.__name__}")
        print(f"The positional arguments are {args}")
        print(f"The key arguments are {kwargs}")
        return_val = f(*args) if args else f(**kwargs)
        print(f"The result is {return_val}")
    return info


@logging_dec
def add(val_1, val_2=6):
    return val_1 + val_2


if __name__ == "__main__":
    add(val_2=7, val_1=1)
