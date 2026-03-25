#Course 2.1: Lists

letters = ["a", "b", "c"] #List of strings
matrix = [[0, 1], [2, 3]] #Matrix (two-dimensional list)
# zeros = [0] * 100
# print(zeros) #When you multiply a list, it will repeat the items in the list

zeros = [0] * 5
combined = zeros + letters
# print(combined)
numbers = list(range(20)) #Range returns the ranged objects
print(numbers)

chars = list("Hello World")
print(chars)
print(len(chars))


#Course 2.2: Accessing Items

# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# # print(letters)
# # print(letters[0:3])
# # print(letters[:3])
# # print(letters[::])
# print(letters[::2]) #Using double quotes twice will skip on the of the choses letters that are between the first and the ones following it

numbers = list(range(20))
# print(numbers[::2]) #For integers case, using double quotes twice for a specific integer, it will generate the list of the following: if an odd numbers is used it will generate and odd number list, and even number with even numbers list.
print(numbers[::-1]) #Using double quotes on a negative integer, it will reverse the list's order.


#Course 2.3: List Unpacking
numbers = [1, 2, 3, 4, 4, 4, 4, 4, 9]
first, *other, last = numbers
# print(first)
print(first, last)
print(other)

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]


#Course 2.4: Looping Over Lists

letters = ["a", "b", "c"]
# items = (0, "a")
# index, letter = items
for index, letter in enumerate(letters): #enumerate() will help generate objects will give us a tuple, which is iterable.
    print(index, letter) 

#You can use "for" loops to iterate other lists. If you use an index, you can call the "enumerate" function, which returns an enumerate object, which is iterable, and each iteration will return a tuple and unpack the tuple 


#Course 2.5: Adding or Removing Items

letters = ["a", "b", "c"]

#Add
letters.append("d") #append() adds an item into the list
letters.insert(0, "-") #insert() adds an item into the list in position based on the applied index
# print(letters)

#Remove
letters.pop(0) #pop() removes the item you added on the list based on the index. Leaving the parentheses empty will remove the last item on the list.
letters.remove("b") #removes() the first instance of the item on the list.
del letters[0:3] #del removes a range of items on the list.
letters.clear() #clear() deletes all the objects on the list.

print(letters)


#Course 2.6: Finding Items

letters = ["a", "b", "c"]
print(letters.count("d")) #count() gives the number of occurrences of the item mentioned on the list.
# if "d" in letters:
#     print(letters.index("d"))


#Course 2.7: Sorting Lists

# numbers = [3, 51, 2, 8, 6]
# # numbers.sort() #sort() rearranges the order of items
# # numbers.sort(reverse=True) #reverse() rearranges the order of items in reverse
# print(sorted(numbers, reverse=True))  #sorted() functions like the sort method but it will write down the items that have been sorted on the terminal
# print(numbers)

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# # def sort_item(item):
# #     return item[1]

# items.sort(key=sort_item)
# print(items)


#Course 2.8: Lambda(λ) Functions

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items.sort(key=lambda item:item[1]) #lambda is a shorter way to define a function of a list
print(items)


#Course 2.9: Map Function

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# prices = []
# for item in items:
#     prices.append(item[1])

prices = list(map(lambda item: item[1], items)) #map() function takes the lambda function and applies on every item on the iterable.
print(prices)
# for item in x:
#     print(item)


#Course 2.10: Filter Function

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filtered = list(filter(lambda item: item[1] >= 10, items)) #filter() takes two parameters, a function and an iterable thought it applies each item in the iterable
print(filtered)


#Course 2.11: List Comprehensions

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items] #List comprehensions produces the exact same result as a map

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]


#Course 2.12: Zip Function

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc", list1, list2))) #The zip() takes one or more iterables into a larger list


#Course 2.13: Stacks

browsing_session = []
browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# last = browsing_session.pop()
# print(last)
# print(browsing_session)
# print("redirect", browsing_session[-1])
# if not browsing_session:
#     print("disable")
# browsing_session.pop()
# if not browsing_session:
#     browsing_session[-1]


#Course 2.14: Queues

from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")


#Courses 2.15: Tuples

# point = tuple([1, 2])
# point = tuple("Hello World")
point = (1, 2, 3)
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exists")

# point[0] = 10


#Course 2.16: Swapping Variables

x = 10
y = 11

# z = x
# x = y
# y = z

x, y = y, x
a, b = 1, 2
# x, y = (11, 10)

print("x", x)
print("y", y)


#Course 2.17: Arrays

from array import array

numbers = array("i", [1, 2, 3])
# numbers[0] = 1.0


#Course 2.18: Sets

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
# second.add(5)
# second.remove(5)
# len(second)
# print(uniques)
print(first | second) #| Includes all of the items from the set
print(first & second) #& includes only the item repeated in a list
print(first - second) #- removes the items from a second set
print(first ^ second) #^ does not add items repeated from a list in the set

# print(first[0])

if 1 in first:
    print("yes")


#Course 2.19: Dictionaries

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print[point["a"]]
# print(point)
print(point.get("a", 0))
del point["x"]
print(point)
for key, value in point.items():
    print(key, value)


#Course 2.20: Dictionary Comprehensions

# values = []
# for x in range(5):
#     values.append(x * 2)

values = {x: x * 2 for x in range(5)} #We use comprehensions with sets, maps and dictionaries
# {1, 2, 3, 4}
# {1: "a", 2: "b"}
print(values)


#Course 2.21: Generator Expressions

from sys import getsizeof

values = (x * 2 for x in range(100000))
# # print(values)
# # for x in values:
# #     print(x)
# print("gen:", getsizeof(values))
# values = [x * 2 for x in range(100000)]
# print("list:", getsizeof(values))

# print(len(values))


#Course 2.22: Unpacking Operator

# numbers = [1, 2, 3]
# print(*numbers)
# print(1, 2, 3)

# values = list(range(5))
# first = [1, 2]
# second = [3]
# values = [*first, "a", *second, *"Hello"]
# values = [*range(5), *"Hello"]
# print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)