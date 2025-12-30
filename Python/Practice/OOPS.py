#ALL OOPS CONCEPTS IN PYTHON (PRACTICE PROGRAM)
#abstraction
from abc import ABC, abstractmethod
class shape:
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class triangle(shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        return 0.5*(self.b*self.h)
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
class pizza(circle):
    def __init__(self,radius):
        super().__init__(radius)
    def area(self):
        return 3.14*self.radius**2
shape=[circle(2),triangle(2,4),rectangle(2,5),pizza(15)]
for i in shape:
    print(f"{i.area()}cm2")

#polymorphism
print()
class vehicle:
    def speak(self):
        print("implementation below")
class car(vehicle):
    def speak(self):
        print("vroom")
class bike(vehicle):
    def speak(self):
        print("boom")
vehicle=[car(),bike()]
for i in vehicle:
    i.speak()

#encapsulation
print()
class vehicle1:
    __color="red"
    __model=2025
    __car="mustang"
    mod="done"
    def display(self):
        print(f"{self.__color} {self.__model} {self.__car}")
    def change(self, color):
        self.__color=color
a=vehicle1()
a.display()
print(a.mod)
a.change("pink")
a.mod="removed"
a.display()
print(a.mod)

#inheritance
print()
class domestic:
    num=0       #class variable
    name="Shreyas"
    def __init__(self,animal,age,color,alive):
        self.animal=animal
        self.age=age
        self.color=color
        self.alive=alive
        domestic.num+=1
    def display(self):
        print(f"{self.color} {self.animal} of age {self.age} still {self.alive}")
    def test(self):
        if self.num>1:
            print("ANIMALSSS")
        else:
            print("only 1 animal...")
    def speak(self):
        print("sounds sounds")
class wild:
    def __init__(self,killer):
        self.killer=killer
    def outcome(self):
        if self.killer:
            print("killer in area")
        else:
            print("savable")
class dog(domestic):            #single inheritance
    def __init__(self,age,color,alive):
        super().__init__("doggy",age,color,alive)
    def speak(self):
        print("bark bark")
class cat(domestic):            #hierarchial inheritance
    def __init__(self,age,color,alive):
        super().__init__("kitty",age,color,alive)
    def speak(self):
        print("meow")
class dogesh(dog):         #multilevel inheritance
    def __init__(self,age,color,alive):
        domestic.__init__(self,"dogesh",age,color,alive)
    def speak(self):
        print("im very dogesh")
class hawk(domestic, wild):     #multiple inheritance
    def __init__(self,age,color,alive,killer):
        domestic.__init__(self,"hawk",age,color,alive)
        wild.__init__(self,killer)
    def speak(self):
        print("cawk")

a=hawk(23,"Red","Dead",True)
a.display()
a.speak()
a.outcome()
b=domestic("Tiger",23,"Orange","Alive")
b.display()
b.test()
print(b.num)
print(b.name)
c=domestic("Tiger",23,"Orange","Alive")
print(c.num)
c.test()
c.speak()
d=wild(False)
d.outcome()
e=wild(True)
e.outcome()
