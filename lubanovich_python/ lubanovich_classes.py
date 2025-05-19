class Thing: ...


example = Thing()
print(Thing, example)


class Thing2:
    letters = "abc"


print(Thing2.letters)


class Thing3:
    def __init__(self):
        self.letters = "xyz"


print(Thing3.letters)


class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return f"{self.__name}, {self.__number}, {self.__symbol}"


element = {"name": "Hydrogen", "symbol": "H", "number": 1}
hydrogen = Element(**element)
hydrogen.name = "lal"
print(hydrogen.name)


class Laser:
    def does(self):
        return "disintegrate"


class Claw:
    def does(self):
        return "crush"


class SmartPhone:
    def does(self):
        return "ring"


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return self.laser.does(), self.claw.does(), self.smartphone.does()


robot = Robot()
print(robot.does())
