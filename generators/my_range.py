def my_range(stop, start=0, step=1):
    while start < stop:
        yield start
        start += step

for number in my_range(10, 1, 2):
    print(number)
