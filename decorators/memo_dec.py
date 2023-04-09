results = {}


def memo_dec(func):
    func_name = func.__name__

    def executing(*args):
        if func_name in results.keys():
            if (args) in results[func_name].keys():
                print('calculated !')
            else:
                print('processing ...')
                results[func_name][(args)] = func(*args)
        else:
            results[func_name] = {}
            print('processing ...')
            results[func_name][(args)] = func(*args)
        print(results)
        return results[func_name][(args)]
    return executing


@memo_dec
def add(n_1, n_2):
    return n_1 + n_2


@memo_dec
def sub(n_1, n_2):
    return n_1 - n_2


if __name__ == "__main__":
    print(add(5, 2))
    print(add(5, 2))
    print(sub(5, 2))
    print(sub(5, 2))
    print(sub(7, 1))
