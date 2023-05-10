class MyString:
    def __init__(self, string):
        self.__string = string
        self.__length = len(self.__string)

    def __str__(self):
        return self.__string

    def capitalize(self):
        first_letter = self.__string[0]
        capitalized = self.__string
        if ord(first_letter) in range(97, 122):
            capitalized = chr(ord(first_letter) - 32) + self.__string[1:]
        return capitalized

    def casefold(self):
        result = ''
        for letter in self.__string:
            if ord(letter) in range(65, 91):
                letter = chr(ord(letter) + 32)
            result += letter
        return result

    def center(self, length, character=' '):
        if isinstance(length, int) and length >= 0:
            space = length * character
            return space + self.__string + space
        else:
            raise TypeError

    def count(self, sub, start=0, end=None):
        result = 0
        if not end:
            end = self.__length
        for i in range(start, end):
            result += (self.__string[i:i + len(sub)] == sub)
            return result

    # def encode(self, encoding='UTF-8',errors='strict'):
    #     pass

    def endswith(self, value, start=0, end=None):
        if not end:
            end = self.__length
        string = self.__string[start: end]
        if string[-(len(value)): end] == value:
            return True
        else:
            return False

    def startswith(self, value, start=0, end=None):
        if not end:
            end = self.__length
        string = self.__string[start: end]
        if string[start: start+len(value)] == value:
            return True
        else:
            return False

    def expandtabs(self, tabsize=8):
        result = ''
        i = 0
        while i < self.__length:
            if self.__string[i: i+2] == '/t':
                result += tabsize * ' '
                i += 2
                continue
            result += self.__string[i]
            i += 1
        return result

    def find(self, value, start=0, end=None):
        if not end:
            end = self.__length
        index = -1
        for i in range(start, end):
            if self.__string[i:i + len(value)] == value:
                index = i
                return index
        return index

    def format(self, *args):
        parts = self.__string.split("{}")

        if len(parts) != len(args) + 1:
            raise ValueError("Number of placeholders does not match number of values")

        result = ""
        for i in range(len(args)):
            result += parts[i] + str(args[i])
        result += parts[-1]
        return result

    def index(self, value, start=0, end=None):
        if not end:
            end = self.__length
        for i in range(start, end):
            if self.__string[i:i + len(value)] == value:
                index = i
                return index
        raise ValueError

    def isalnum(self):
        not_alphanumeric = " \|+=_-*^$@~!#%&?.,></;:'[]{}()"
        for letter in self.__string:
            if letter in not_alphanumeric:
                return False
        return True

    def isalpha(self):
        not_alphanumeric = " \|+=_-*^$@~!#%&?.,></;:'[]{}()1234567890"
        for letter in self.__string:
            if letter in not_alphanumeric:
                return False
        return True

    def isascii(self):
        for letter in self.__string:
            if ord(letter) > 127:
                return False
        return True

    def isdecimal(self):
        digits = '0123456789\u00B2'
        for letter in self.__string:
            if letter not in digits:
                return False
        return True

    def isidentifier(self):
        symbols = " \|+=-*^$@~!#%&?.,></;:'[]{}()"
        numbers = '0123456789'
        first = 0
        identifier = True
        if self.__string[first] not in symbols and self.__string[first] not in numbers:
            for i in range(1, len(self.__string)):
                if self.__string[i] in symbols:
                    identifier = False
                    break
        else:
            identifier = False
        return identifier

    def islower(self):
        for letter in self.__string:
            if ord(letter) in range(65, 91):
                return False
        return True

    def isnumeric(self):
        digits = '0123456789'
        for letter in self.__string:
            if letter not in digits:
                return False
        return True

    def isprintable(self):
        escape_characters = r"\\n\t\r\b\f\x16"
        i = 0
        while i < len(self.__string):
            if repr(self.__string)[i: i + 2] in escape_characters:
                return False
            i += 1
        return True

    def isspace(self):
        for char in self.__string:
            if char != ' ':
                return False
        return True

    def istitle(self):
        splited_string = self.__string.split()
        for i in range(len(splited_string)):
            for j in range(len(splited_string[i])):
                if i == 0 and j == 0:
                    if ord(splited_string[i][j]) not in range(65, 91):
                        return False
                if splited_string[i][j] in range(65, 91):
                    return False
        return True




# print(ord('a'))
# print(ord('z'))
# print(ord('A'))
# print(ord('Z'))

my_string = MyString('Asdh ghj ghj')
# print(my_string.capitalize())
# print(my_string.casefold())
# print(my_string.center(9, '*'))
# print(my_string.count('mY', 5))
# print(my_string.endswith('Object', 0, 8))
# print(my_string.expandtabs(2))
# print(my_string.find(" "))
# print(my_string.format('ffffff', 'iiiiiii'))
# print(my_string.index(" "))
# print(my_string.isalnum())
# print(my_string.isalpha())
# print(my_string.isdecimal())
# print(my_string.islower())
# print(my_string.isprintable())
print(my_string.istitle())
