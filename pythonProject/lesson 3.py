#
#
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15, 16, 17, 18, 19, 20]
#
# b = []
# c = []
# for i in a:
#     if i % 2 == 0:
#       b.append(i)
#      else:
# c.append(i)
# print(b)
# print(c)






# oop
class Car:
    def __init__(self, name, marka, factory):
        self.name = name
        self.marka = marka
        self.factory = factory

    def __str__(self):
        return f"name: {self.name}\n" \
        f"marka: {self.marka}\n"  \
        f"factory: {self.marka}n"

    def drive(self):
            return f"Lets gooo"


car = Car(name="Kia", marka="k5", factory="Korea")
print(car)
print(car.drive())

class Autocar(Car):
    def __init__(self, name, marka, factory, bak, dvs):
        super(Autocar, self).__init__(name, marka, factory)
        self.bak = bak
        self.dvs = dvs

    def __str__(self):
        return super(Autocar, self).__str__() \
            +f"Bak; {self.bak}\n"\
             f"Dvs: {self.dvs}\n"

    def drive1(self):
        return f"He can drive only with fuel!"

car1 = Autocar(name="Lexus", marka="LX600", factory="Japan", bak=100, dvs=6.0)
print(car1)
print(car1.drive())
print(car1.drive1())


class Electrocar(Car):
    def init(self, name, marka, factory, battery):
        super(Electrocar, self).init(name, marka, factory)
        self.battery = battery

    def str(self):
        return super(Electrocar, self).str() \
             +f"Battery: {self.battery}\n"\

    def drive2(self):
        return f"Hi can drive only with electrica!"

car2 = Electrocar(name="BMW", marka="i8", factory="Germany", battery="+300km")
print(car2)
print(car2.drive())
print(car2.drive2())


# class Hybrid(Autocar, Electrocar):
#     def __init__(self):name, marka, factory, bak, dvs, battery, company):
#         super(Hybrid, self).__init__(name, marka, factory, bak, dvs, battery)
#         self.company = company
