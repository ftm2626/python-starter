# super(): function used to give access to the methods of a parent class. return a temporary object of a parent class when used

class Rectangle:
    def __init__(self,length,width) :
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)


class Cube(Rectangle):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height = height


square = Square(2,2)
cube = Cube(2,2,2)