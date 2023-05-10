def decimal_to_binary(number):
    binary = ""

    while number > 0:
        binary = str(number % 2) + binary
        number //= 2

    return binary


def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        val = int(binary[i]) * 2 ** i
        decimal += val
    return decimal


def decimal_to_hexadecimal(decimal):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        quotient = decimal // 16
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal = quotient
    return hexadecimal


def hexadecimal_to_decimal(hexadecimal):
    hex_digits = "0123456789ABCDEF"
    decimal = 0
    power = 0
    for digit in hexadecimal[::-1]:
        decimal += hex_digits.index(digit) * (16 ** power)
        power += 1
    return decimal


def hexadecimal_to_binary(hexadecimal):
    hex_binary_digits = {
        '0': '0', '1': '0001',
        '2': '0010', '3': '0011',
        '4': '0100', '5': '0101',
        '6': '0110', '7': '0111',
        '8': '1000', '9': '1001',
        'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101',
        'E': '1110', 'F': '1111'
    }
    binary = ""
    for digit in hexadecimal:
        binary += hex_binary_digits[digit]
    return binary


def is_prime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    return prime


def all_prime_numbers_until(number):
    all_primes = []
    for i in range(2, number + 1):
        if is_prime(i):
            all_primes.append(i)
    return all_primes


def digits_sum(number):
    result = 0
    for n in str(number):
        result += int(n)
    return result


def revers(number):
    result = ''
    while number:
        result += str(number % 10)
        number = number // 10
    return int(result)


def is_palindrome(number):
    return number == int(str(number)[::-1])


if __name__ == "__main__":
    # print(decimal_to_binary(1))
    # print(binary_to_decimal(decimal_to_binary(10)))
    # print(decimal_to_hexadecimal(16))
    # print(hexadecimal_to_decimal('10'))
    # print(hexadecimal_to_binary('10'))
    # print(is_prime(6))
    # print(all_prime_numbers_until(10))
    # print(digits_sum(56))
    # print(revers(567))
    print(is_palindrome(569))
