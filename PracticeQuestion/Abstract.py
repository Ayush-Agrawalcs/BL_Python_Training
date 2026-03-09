from abc import ABC, abstractmethod
import math

class shape:
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius

class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

circ=circle(7)
rec=rectangle(2,3)

print(circ.area())
print(rec.area())
