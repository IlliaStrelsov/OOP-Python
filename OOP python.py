from abc import ABC, abstractmethod
import math
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
        if (type(new_speed) == str):
            raise wrong_input('Wrong input')
        if(new_speed>250 or new_speed<30):
            raise Exception
        self.__speed = new_speed


class Train(Transport):
    __speed = 50

    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed):
        if (type(new_speed) == str):
            raise wrong_input('Wrong input')
        if (new_speed > 250 or new_speed < 30):
            raise Exception
        self.__speed = new_speed


class Aircraft(Transport):
    __speed = 900

    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed):
        if (type(new_speed) == str):
            raise wrong_input('Wrong input')
        if (new_speed > 3000 or new_speed < 300):
            raise Exception
        self.__speed = new_speed





class Cordinates:
    def __init__(self,x,y):
        if (type(x) == str or type(y) == str):
            raise wrong_input('Wrong input')
        if (y < -180 or y > 180 or x < -90 or x > 90):
            raise Exception
        self.x = x
        self.y = y

    def set_cordinates(self,x,y):
        if (type(x) == str or type(y) == str):
            raise wrong_input('Wrong input')
        if (y < -180 or y > 180 or x < -90 or x > 90):
            raise Exception
        self.x = x
        self.y = y

    def get_cordinates(self):
        return [self.x,self.y]


class distanceGetter(ABC):
    @abstractmethod
    def get_distance(self,a:Cordinates,b:Cordinates):
        pass

class DirectDistance(distanceGetter):
    __Earth_radius = 6372795
    def get_distance(self,cor1:Cordinates,cor2:Cordinates):
        self.x1 = cor1.x * math.pi / 180
        self.y1 = cor1.y * math.pi / 180
        self.x2 = cor2.x * math.pi / 180
        self.y2 = cor2.y * math.pi / 180
        self.cl1 = math.cos(self.x1)
        self.cl2 = math.cos(self.x2)
        self.sl1 = math.sin(self.x1)
        self.sl2 = math.sin(self.x2)
        self.delta = self.y2 - self.y1
        self.cdelta = math.cos(self.delta)
        self.sdelta = math.sin(self.delta)

        self.y = math.sqrt(math.pow(self.cl2*self.sdelta,2) + math.pow(self.cl1*self.sl2 - self.sl1* self.cl2 *self.cdelta,2))
        self.x = self.sl1 *self.sl2 + self.cl1 * self.cl2 * self.cdelta

        self.ad = math.atan2(self.y,self.x)
        self.dist = self.ad * self.__Earth_radius
        return int(self.dist)
        # return in meters





class IndirectDistance(distanceGetter):
    def get_distance(self,x,y):
        pass




class DistantType:
    def change_into_km_from_meters(self,a):
        self.a = a /1000
        return self.a
    def change_into_meters_from_km(self,a):
        self.a = a * 1000
        return self.a
    def from_meters_into_miles(self,a):
        self.a = a * 0.000621371
        return self.a
    def from_miles_into_meters(self,a):
        self.a = a / 0.000621371
        return self.a



class wrong_input(Exception):
    def __init__(self,msg):
        super().__init__(msg)




try:
    car = Car()
    air = Aircraft()
    car.set_speed(50)
except wrong_input as e:
    print(f'{e}')
except Exception:
    print('Wrong speed number')
try:
    a = Cordinates(67,-139.398)
    b = Cordinates(67,-139.55)
    d = DirectDistance()
    c = d.get_distance(a,b)
    l = DistantType()
    print(l.change_into_km_from_meters(c))
except NameError as e:
    print(f'Error:{e}')
except wrong_input as e:
    print(f'{e}')
except Exception:
   print(f'Coordinates can ту only from -90 to 90 if it`s latitude and from -180 to 180 if it`s longitude ')


