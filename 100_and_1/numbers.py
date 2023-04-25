def decimal_to_binary(number):
    binary = ""

    while number > 0:
        binary = str(number % 2) + binary
        number //= 2

    return binary


def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        val = int(binary[i]) * 2**i
        print(val)
        decimal += val
    return decimal


print(decimal_to_binary(10))
print(binary_to_decimal(decimal_to_binary(10)))