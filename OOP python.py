from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def get_speed(self):
        pass

    @abstractmethod
    def set_speed(self,new_speed):
        pass

class Car(Transport):
    __speed = 80
    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed):
        self.__speed = new_speed


class Train(Transport):
    __speed = 50

    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed):
        self.__speed = new_speed


class Aircraft(Transport):
    __speed = 900

    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed):
        self.__speed = new_speed


a = Car()
b = Train()
c = Aircraft()
a.set_speed(60)
b.set_speed(80)
c.set_speed(500)
print(a.get_speed())
print(b.get_speed())
print(c.get_speed())