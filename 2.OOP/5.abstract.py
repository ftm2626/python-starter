# prevents a user from creating an object of that class, comples a user to override abstract methods in a child class

# abstract class: a class which contaings one or more abstract mehods
# abstract method: a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    def go(self):
        print("you drive the car")

class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")

vehicle = Vehicle() #this does not work
car = Car()
motorcycle = Motorcycle()
car.go()