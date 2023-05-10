class Weapon:
    def __init__(self, type, weight, caliber, distance, cartridge_count):
        self.set_type(type)
        self.set_weight(weight)
        self.set_caliber(caliber)
        self.set_distance(distance)
        self.set_cartridge_case(cartridge_count)
        self.__cartridges_initial_count = cartridge_count


    def __str__(self):
        return f"Type is {self.__type}. \nWeight is {self.__weight} kg." \
               f" \nCaliber is {self.__caliber} mm. \nStrike distance is {self.__distance} m."

    def set_type(self, type):
        self.__type = type

    def set_weight(self, weight):
        self.__weight = weight

    def set_caliber(self, caliber):
        self.__caliber = caliber

    def set_distance(self, distance):
        self.__distance = distance

    def set_cartridge_case(self, cartridge_count):
        self.__cartridge_case = cartridge_count

    def get_type(self):
        return self.__type

    def get_weight(self):
        return self.__weight

    def get_caliber(self):
        return self.__caliber

    def get_distance(self):
        return self.__distance

    def reload(self, cartridges_count):
        if cartridges_count <= self.__cartridges_initial_count:
            self.set_cartridge_case(cartridges_count)
            print('The cartridge case is full!')
        else:
            print(f'For {self.__type} type of weapon the max count of cartridges'
                  f' is {self.__cartridges_initial_count}.')


    def shoot(self):
        if self.__cartridge_case > 0:
            if self.__cartridge_case == 1:
                print('This was the last cartridge! Be careful.')
            self.__cartridge_case -= 1
            print('shooting! boom boom')

        if self.__cartridge_case == 0:
            print("There is no cartridge. You need to reload the weapon!")
            return






if __name__ == "__main__":
    gun = Weapon('gun', 3, 7.16, 50, 15)
    print(gun)
    for i in range(15):
        gun.shoot()
    gun.reload(20)
