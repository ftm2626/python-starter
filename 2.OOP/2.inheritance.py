class Animal:

    alive = True

    def eat(self):
        print("this animal is eating")
    
    def sleep(self):
        print("this animal is sleeping")

class Pray(Animal):
    def flee(self):
        print('this animal is fleeing')

class Preditor(Animal):
    def hunt(self):
        print('this animal is hunting')

class Rabbit(Pray):
    pass

class Fish(Pray,Preditor):
    pass

class Hawk(Preditor):
    pass


fish = Fish()
fish.eat()
fish.flee()
fish.hunt()


# 04:01:50