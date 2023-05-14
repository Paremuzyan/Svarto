class MyTuple:

    def __init__(self, *args):
        self.__tuple = (args)

    def count(self, value):
        count_of_value = 0
        for item in self.__tuple:
            if item == value:
                count_of_value += 1
        return count_of_value

    def index(self, value):
        for i in range(len(self.__tuple)):
            if self.__tuple[i] == value:
                return i
        raise ValueError


