# duck typing : concept where the class on an object is less inportant than the methods/attributes.
#        class type is not checked if minimum methods/attributes are present
#       "if it walked like a duck, and it quacks like a duck, then i must be a duck."

class Duck:
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking")


class Chicken:
    def walk(self):
        print("this chicken is walking")

    def talk(self):
        print("this chicken is chickening")

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)