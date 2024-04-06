# method overwriting: child class overwrites the parent method

class Car:
    def turnOn(self):
        print("you turnOn this car")
        return self # this is for method chaining

    def drive(self):
        print("you drive this car")
        return self # this is for method chaining

    def brake(self):
        print("you brake this car")
        return self # this is for method chaining

    def turnOff(self):
        print("you turnOff this car")
        return self # this is for method chaining

class Pride(Car):
    def drive(self):
        print('someone is about to die!')


pride = Pride()
pride.drive()

# method chaining: calling multiple methods sequentially, each call performs an action on the same object and returns self

car = Car()

car.drive().turnOff()

car.turnOff()\
.drive()\
.brake()\
.turnOff()