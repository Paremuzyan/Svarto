class MySet:
    def __init__(self, *args):
        self.set_value(args)

    def set_value(self, args):
        my_set = []
        for arg in args:
            if arg not in my_set:
                my_set.append(arg)
        self.__set = set(my_set)

    def __str__(self):
        return str(self.__set)

    def add(self):
        pass

    def clear(self):
        pass



s = MySet(1,2,3,4,5,5)
print(s)