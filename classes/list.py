class MyList:
    def __init__(self, *args):
        self.__list = []
        for arg in args:
            self.append(arg)

    def __str__(self):
        return f"CustomList: {str(self.__list)}"

    def append(self, element):
        self.__list += [element]

    def clear(self):
        MyList.__list = []

    def copy(self):
        cp_list = []
        for item in self.__list:
            cp_list += [item]
        return cp_list

    def count(self, value):
        count_of_value = 0
        for item in self.__list:
            if item == value:
                count_of_value += 1
        return count_of_value

    def extend(self, iterable):
        try:
            for iter in iterable:
                self.__list += [iter]
        except:
            return f"{type(iterable)} is not iterable "

    def index(self, element):
        for i in range(len(self.__list)):
            if self.__list[i] == element:
                return i
        raise ValueError

    def insert(self, position, element):
        tmp1 = self.__list[:position]
        tmp2 = self.__list[position:]
        self.__list = tmp1 + [element] + tmp2

    def pop(self, pos=-1):
        if pos > 0:
            tmp1 = self.__list[:pos]
            tmp2 = self.__list[pos+1:]
            self.__list = tmp1 + tmp2
        else:
            self.__list = self.__list[:pos]

    def remove(self, element):
        for i in range(len(self.__list)):
            if self.__list[i] == element:
                tmp1 = self.__list[:i]
                tmp2 = self.__list[i+1:]
                self.__list = tmp1 + tmp2
                return
        raise ValueError

    def reverse(self):
        self.__list = self.__list[::-1]

    def sort(self, reverse=False):
        n = len(self.__list)
        for i in range(n):
            for j in range(n-1-i):
                if self.__list[j] > self.__list[j+1]:
                    self.__list[j], self.__list[j+1] = self.__list[j+1], self.__list[j]
        if reverse:
            self.reverse()



if __name__ == "__main__":
    my_list = MyList(4, 7, 3, 9, 0)
    # my_list.append(9999)
    print(my_list)
    # my_list.clear()
    # cp_list = my_list.copy()
    # print('cp_list --> ', cp_list)
    # cp_list.append('new')
    # print('cp_list --> ', cp_list)
    # print(cp_list.count(9999))
    # cp_list.extend([9, 75, 64])
    # print(cp_list)
    # my_list.insert(2, 0)
    # my_list.pop(1)
    # my_list.remove(0)
    # my_list.reverse()
    my_list.sort(False)
    print(my_list)
