class Car:
    
    wheels = 4 #class variable

    # this is object / constructor
    # step 1 
    # def __init__(self):
    #     make = None
    #     model = None
    #     year = None
    #     color= None
    # step2
    def __init__(self,make,model,year,color):
        self.make = make #instance variable
        self.model = model #instance variable
        self.year = year #instance variable
        self.color = color #instance variable

    def drive(self):
        print("this "+ self.model +" is driving")
    def stop(self):
        print("this car has stopped")

car_1 = Car("Chevy","Corvetter",2021,"blue")

car_1.wheels = 2 # change default 
Car.wheels = 3 #changes default for everything


print(car_1.color)
print(car_1.wheels)

car_1.drive()
car_1.stop()