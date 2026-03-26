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

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)
     
cloud = TagCloud()
print(cloud._TagCloud__tags)
# print(cloud.__tags)
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags["PYTHON"])