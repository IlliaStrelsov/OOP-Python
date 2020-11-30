from abc import ABC, abstractmethod
import math
import pymongo


class SingletonMetaclass(type):
    __instance = {}

    def __call__(cls,*args,**kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super().__call__(*args,**kwargs)
        return cls.__instance[cls]


class DataBase(metaclass=SingletonMetaclass):

    def insert(self,continent:str,country:str,city:str,longitude:float,latitude:float):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["Studing"]
        mydict = {"Continent": continent, "Country": country, "City": city, "longitude_coordinate": longitude,"latitude_coordinate": latitude}
        x = mycol.insert_one(mydict)

    def select(self,city:str):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["Studing"]
        myquery = {"City":city}
        mydoc = mycol.find(myquery)
        return mydoc[0]




class Continent:

    def __init__(self,name):
        self.name_cont = name

    def get_continent_name(self):
        return self.name_cont

    def set_continent_name(self,new_name):
        self.name_cont = new_name


class Country:
    def __init__(self, name):
        self.name_coun = name

    def get_country_name(self):
        return self.name_coun

    def set_country_name(self, new_name):
        self.name_coun = new_name


class City:
    def __init__(self, name):
        self.name_city = name

    def get_country_name(self):
        return self.name_city

    def set_country_name(self, new_name):
        self.name_city = new_name






class Transport(ABC):
    @abstractmethod
    def get_speed(self):
        pass

    @abstractmethod
    def set_speed(self,new_speed):
        pass


class Car(Transport):
    speed = 80

    def get_speed(self):
        return self.speed

    def set_speed(self, new_speed):
        if type(new_speed) == str:
            raise WrongInput('Wrong input')
        if new_speed>250 or new_speed<30:
            raise WrongSpeedNumber('Wrong speed number')
        self.speed = new_speed


class Train(Transport):
    speed = 50

    def get_speed(self):
        return self.speed

    def set_speed(self, new_speed):
        if (type(new_speed) == str):
            raise WrongInput('Wrong input')
        if (new_speed > 250 or new_speed < 30):
            raise WrongSpeedNumber('Wrong speed number')
        self.speed = new_speed


class Aircraft(Transport):
    speed = 900

    def get_speed(self):
        return self.speed

    def set_speed(self, new_speed):
        if (type(new_speed) == str):
            raise WrongInput('Wrong input')
        if (new_speed > 3000 or new_speed < 300):
            raise WrongSpeedNumber('Wrong speed number')
        self.speed = new_speed





class Cordinates:
    def __init__(self,x,y):
        if (type(x) == str or type(y) == str):
            raise WrongInput('Wrong input')
        if (y < -180 or y > 180 or x < -90 or x > 90):
            raise WrongCoordinates(f'Coordinates can ту only from -90 to 90 if it`s latitude and from -180 to 180 if it`s longitude')
        self.x = x
        self.y = y

    def set_cordinates(self,x,y):
        if (type(x) == str or type(y) == str):
            raise WrongInput('Wrong input')
        if (y < -180 or y > 180 or x < -90 or x > 90):
            raise WrongCoordinates(f'Coordinates can ту only from -90 to 90 if it`s latitude and from -180 to 180 if it`s longitude')
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
    def change_into_km_from_meters(self, a):
        self.a = a /1000
        return self.a
    def change_into_meters_from_km(self, a):
        self.a = a * 1000
        return self.a
    def from_meters_into_miles(self, a):
        self.a = a * 0.000621371
        return self.a
    def from_miles_into_meters(self, a):
        self.a = a / 0.000621371
        return self.a


class TravelTime:

    def get_time(self,distant,speed):
        return  distant/speed








class WrongInput(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class WrongCoordinates(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class WrongSpeedNumber(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def run():
    while True:
        try:
            print("1.Distance beetwen 2 cities")
            print("2.Find distance between 2 points")
            print("3.Get information about city")
            print("4.Exit")
            x = int(input())
            if x == 1:
                print("Enter a name of the first city")
                first = str(input())
                print("Enter a name of the second city")
                second = str(input())
                find = DataBase()
                try:
                    coordinates = find.select(first)
                    cor1 = coordinates["longitude_coordinate"]
                    cor2 = coordinates["latitude_coordinate"]
                    first_city = Cordinates(cor1,cor2)
                    coordinate = find.select(second)
                    cor11 = coordinate["longitude_coordinate"]
                    cor21 = coordinate["latitude_coordinate"]
                    second_city = Cordinates(cor11,cor21)
                except TypeError:
                    print("Sorry but we don`t know such city ")
                    print("1.Add this city to DataBase")
                    print("2.Exit to main menu")
                    y = int(input())
                    if y == 1:
                        try:
                            print("Enter a continent where city is located:")
                            cont = str(input())
                            print("Enter a country where city is located:")
                            coun = str(input())
                            print("Enter a name of city:")
                            city = str(input())
                            print("Enter a longitude coordinate:")
                            longitude = float(input())
                            print("Enter a latitude coordinate")
                            latitude = float(input())
                            cord = Cordinates(longitude,latitude)
                            find.insert(cont,coun,city,cord.y,cord.x)
                        except WrongCoordinates as e:
                            print(f'{e}')
                        finally:
                            continue
                    if y ==2:
                        continue
                d = DirectDistance()
                distance = d.get_distance(first_city,second_city)
                l = DistantType()
                distance = l.change_into_km_from_meters(distance)
                print("Distance is:",int(distance),"km")
                print("1.Get time of travel")
                print("2.Exit")
                p = int(input())
                if p == 1:
                    print("Choose transport:")
                    print("1.Car")
                    print("2.Train")
                    print("3.Aircraft")
                    o = int(input())
                    if o == 1:
                        car = Car()
                        print("1.Set speed")
                        print("2.Set default speed(50 km per hour)")
                        m = int(input())
                        if m == 1:
                            try:
                                print("Enter a value of speed(km per hour):")
                                j = int(input())
                                car.set_speed(j)
                                time = TravelTime()
                                timing = time.get_time(distance,car.speed)
                                print("Time of travel is about",int(timing),"hours\n\n\n")
                            except WrongSpeedNumber as e:
                                print(f'{e}\n\n\n')
                            except WrongInput as e:
                                print(f'{e}\n\n\n')
                            except ValueError:
                                print(f'Wrong input\n\n\n')
                        if m ==2:
                            time = TravelTime()
                            timing = time.get_time(distance, car.speed)
                            print("Time of travel is about", int(timing), "hours\n\n\n")

                    if o == 2:
                        train = Train()
                        time = TravelTime()
                        timing = time.get_time(distance, train.speed)
                        print("Time of travel is about", int(timing), "hours\n\n\n")

                    if o == 3:
                        aircraft = Aircraft()
                        time = TravelTime()
                        timing = time.get_time(distance, aircraft.speed)
                        print("Time of travel is about", int(timing), "hours\n\n\n")

                if p == 2:
                    continue

            if x == 4:
                break

            if x == 3:
                find = DataBase()
                print("Enter name of city:")
                city = str(input())
                try:
                    info  = find.select(city)
                    continent = info["Continent"]
                    country = info["Country"]
                    city = info["City"]
                    longitude = info["longitude_coordinate"]
                    latitude = info["latitude_coordinate"]
                    print(city,"is located on",continent,"in country",country,"with such coordinates of longitube:",longitude," and latitude:",latitude ,'\n\n\n')
                except TypeError:
                    print("Sorry but we don`t know such city ")
                    print("1.Add this city to DataBase")
                    print("2.Exit to main menu")
                    y = int(input())
                    if y == 1:
                        try:
                            print("Enter a continent where city is located:")
                            cont = str(input())
                            print("Enter a country where city is located:")
                            coun = str(input())
                            print("Enter a name of city:")
                            city = str(input())
                            print("Enter a longitude coordinate:")
                            longitude = float(input())
                            print("Enter a latitude coordinate")
                            latitude = float(input())
                            cord = Cordinates(longitude, latitude)
                            find.insert(cont, coun, city, cord.y, cord.x)
                        except WrongCoordinates as e:
                            print(f'{e}')
                        finally:
                            continue
                    if y ==2:
                        continue
            if x == 2:
                print("Enter a longitude of the first point")
                long1= float(input())
                print("Enter a latitudeof the first point")
                lati1 = float(input())
                print("Enter a longitude of the second point")
                long2 = float(input())
                print("Enter a latitudeof the second point")
                lati2 = float(input())
                try:
                    a = Cordinates(long1,lati1)
                    b = Cordinates(long2,lati2)
                    d = DirectDistance()
                    c = d.get_distance(a,b)
                    l = DistantType()
                    print("\n\n",int(l.change_into_km_from_meters(c)),"km\n\n\n")
                except NameError as e:
                    print(f'Error:{e}\n\n\n')
                except WrongInput as e:
                    print(f'{e}\n\n\n')
                except WrongCoordinates as e:
                    print(f'{e}\n\n\n')
        except ValueError:
            print("Wrong Input")
            continue


run()