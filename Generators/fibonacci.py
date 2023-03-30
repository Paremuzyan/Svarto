def fib_sequance(num):
    num_1, num_2 = 0, 1
    for i in range(num):
        num_1, num_2 = num_2, num_1 + num_2
        yield num_1


# for fib_number in fib_sequance(10):
#     print(fib_number, end=', ')
# print()

fib = fib_sequance(10)
default_val = 'done!'
for i in range(12):
    print(next(fib, default_val))

