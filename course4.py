#Course 4.1: Classes

# x = 1
# print(type(x))

# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: John, Mary, Jack


#Course 4.2: Creating Classes

# class Point:
#     def draw(self):
#         print("draw")

# point = Point()
# print(type(point))
# print(isinstance(point, int))


#Course 4.3: Constructors

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         # print("draw")
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# # print(point.x)
# point.draw(point)


#Course 4.4: Class vs Instance Attributes

# class Point:
#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# Point.default_color = "yellow"

# point = Point(1, 2)
# # point.z = 10
# print(point.default_color)
# print(Point.default_color)
# point.draw()

# another = Point(3, 4)
# print(another.default_color)
# another.draw()


#Course 4.5: Class vs Instance Methods

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod #Decorator: a way to extend the way of a method or a function
#     def zero(cls):
#         return cls(0, 0)
    
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# # point = Point(0, 0, 1, "a")
# point = Point.zero()
# point.draw()


#Course 4.6: Magic Methods

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"
    
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1, 2)
# # point.__str__
# print(str(point))


#Course 4.7: Comparing objects

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y
    

# point = Point(10, 20)
# other = Point(1, 2)
# # print(point == other)
# print (point > other)


#Course 4.8: Performing Arithmetic Operations

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)


# point = Point(10, 20)
# other = Point(1, 2)
# combined = point + other
# print(combined.x)


#Course 4.9: Making Custom Containers

# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)
    
#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)
    
#     def __iter__(self):
#         return iter(self.tags)
     
# cloud = TagCloud()
# cloud["python"] = 10
# len(cloud)
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags)


#Course 4.10: Private Members

# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)
    
#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)
    
#     def __iter__(self):
#         return iter(self.__tags)
     
# cloud = TagCloud()
# print(cloud._TagCloud__tags)
# print(cloud.__tags)
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags["PYTHON"])


#Course 4.11: Properties

# class Product:
#     def __init__(self, price):
#         # self.__price = price
#         # self.set_price(price)
#         self.price = price

#     @property
#     # def get_price(self):
#     def price(self):
#         return self.__price
    
#     # @price.setter
#     # # def set_price(self,value):
#     # def price(self, value):
#     #     if value < 0:
#     #         raise ValueError("Price cannot be negative.")
#     #     self.__price = value

#     # price = property(get_price, set_price)

# product = Product(10)
# product.price = 2
# # product.price = -1
# print(product.price)


#Course 4.12: Inheritance

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")

# # Animal: Parent, Base
# # Mammal: Child, Sub
# class Mammal(Animal):
#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")

# m = Mammal()
# m.eat()
# print(m.age)


#Course 4.13: The Object Class

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")

# # Animal: Parent, Base
# # Mammal: Child, Sub

# class Mammal(Animal):
#     def walk(self):
#         print("walk")


# m = Mammal()
# print(isinstance(m, object))
# # o = object()
# print(issubclass(Mammal, object))


#Course 4.14: Method Overriding

# Method overriding means replacing or extending a method defined in the base class.
# class Animal:
#     def __init__(self):
#         print("Animal Constructor")
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def __init__(self):
#         print("Mammal Constructor")
#         self.weight = 2
#         super().__init__()

#     def walk(self):
#         print("walk")


# m = Mammal()
# print(m.age)
# print(m.weight)


#Course 4.15: Multi-Level Inheritance

# class Animal:
#     def eat(self):
#         print("eat")

# class Bird(Animal):
#     def fly(self):
#         print("fly")

# class Chicken(Bird):
#     pass

# Multi-Level Inheritance should be avoided at all cost. If you want to use inheritance, use only 1 or 2 levels.


#Course 4.16: Multiple Inheritance

# # class Employee:
# #     def greet(self):
# #         print("Employee Greet")


# class Flyer:
#     def fly(self):
#         pass


# # class Person:
# #     def greet(self):
# #         print("Person Greet")


# class Swimmer:
#     def swim(self):
#         pass


# # class Manager(Employee, Person):
# # class Manager(Person, Employee):
# #     pass


# class FlyingFish(Flyer, Swimmer):
#     pass

# # manager = Manager()
# # manager.greet()


#Course 4.17: A Good Example of Inheritance

# class InvalidOperationError(Exception):
#     pass

# class Stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")
#         self.opened = False

# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")


#Course 4.18: Abstract Base Classes

# from abc import ABC, abstractmethod

# class InvalidOperationError(Exception):
#     pass

# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open.")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass

# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")

# class MemoryStream(Stream):
#     def read(self):
#         print("Reading data from a memory stream.")

# # stream = Stream()
# stream = MemoryStream()
# stream.open()


#Course 4.19: Polymorphism

# from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")


# class DropDownlist(UIControl):
#     def draw(self):
#         print("DropDownList")


# # def draw(control):
# def draw(controls):
#     for control in controls:
#         control.draw()

# ddl = DropDownlist()
# # print(isinstance(ddl, UIControl))
# textbox = TextBox()
# # draw(ddl)
# # draw(textbox)
# draw([ddl, textbox])


#Course 4.20: Duck Typing

from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class TextBox():
#     def draw(self):
#         print("TextBox")


# class DropDownlist():
#     def draw(self):
#         print("DropDownList")


# # def draw(control):
# def draw(controls):
#     for control in controls:
#         control.draw()

#It is called duck typing. Polymorphism works even without a specific class. If it walks like a duck and sounds like a duck, it is a duck.


#Course 4.21: Extending Built-in Typing

# class Text(str):
#     def duplicate(self):
#         return self + self
    
# # text = Text("Python")
# # print(text.lower())
# # print(text.duplicate())

# class TrackableList(list):
#     def append(self, object):
#         print("Append called")
#         super().append(object)

# list = TrackableList()
# list.append("1")


#Course 4.22: Data Classes

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

# from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"])
# # p1 = Point(1, 2)
# # p2 = Point(1, 2)
# # print(p1 == p2)
# # print(id(p1))
# # print(id(p2))
# p1 = Point(x=1, y=2)
# # print(p1.x)
# # p1.x = 10
# p1 = Point(x=10, y=20)
# p2 = Point(x=1, y=2)
# print(p1 == p2)
