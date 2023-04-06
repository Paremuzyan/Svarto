def fib_sequance(num):
    num_1, num_2 = 0, 1
    i = 0
    while i < num:
        num_1, num_2 = num_2, num_1 + num_2
    
        yield num_1
        i += 1


for i in fib_sequance(12):
    print(i)
