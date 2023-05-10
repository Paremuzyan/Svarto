class Human:
    def __init__(self, name, surname, age, hair_color, height, lives):
        self._name = name
        self._surname = surname
        self._age = age
        self._hair_color = hair_color
        self._height = height
        self._lives = lives


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def age(self):
            return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            self.__age = 18

    @property
    def hair_color(self):
        return self._hair_color

    @hair_color.setter
    def hair_color(self, hair_color):
        self._hair_color = hair_color

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if isinstance(height, int) and height > 0:
            self._height = height

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        if isinstance(lives, int) and lives > 0:
            self._lives = lives

    def walking(self):
        print(f'{self._name()} is walking! ', end='')
        for i in range(10):
            print('step ', end='')
        print()

    def running(self):
        print(f'{self._name()} is running! ', end='')
        for i in range(10):
            print('run.... ', end='')
        print()

    def speaking(self, speech):
        print(f'{self._name()} is speaking! ')
        print(speech)

    def shooting(self, who):
        return f'{self._name} shoots {who}...'



if __name__ == "__main__":
    m = Human('M', 'N', 19, 'black', 180, 5)
    m.name='Poghos'
    print(m.name)
    # m.walking()
    # m.running()
    # m.speaking('Hello !')


