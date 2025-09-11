#abstract class
# Create an abstract class Shape that defines:
 
# An abstract method area() (no implementation).

# Create two child classes that inherit from Shape:

# Rectangle → has attributes length, breadth, and implements area().

# Circle → has attribute radius, and implements area().

# Task:

# Define the abstract class Shape using the abc module.

# Implement Rectangle and Circle classes by providing their own version of area().

# Create one object of Rectangle and one of Circle, then display their areas.
 
from abc import ABC, abstractmethod
 
# Abstract class

class Shape(ABC):
 
    @abstractmethod           # Abstract method

    def area(self):

        pass   

 

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self,length,width):
        self.w =width
        self.l = length

    def area(self):
        a= self.w *self.l
        print(f"Area of rectangle: {a}")
    
class Circle(Shape):
    def __init__(self,radius,pi=3.214):
        self.r = radius
        self.pi=pi
        

    def area(self):
        a= self.pi *self.r*self.r
        print(f"Area of circle: {a}")
    
rec = Rectangle(10,20)
rec.area()

cir= Circle(3)
cir.area()
        


