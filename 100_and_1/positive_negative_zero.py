from print_result import input_to_int

n = input_to_int("Checking")
if n > 0:
    print(f"{n} is positive!")
elif n < 0:
    print(f"{n} is negative!")
else:
    print(f"zero!")
